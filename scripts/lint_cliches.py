#!/usr/bin/env python3
"""Detecta clichês de copy em PB, de forma determinística.

Modelo de linguagem reconhece clichê por julgamento e erra por inconsistência;
lista fechada acerta sempre. Os termos vivem em scripts/cliches.json.

Uso:

    # via stdin
    echo "Peça versátil com conforto e sofisticação para todos os momentos." \
      | python3 lint_cliches.py

    # via arquivo, saída legível
    python3 lint_cliches.py --arquivo copy.txt --formato texto

    # ignorar categorias que a marca usa legitimamente
    python3 lint_cliches.py --arquivo copy.txt --ignorar cta_fraco,adjetivo_vazio

    # listar as categorias disponíveis
    python3 lint_cliches.py --categorias

Entrada:  texto via stdin ou --arquivo
Saída:    {"total": N, "ocorrencias": [{termo, categoria, posicao, trecho, sugestao}]}
Exit code: 0 = limpo, 1 = clichê encontrado, 2 = erro.

A comparação é insensível a maiúscula e a acento (normalização NFD), mas o
trecho reportado preserva o texto original — o que se corrige é o que está lá.
"""

import argparse
import json
import os
import re
import sys
import unicodedata

CAMINHO_CLICHES = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "cliches.json")

CATEGORIA_TRINCA = "trinca_generica"
MIN_ADJETIVOS_TRINCA = 3
JANELA_TRECHO = 30


def carregar_cliches(caminho=CAMINHO_CLICHES):
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def normalizar(texto):
    """Minúsculas sem acento, preservando o comprimento caractere a caractere.

    Preservar o comprimento é o que permite mapear a posição encontrada no
    texto normalizado de volta para a posição no texto original.
    """
    saida = []
    for ch in texto.lower():
        decomposto = unicodedata.normalize("NFD", ch)
        base = "".join(c for c in decomposto if not unicodedata.combining(c))
        # Se a decomposição mudar o comprimento (ex.: 'ß'), mantém o original.
        saida.append(base if len(base) == 1 else ch)
    return "".join(saida)


def _trecho(texto, inicio, fim):
    a = max(0, inicio - JANELA_TRECHO)
    b = min(len(texto), fim + JANELA_TRECHO)
    prefixo = "..." if a > 0 else ""
    sufixo = "..." if b < len(texto) else ""
    return "%s%s%s" % (prefixo, texto[a:b].replace("\n", " ").strip(), sufixo)


def _categorias(dados):
    return [k for k in dados if not k.startswith("_")]


def buscar_termos(texto, dados, ignorar=()):
    """Encontra cada termo da lista fechada, com fronteira de palavra."""
    normalizado = normalizar(texto)
    sugestoes = dados.get("_meta", {}).get("sugestoes", {})
    ocorrencias = []

    for categoria in _categorias(dados):
        if categoria in ignorar:
            continue
        for termo in dados[categoria]:
            padrao = re.compile(r"(?<!\w)%s(?!\w)" % re.escape(normalizar(termo)))
            for m in padrao.finditer(normalizado):
                ocorrencias.append({
                    "termo": texto[m.start():m.end()],
                    "categoria": categoria,
                    "posicao": m.start(),
                    "trecho": _trecho(texto, m.start(), m.end()),
                    "sugestao": sugestoes.get(categoria, "reescreva com informação concreta"),
                })
    return ocorrencias


def buscar_trincas(texto, dados, ignorar=()):
    """Detecta três ou mais adjetivos vazios encadeados na mesma frase.

    É o padrão mais comum de copy genérica em PB ("estilo, qualidade e
    elegância") e o mais fácil de detectar com certeza — por isso tem
    categoria própria em vez de virar três achados soltos.
    """
    if CATEGORIA_TRINCA in ignorar or "adjetivo_vazio" not in dados:
        return []

    normalizado = normalizar(texto)
    sugestoes = dados.get("_meta", {}).get("sugestoes", {})
    adjetivos = [normalizar(t) for t in dados["adjetivo_vazio"]]
    padrao_adj = re.compile(r"(?<!\w)(?:%s)(?!\w)" % "|".join(
        re.escape(a) for a in sorted(adjetivos, key=len, reverse=True)))

    ocorrencias = []
    inicio_frase = 0
    for fim_frase in [m.end() for m in re.finditer(r"[.!?\n]|$", normalizado)]:
        if fim_frase <= inicio_frase:
            continue
        frase = normalizado[inicio_frase:fim_frase]
        achados = list(padrao_adj.finditer(frase))

        # Só conta como trinca se os adjetivos estiverem encadeados por
        # vírgula ou "e" — não se estiverem espalhados pela frase.
        encadeados = [achados[0]] if achados else []
        for anterior, atual in zip(achados, achados[1:]):
            ligacao = frase[anterior.end():atual.start()]
            if re.fullmatch(r"[\s,]*(?:e|,)?[\s,]*", ligacao):
                encadeados.append(atual)
            else:
                if len(encadeados) < MIN_ADJETIVOS_TRINCA:
                    encadeados = [atual]
                else:
                    break

        if len(encadeados) >= MIN_ADJETIVOS_TRINCA:
            ini = inicio_frase + encadeados[0].start()
            fim = inicio_frase + encadeados[-1].end()
            ocorrencias.append({
                "termo": texto[ini:fim],
                "categoria": CATEGORIA_TRINCA,
                "posicao": ini,
                "trecho": _trecho(texto, ini, fim),
                "sugestao": sugestoes.get(CATEGORIA_TRINCA,
                                          "escolha um atributo concreto e prove"),
            })
        inicio_frase = fim_frase
    return ocorrencias


