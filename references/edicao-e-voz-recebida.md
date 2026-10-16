# Edição, reescrita e a voz do texto recebido

Quando o cliente entrega um texto pronto, ele entrega também decisões: o argumento escolhido, as palavras que o público usa, o tratamento, o registro. Muitas dessas decisões já passaram por aprovação ou já performaram. Trocar o texto por uma versão "melhor" no gosto do modelo apaga essas decisões, gera retrabalho e faz o cliente desconfiar da próxima entrega.

Este arquivo define o que muda e o que fica em cada modo de pedido. A classificação do modo está no `SKILL.md`.

---

## A. Os três modos, pelo pedido

| Pedido | Modo | O que volta |
|---|---|---|
| "Escreve um push de boas-vindas" | Criação | Entregável completo, com variações |
| "Melhora esse e-mail, tá fraco" | Reescrita | Texto inteiro revisado, com o motivo de cada alteração |
| "Reescreve a PDP com a ficha nova" | Reescrita | Texto inteiro, preservando o que a ficha não muda |
| "Muda só a headline" | Edição pontual | A headline nova, e o resto idêntico |
| "Troca o CTA por algo mais direto" | Edição pontual | O CTA novo e a contagem |
| "Corrige essa frase: '...'" | Edição pontual | A frase corrigida |
| "Dá uma olhada nesse texto" | Ambíguo | Trate como revisão: aponte os achados e pergunte se é para reescrever |

Na dúvida entre reescrita e edição pontual, fique com a edição pontual. É mais fácil oferecer mais do que desfazer o que ninguém pediu.

---

## B. Escopo da edição pontual

1. **O alvo é o que foi nomeado:** uma frase, um campo, um CTA. Tudo fora dele volta caractere por caractere, inclusive pontuação, quebra de linha e emoji.
2. **Ajuste colateral mínimo.** Se a troca no alvo quebra algo fora dele (concordância, um termo que a frase seguinte retoma), faça o menor ajuste possível e declare: "ajustei também 'ela' na frase seguinte, que retomava 'a coleção'".
3. **Fora do escopo, aponte sem mexer.** Claim sem fonte, limite de canal estourado e clichê em outro trecho entram numa linha de observação, não na edição.
4. **Conformidade não fica calada.** Um claim bloqueado fora do trecho (`references/compliance-br.md`) precisa ser apontado, mesmo que o pedido seja trocar uma vírgula. A skill não corrige sozinha; ela avisa.
5. **Sem extras.** Edição pontual não ganha variações, diagnóstico, hipótese nem relatório. Se fizer sentido, ofereça em uma linha: "Se quiser, testo um segundo ângulo para essa headline."

---

## C. O que preservar na reescrita

Antes de reescrever, descreva a voz do texto recebido em uma linha, com estes cinco sinais:

| Sinal | O que olhar | Exemplo de registro |
|---|---|---|
| Tratamento | você, tu, a gente, nominal | "você", 2ª pessoa direta |
| Registro | coloquial, neutro, técnico, editorial | coloquial, com "pra" e "tá" |
| Ritmo | frases curtas ou longas, fragmentos | frases curtas, fragmentos no fim |
| Marcas próprias | gírias, bordões, emoji, pontuação | "bora", reticências, um emoji por bloco |
| Vocabulário do público | palavras que vieram do cliente (VoC) | "não descasca", "serve em indução" |

Depois, preserve:

- **O argumento central e a ordem lógica**, quando funcionam. Reescrita não é trocar de ângulo; trocar de ângulo é criação.
- **O vocabulário do cliente.** Palavra que veio de review, ticket ou conversa vale mais que sinônimo elegante (`references/pesquisa-voc.md`).
- **Tratamento, registro e marcas próprias.** Texto coloquial continua coloquial. Formalizar um texto coloquial sem pedido é uma alteração e precisa de motivo.
- **Trechos que já performaram ou foram aprovados.** Se o cliente diz que a abertura "funcionou na última campanha", ela fica.
- **Números e fontes, sempre.** Nunca altere preço, percentual, prazo ou dado. Se parecer errado, pergunte.

---

## D. Motivo por alteração

Toda alteração em reescrita ou edição pontual leva um motivo da lista abaixo. Alteração sem motivo da lista volta ao original.

| Motivo | Exemplo |
|---|---|
| Clichê detectado | `lint_cliches.py` apontou "atemporal" |
| Limite do canal | título com 34 de 30 caracteres, por `validar_limites.py` |
| Claim sem fonte ou conformidade | "o mais vendido" sem dado de venda |
| Ambiguidade concreta | "leve" pode ser peso ou tecido; o leitor não sabe qual |
| Estágio de consciência | a peça abre na oferta para um público que ainda não conhece o problema |
| CTA fraco | "Saiba mais" onde a ação real é "Ver o lote" |
| Pedido explícito | o cliente pediu mais curto, mais direto, sem emoji |

"Soa melhor", "fica mais fluido" e "mais profissional" não são motivos.

Formato na entrega:

```markdown
| Antes | Depois | Motivo |
|---|---|---|
| "Camisa versátil para todos os momentos" | "Camisa de Oxford 140 g, do escritório ao fim de semana" | Clichê ("versátil", "todos os momentos") trocado por dado da ficha |
```

---

## E. Quando a voz recebida e a da marca divergem

- **Há `brand-voice-intake` e o texto recebido foge dele:** aponte a diferença com um exemplo e pergunte qual vale. Em edição pontual, siga o texto recebido no trecho e registre a divergência numa linha.
- **Não há `brand-voice-intake`:** a voz do texto recebido é a melhor evidência da voz da marca. Ela vence o arquétipo de tom do `checklist-editorial.md`.

---

## F. Exemplos

**Edição pontual.** Pedido: "Muda só o título da PDP, o resto tá aprovado."

```
Texto recebido:
  Título: Conforto e sofisticação para o seu dia a dia
  Frase de uso: Algodão Pima, 160 g/m², costura reforçada nos ombros. Lava a 30 °C.

Entrega:
  Título: Algodão Pima que aguenta o dia inteiro
  Motivo: "Conforto e sofisticação" é fórmula fechada (lint_cliches.py); o título novo usa o material da ficha.
  Contagem: titulo 38/70 (validar_limites.py, canal pdp).
  A frase de uso não foi alterada.
```

**Reescrita com registro coloquial.** Pedido: "Melhora esse push, mas mantém o jeitão da marca."

```
Recebido: "Bora garantir o seu? Tá acabando o estoque da cor terracota 🔥"
Voz: "você" implícito, coloquial ("bora", "tá"), um emoji no fim.

Reescrita: "Bora garantir o seu? A terracota tem 12 peças no estoque 🔥"
Motivo: "tá acabando" é escassez sem número; a reescrita usa o estoque real informado no briefing.
Preservado: "Bora garantir o seu?", o registro coloquial e o emoji.
```
