#!/usr/bin/env python3
"""Valida limites de caractere por canal, de forma determinística.

Modelo de linguagem não conta caractere com confiabilidade; script conta sempre.
Os limites vivem em scripts/limites_canais.json — nunca hardcoded aqui.

Uso:

    # via stdin
    echo '{"canal":"push","campos":{"titulo":"Seu carrinho está guardado",
          "corpo":"Frete e pagamento já preenchidos. Falta confirmar."}}' \
      | python3 validar_limites.py

    # via arquivo
    python3 validar_limites.py --arquivo peca.json

    # saída legível em vez de JSON
    python3 validar_limites.py --arquivo peca.json --formato texto

    # campo repetível (RSA): a lista valida tamanho de cada item e a quantidade
    echo '{"canal":"google_rsa","campos":{"titulo":["Feche o mês em 4h","..."]}}' \
      | python3 validar_limites.py

Entrada:  {"canal": "<nome>", "campos": {"<campo>": "texto" | ["t1","t2"]}}
Saída:    {"canal", "aprovado", "resultados": [...]}
Exit code: 0 = aprovado (inclui avisos), 1 = reprovado, 2 = erro de entrada.

Nota sobre emoji: a contagem é feita em caracteres Unicode (len sobre str).
Plataformas que medem em bytes UTF-8 ou em unidades UTF-16 contam emoji e
caracteres acentuados de forma diferente — para peças com muitos emoji,
trate o resultado como piso, não como valor exato da plataforma.
"""

import argparse
import json
import os
import sys

CAMINHO_LIMITES = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "limites_canais.json")

STATUS_OK = "ok"
STATUS_AVISO = "aviso"
STATUS_ERRO = "erro"


def carregar_limites(caminho=CAMINHO_LIMITES):
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def _contar(texto, regra):
    """Devolve (valor, unidade) conforme a regra usa caracteres ou palavras."""
    if "max_palavras" in regra:
        return len([p for p in texto.split() if p]), "palavras"
    return len(texto), "caracteres"


def _teto(regra):
    return regra.get("max", regra.get("max_palavras"))


def validar_campo(nome, texto, regra):
    """Valida um valor único contra a regra do campo."""
    valor, unidade = _contar(texto, regra)
    teto = _teto(regra)
    recomendado = regra.get("recomendado")

    resultado = {
        "campo": nome,
        unidade: valor,
        "max": teto,
        "texto": texto,
    }
    if recomendado is not None:
        resultado["recomendado"] = recomendado

    if teto is not None and valor > teto:
        resultado["status"] = STATUS_ERRO
        excedente = valor - teto
        rotulo = unidade if excedente != 1 else unidade.rstrip("s")
        resultado["mensagem"] = "acima do máximo: corte %d %s" % (excedente, rotulo)
    elif recomendado is not None and valor > recomendado:
        resultado["status"] = STATUS_AVISO
        resultado["mensagem"] = "acima do recomendado, dentro do máximo"
    else:
        resultado["status"] = STATUS_OK
        resultado["mensagem"] = "dentro do limite"

    if regra.get("nota"):
        resultado["nota"] = regra["nota"]
    return resultado


def validar_quantidade(nome, itens, regra):
    """Valida a quantidade de itens de um campo repetível."""
    minimo = regra.get("quantidade_min")
    maximo = regra.get("quantidade_max")
    total = len(itens)

    resultado = {"campo": nome, "quantidade": total,
                 "quantidade_min": minimo, "quantidade_max": maximo}

    if minimo is not None and total < minimo:
        resultado["status"] = STATUS_ERRO
        resultado["mensagem"] = "faltam %d item(ns): o formato pede no mínimo %d" % (
            minimo - total, minimo)
    elif maximo is not None and total > maximo:
        resultado["status"] = STATUS_ERRO
        resultado["mensagem"] = "%d item(ns) além do máximo de %d" % (total - maximo, maximo)
    else:
        resultado["status"] = STATUS_OK
        resultado["mensagem"] = "quantidade dentro do formato"
    return resultado


def validar(entrada, limites=None):
    """Valida a peça inteira. Devolve o dicionário de saída."""
    limites = limites if limites is not None else carregar_limites()

    canal = entrada.get("canal")
    if not canal:
        raise ValueError("campo 'canal' ausente na entrada")
    if canal not in limites or canal.startswith("_"):
        disponiveis = ", ".join(sorted(c for c in limites if not c.startswith("_")))
        raise ValueError("canal desconhecido: %r. Canais: %s" % (canal, disponiveis))

    campos = entrada.get("campos")
    if not isinstance(campos, dict) or not campos:
        raise ValueError("campo 'campos' ausente ou vazio")

    regras_canal = limites[canal]
    resultados = []

    for nome, valor in campos.items():
        regra = regras_canal.get(nome)
        if regra is None or nome.startswith("_"):
            campos_validos = ", ".join(c for c in regras_canal if not c.startswith("_"))
            resultados.append({
                "campo": nome, "status": STATUS_ERRO,
                "mensagem": "campo inexistente em %r. Campos: %s" % (canal, campos_validos),
            })
            continue

        if isinstance(valor, list):
            resultados.append(validar_quantidade(nome, valor, regra))
            for i, item in enumerate(valor, start=1):
                r = validar_campo("%s[%d]" % (nome, i), item, regra)
                resultados.append(r)
        else:
            resultados.append(validar_campo(nome, valor, regra))

    aprovado = all(r["status"] != STATUS_ERRO for r in resultados)
    return {"canal": canal, "aprovado": aprovado, "resultados": resultados}


