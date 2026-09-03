# Briefing de copy — template

A skill exige briefing antes de escrever. Este arquivo define o que conta como briefing **suficiente**.

Campos marcados como **obrigatório** precisam estar preenchidos ou explicitamente inferidos. Se um obrigatório está vazio e não é inferível, a skill para e pergunta — ver a seção "Se faltar", no final.

---

## Campos obrigatórios

**Objetivo da peça** — *obrigatório*
O que precisa acontecer depois que a pessoa lê. Uma ação, não uma intenção. ("Recuperar carrinho abandonado", não "aumentar as vendas".)

**Público** — *obrigatório*
Quem é e, principalmente, **o que já sabe** sobre o problema e sobre o produto. Base ativa? Público frio? Já comprou antes?

**Canal e formato** — *obrigatório*
Push, e-mail, RSA, PDP, Reels, LinkedIn. Com o formato específico dentro do canal (assunto? corpo? título de anúncio?).

**Momento da jornada** — *obrigatório*
Em que ponto essa pessoa está: primeiro contato, carrinho abandonado, pós-compra, base fria. Ver `references/ciclo-de-vida-crm.md`.

**Promessa central** — *obrigatório*
O que o produto entrega, em uma frase. O que o leitor ganha.

**Fonte da promessa** — *obrigatório*
**Onde está escrito** que o produto entrega isso. Ficha técnica, PDP, estudo, dado interno, contrato, laudo, página do fabricante. Um link, um nome de arquivo ou uma citação — não "o cliente falou por telefone".
Sem este campo, a skill não escreve a promessa. Quem anuncia carrega o ônus de provar o que afirma (ver `references/compliance-br.md`).

**Oferta e condições** — *obrigatório quando há oferta*
Valor, desconto, prazo, condição de uso, exceções, estoque. Se a peça menciona preço ou vantagem, os números vêm daqui.

**CTA desejado** — *obrigatório*
A ação e para onde ela leva. Se houver mais de uma ação possível, qual é a primária.

**Restrições** — *obrigatório*
Limite de caracteres específico do cliente (se diferente do padrão do canal), palavras proibidas, tom, obrigatoriedade legal de aviso, elementos que precisam aparecer.

---

## Campos opcionais

**Concorrentes diretos** — as três promessas mais usadas por eles. Alimenta o diagnóstico de sofisticação de mercado.
**Peças anteriores e resultado** — o que já rodou e como performou. Evita repetir um ângulo que já falhou.
**Prazo** — data de veiculação; define se dá para pedir pesquisa ou fonte que falta.
**Ativos disponíveis** — imagem, vídeo, depoimento, laudo, número de prova. Determina qual framework é viável (sem prova, não use 4 Ps).
**Pesquisa VoC disponível** — reviews, tickets, conversas. Ver `references/pesquisa-voc.md`.
**Histórico de conformidade** — claims que o jurídico do cliente já vetou antes.

---

## Se faltar

Para cada campo obrigatório ausente: o que fazer, e se é inferível.

| Campo ausente | Inferível? | O que fazer |
|---|---|---|
| **Objetivo** | Não | Pergunte: "qual ação essa peça precisa gerar?" Sem isso não há métrica nem framework. |
| **Público** | Parcialmente | Infira o nível de conhecimento a partir do canal + momento e **declare a inferência**. Dados demográficos, não invente. |
| **Canal e formato** | Não | Pergunte. Canal define limite, estrutura e CTA — inferir errado invalida a peça inteira. |
| **Momento da jornada** | Sim | Infira pelo canal e pelo gatilho declarado, usando `references/ciclo-de-vida-crm.md`. Declare. |
| **Promessa central** | Não | Pergunte. Se o cliente não sabe dizer o que o produto entrega, a copy não vai descobrir. |
| **Fonte da promessa** | **Nunca** | Pare. Nomeie qual claim está descoberto e peça a fonte específica. Ofereça escrever a peça sem aquele claim, se ainda fizer sentido. |
| **Oferta e condições** | Não | Pergunte os números. Nunca escreva percentual, preço ou prazo que não veio da fonte. |
| **CTA** | Sim | Infira a ação mais forte disponível no canal e declare. Confirme na entrega. |
| **Restrições** | Sim | Use os padrões do canal (`scripts/limites_canais.json`) e declare que foram usados os padrões. |

Regra geral: **infira o que é contexto, pergunte o que é fato.** Estágio de consciência é contexto — pode ser inferido com declaração. Preço, percentual, prazo e claim de resultado são fatos — nunca são inferidos.