def lint(texto, dados=None, ignorar=()):
    dados = dados if dados is not None else carregar_cliches()
    ignorar = set(ignorar)
    ocorrencias = buscar_termos(texto, dados, ignorar) + buscar_trincas(texto, dados, ignorar)
    ocorrencias.sort(key=lambda o: (o["posicao"], o["categoria"]))
    return {"total": len(ocorrencias), "ocorrencias": ocorrencias}


def formatar_texto(saida):
    if not saida["total"]:
        return "limpo: nenhum clichê da lista encontrado"
    linhas = ["%d ocorrência(s):" % saida["total"]]
    for o in saida["ocorrencias"]:
        linhas.append("  [%s] %r (pos. %d)" % (o["categoria"], o["termo"], o["posicao"]))
        linhas.append("      trecho: %s" % o["trecho"])
        linhas.append("      %s" % o["sugestao"])
    return "\n".join(linhas)


def _testes():
    """Casos de teste. Rode com: python3 lint_cliches.py --testes"""
    dados = carregar_cliches()
    falhas = []

    def checa(nome, condicao):
        if not condicao:
            falhas.append(nome)

    def cats(saida):
        return {o["categoria"] for o in saida["ocorrencias"]}

    # 1. Copy limpa não gera ocorrência.
    s = lint("Oxford de algodão com elastano, mantém o caimento ao longo do dia.", dados)
    checa("1 limpo", s["total"] == 0)

    # 2. Fórmula fechada e adjetivo vazio são detectados juntos.
    s = lint("Peça versátil com conforto e sofisticação para todos os momentos.", dados)
    checa("2 detecta", s["total"] >= 3)
    checa("2 categorias", {"adjetivo_vazio", "formula_fechada"} <= cats(s))

    # 3. Comparação insensível a acento e a maiúscula; trecho preserva o original.
    s = lint("Produto VERSATIL e Sofisticado.", dados)
    checa("3 sem acento", any(o["termo"] == "VERSATIL" for o in s["ocorrencias"]))
    checa("3 maiuscula", any(o["termo"] == "Sofisticado" for o in s["ocorrencias"]))

    # 4. Trinca genérica encadeada vira categoria própria.
    s = lint("Estilo: moderno, elegante e sofisticado.", dados)
    checa("4 trinca", CATEGORIA_TRINCA in cats(s))

    # 5. Adjetivos espalhados pela frase não viram trinca.
    s = lint("O tecido é moderno. A modelagem é elegante. O acabamento é impecável.", dados)
    checa("5 nao e trinca", CATEGORIA_TRINCA not in cats(s))

    # 6. --ignorar remove a categoria da saída.
    s = lint("Peça versátil e exclusiva.", dados, ignorar={"adjetivo_vazio"})
    checa("6 ignorar", "adjetivo_vazio" not in cats(s))

    # 7. Fronteira de palavra: 'confira' não casa dentro de outra palavra.
    s = lint("Nós confirmamos o pedido e conferimos o estoque.", dados)
    checa("7 fronteira", s["total"] == 0)

    # 8. Posição reportada aponta para o termo no texto original.
    texto = "Nada aqui. Oferta imperdível hoje."
    s = lint(texto, dados)
    o = next(x for x in s["ocorrencias"] if x["categoria"] == "urgencia_vazia")
    checa("8 posicao", texto[o["posicao"]:o["posicao"] + len(o["termo"])] == o["termo"])

    # 9. Toda ocorrência carrega sugestão não vazia.
    s = lint("Saiba mais sobre o produto premium imperdível.", dados)
    checa("9 sugestao", all(o["sugestao"] for o in s["ocorrencias"]))

    if falhas:
        print("FALHAS: %s" % ", ".join(falhas))
        return 1
    print("todos os testes passaram")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Detecta clichês de copy em PB a partir de lista fechada.",
        epilog="Texto via stdin ou --arquivo. Exit: 0 limpo, 1 clichê encontrado, 2 erro.")
    ap.add_argument("--ajuda", action="help", help="mostra esta ajuda e sai")
    ap.add_argument("--arquivo", help="arquivo de texto de entrada (padrão: stdin)")
    ap.add_argument("--formato", choices=["json", "texto"], default="json",
                    help="formato da saída (padrão: json)")
    ap.add_argument("--ignorar", default="",
                    help="categorias a ignorar, separadas por vírgula")
    ap.add_argument("--cliches", default=CAMINHO_CLICHES,
                    help="caminho alternativo do cliches.json")
    ap.add_argument("--categorias", action="store_true",
                    help="lista as categorias disponíveis e sai")
    ap.add_argument("--testes", action="store_true", help="roda os casos de teste e sai")
    args = ap.parse_args(argv)

    if args.testes:
        return _testes()

    try:
        dados = carregar_cliches(args.cliches)
    except (OSError, ValueError) as e:
        print(json.dumps({"erro": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2

    if args.categorias:
        print("\n".join(_categorias(dados) + [CATEGORIA_TRINCA]))
        return 0

    ignorar = {c.strip() for c in args.ignorar.split(",") if c.strip()}
    desconhecidas = ignorar - set(_categorias(dados) + [CATEGORIA_TRINCA])
    if desconhecidas:
        print(json.dumps({"erro": "categoria desconhecida: %s" % ", ".join(sorted(desconhecidas))},
                         ensure_ascii=False), file=sys.stderr)
        return 2

    try:
        texto = open(args.arquivo, encoding="utf-8").read() if args.arquivo else sys.stdin.read()
    except OSError as e:
        print(json.dumps({"erro": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2

    saida = lint(texto, dados, ignorar)
    if args.formato == "texto":
        print(formatar_texto(saida))
    else:
        print(json.dumps(saida, ensure_ascii=False, indent=2))
    return 1 if saida["total"] else 0


if __name__ == "__main__":
    sys.exit(main())