def formatar_texto(saida):
    simbolo = {STATUS_OK: "OK  ", STATUS_AVISO: "AVISO", STATUS_ERRO: "ERRO"}
    linhas = ["canal: %s" % saida["canal"]]
    for r in saida["resultados"]:
        if "quantidade" in r:
            medida = "%d item(ns)" % r["quantidade"]
        elif "caracteres" in r:
            medida = "%d/%s caracteres" % (r["caracteres"], r.get("max"))
        elif "palavras" in r:
            medida = "%d/%s palavras" % (r["palavras"], r.get("max"))
        else:
            medida = "-"
        linhas.append("  [%s] %-18s %-22s %s" % (
            simbolo.get(r["status"], r["status"]), r["campo"], medida, r["mensagem"]))
    linhas.append("resultado: %s" % ("aprovado" if saida["aprovado"] else "REPROVADO"))
    return "\n".join(linhas)


def _testes():
    """Casos de teste. Rode com: python3 validar_limites.py --testes"""
    limites = carregar_limites()
    falhas = []

    def checa(nome, condicao):
        if not condicao:
            falhas.append(nome)

    # 1. Push dentro do limite é aprovado, com status ok.
    s = validar({"canal": "push", "campos": {
        "titulo": "Seu carrinho está guardado",
        "corpo": "Frete e pagamento já preenchidos. Falta confirmar."}}, limites)
    checa("1 push aprovado", s["aprovado"] is True)
    checa("1 push contagem", s["resultados"][0]["caracteres"] == 26)

    # 2. Push com título acima do máximo reprova.
    s = validar({"canal": "push", "campos": {"titulo": "x" * 51}}, limites)
    checa("2 push reprova", s["aprovado"] is False)
    checa("2 push status", s["resultados"][0]["status"] == STATUS_ERRO)

    # 3. Acima do recomendado, dentro do máximo: aviso, mas aprovado.
    s = validar({"canal": "push", "campos": {"titulo": "x" * 45}}, limites)
    checa("3 aviso não reprova", s["aprovado"] is True)
    checa("3 status aviso", s["resultados"][0]["status"] == STATUS_AVISO)

    # 4. RSA com títulos de menos reprova por quantidade.
    s = validar({"canal": "google_rsa", "campos": {"titulo": ["Feche o mês em 4h"] * 3}}, limites)
    checa("4 rsa quantidade reprova", s["aprovado"] is False)
    checa("4 rsa item ok", any(r["campo"] == "titulo[1]" and r["status"] == STATUS_OK
                              for r in s["resultados"]))

    # 5. RSA com quantidade suficiente e tamanhos válidos aprova.
    s = validar({"canal": "google_rsa", "campos": {"titulo": ["Feche o mês em 4h"] * 8}}, limites)
    checa("5 rsa aprova", s["aprovado"] is True)

    # 6. Campo em palavras (banner) conta palavras, não caracteres.
    s = validar({"canal": "banner", "campos": {"titulo": "um dois três quatro cinco"}}, limites)
    checa("6 banner palavras", s["resultados"][0]["palavras"] == 5)
    checa("6 banner aprovado", s["aprovado"] is True)

    # 7. Campo inexistente no canal é erro, não silêncio.
    s = validar({"canal": "push", "campos": {"assunto": "oi"}}, limites)
    checa("7 campo inexistente", s["aprovado"] is False)

    # 8. Canal desconhecido levanta ValueError.
    try:
        validar({"canal": "tiktok_ads", "campos": {"titulo": "x"}}, limites)
        checa("8 canal desconhecido", False)
    except ValueError:
        pass

    # 9. Emoji e acento contam como um caractere cada.
    s = validar({"canal": "push", "campos": {"titulo": "café ☕"}}, limites)
    checa("9 unicode", s["resultados"][0]["caracteres"] == 6)

    if falhas:
        print("FALHAS: %s" % ", ".join(falhas))
        return 1
    print("todos os testes passaram")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Valida limites de caractere por canal.",
        epilog="Entrada JSON via stdin ou --arquivo. Exit: 0 aprovado, 1 reprovado, 2 erro.")
    ap.add_argument("--ajuda", action="help", help="mostra esta ajuda e sai")
    ap.add_argument("--arquivo", help="arquivo JSON de entrada (padrão: stdin)")
    ap.add_argument("--formato", choices=["json", "texto"], default="json",
                    help="formato da saída (padrão: json)")
    ap.add_argument("--limites", default=CAMINHO_LIMITES,
                    help="caminho alternativo do limites_canais.json")
    ap.add_argument("--testes", action="store_true", help="roda os casos de teste e sai")
    args = ap.parse_args(argv)

    if args.testes:
        return _testes()

    try:
        bruto = open(args.arquivo, encoding="utf-8").read() if args.arquivo else sys.stdin.read()
        entrada = json.loads(bruto)
        saida = validar(entrada, carregar_limites(args.limites))
    except (OSError, ValueError) as e:
        print(json.dumps({"erro": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2

    if args.formato == "texto":
        print(formatar_texto(saida))
    else:
        print(json.dumps(saida, ensure_ascii=False, indent=2))
    return 0 if saida["aprovado"] else 1


if __name__ == "__main__":
    sys.exit(main())
