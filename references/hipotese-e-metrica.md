# Hipótese e métrica

Copy sem métrica primária declarada não é avaliável: ela pode ter funcionado ou não, e ninguém saberá. Este passo transforma cada entrega em aprendizado acumulável — que é o que faz o cliente renovar contrato, e o que evita repetir um ângulo que já falhou há seis meses.

---

## 1. Formato da hipótese

```
Se [mudança específica], então [métrica primária] varia,
porque [mecanismo ligado ao diagnóstico].
```

**Boa:**
> Se o push de carrinho abandonado remover o atrito do checkout em vez de reapresentar o produto, então a taxa de recuperação de carrinho sobe, porque o leitor mais consciente já decidiu e foi interrompido — reapresentar o produto é atrito, não argumento.

**Ruim:**
> Se a copy for mais persuasiva, então as vendas aumentam, porque a copy é melhor.

O que a segunda erra: "mais persuasiva" não é uma mudança específica (não dá para fazer o oposto), "vendas" não é a métrica que essa peça move, e o "porque" não explica mecanismo nenhum. Uma hipótese que não pode estar errada não é hipótese.

---

## 2. Métrica primária por canal

Cada canal tem uma métrica que a copy de fato move. Atribuir à copy uma métrica que ela não controla é o erro mais comum de mensuração.

| Canal | Métrica primária | O que a copy move de fato |
|---|---|---|
| **Push** | Taxa de abertura + conversão pós-abertura | O título move a abertura; o corpo move o que acontece depois |
| **E-mail** | Assunto → taxa de abertura; corpo → taxa de clique | Testar corpo olhando abertura é erro de atribuição |
| **SMS / WhatsApp** | Taxa de clique ou de resposta | Sem abertura mensurável; a métrica é a ação |
| **Anúncio (Meta, RSA, PMax)** | CTR para o criativo; CPA para a campanha | Copy move CTR; CPA depende também de oferta e página |
| **PDP** | Taxa de adição ao carrinho | Conversão final depende do checkout, não da descrição |
| **Landing page** | Taxa de conversão da página | Com rejeição como guardrail obrigatório |
| **Banner / hero** | CTR do bloco | Isolado do resto da página |
| **Vídeo curto** | Retenção nos primeiros 3 segundos, depois CTR | O gancho e o resto são medidos separadamente |
| **LinkedIn / B2B** | Taxa de clique; para InMail, taxa de resposta | Volume baixo — ver seção 5 |
| **In-app** | Taxa de conclusão da ação | Com taxa de dispensa como guardrail |
| **Transacional** | Taxa de contato ao suporte sobre aquele assunto | Métrica de redução, não de conversão |
| **Carta de vendas** | Taxa de conversão da página + tempo até a rolagem de saída | Onde o leitor para indica qual bloco falhou |

---

## 3. Guardrail

Toda métrica primária vem acompanhada de uma métrica que **não pode piorar**. Sem guardrail, otimização vira dano.

Exemplo concreto: um push com título sensacionalista ("Você não vai acreditar no que aconteceu com seu pedido") pode subir a taxa de abertura em dois dígitos — e, na mesma semana, derrubar a conversão pós-abertura, subir a taxa de desativação de notificações e aumentar a desinstalação do app. A métrica primária melhorou; o canal ficou pior.

| Métrica primária | Guardrail típico |
|---|---|
| Taxa de abertura de push | Conversão pós-abertura, desativação de push |
| Taxa de abertura de e-mail | Taxa de descadastro, marcação de spam |
| CTR de anúncio | CPA, taxa de rejeição da página de destino |
| Taxa de adição ao carrinho | Taxa de conversão do checkout, taxa de devolução |
| Conversão de landing page | Qualidade do lead, taxa de show em reunião agendada |
| Taxa de recuperação de carrinho | Margem (se houver desconto no fluxo) |

Regra: se você não consegue nomear o dano que a otimização poderia causar, você ainda não entendeu o que está otimizando.

---

## 4. Uma variável por vez

Se a variação muda headline, imagem e CTA ao mesmo tempo, o resultado não é atribuível — você aprende que "B ganhou", não *por que* ganhou, e não consegue reaproveitar o aprendizado na próxima campanha.

Exceção legítima: teste de **conceito**, em que duas abordagens inteiras competem de propósito. Nesse caso, declare que é teste de conceito, não de elemento — e saiba que o resultado responde "qual direção seguir", não "qual palavra usar".

---

## 5. Poder do teste

Volume baixo não detecta diferença pequena. Um teste com 400 envios não distingue 2,0% de 2,3% de conversão — a diferença observada é indistinguível de ruído, e declarar vencedor ali produz aprendizado falso, que é pior que nenhum.

**Regra prática: quanto menor o volume, maior precisa ser a diferença testada.**

| Volume do canal | O que faz sentido testar |
|---|---|
| Alto (dezenas de milhares por envio) | Ajuste fino: uma palavra na headline, ordem dos blocos, texto do botão |
| Médio (milhares) | Ângulos distintos dentro da mesma estrutura |
| Baixo (centenas) | Só diferenças grandes de ângulo ou de oferta. Ajuste de palavra é indetectável |
| Muito baixo (dezenas — B2B de ticket alto) | Não teste A/B. Aprenda por conversa e resposta qualitativa |

Como decidir se vale testar, sem prometer número universal: pergunte qual é a menor diferença que **mudaria sua decisão**. Se uma diferença de 0,2 ponto percentual não mudaria nada na sua operação, não desenhe um teste para detectá-la. Se você precisa de um número exato de amostra, calcule com a taxa base real do canal e o efeito mínimo relevante — não com uma regra de bolso.

---

## 6. Falsificação

O que precisaria acontecer para a hipótese estar errada? Se não dá para responder, a hipótese é vaga demais e precisa ser reescrita antes da peça ir ao ar.

- Hipótese: "o leitor de carrinho abandonado está no estágio mais consciente, logo copy curta sem reapresentação vence."
- Falsificação: "se a variação que reapresenta o produto empatar ou vencer, o público não está no estágio inferido — e todo o resto do fluxo precisa ser revisto, não só esta peça."

Escrever a falsificação junto com a hipótese tem um efeito colateral útil: ela obriga a declarar o que o resultado significaria para o **diagnóstico**, não só para a peça.

---

## 7. Registro de aprendizado

Formato curto, acumulado por cliente, fora deste repositório. É o ativo que se forma ao longo dos meses e que nenhum concorrente consegue copiar.

```
[data] · [canal] · [fluxo]
Hipótese: ...
Resultado: [métrica primária: de X para Y] · [guardrail: estável / piorou]
Conclusão: [o que isso diz sobre o público, não sobre a peça]
Aplicável a: [quais outros fluxos herdam este aprendizado]
```

Exemplo:

```
2026-09-03 · push · carrinho abandonado
Hipótese: remover atrito vence reapresentar produto, porque o leitor é mais consciente.
Resultado: recuperação de 4,1% → 5,3% · desativação de push estável.
Conclusão: o público de carrinho está mesmo no estágio mais consciente; interrupção, não dúvida.
Aplicável a: recuperação de checkout, reposição, lembrete de teste expirando.
```

Repare que a conclusão fala do **público**, não da frase. Aprendizado sobre a frase morre com a campanha; aprendizado sobre o público sobrevive a ela.

### Consultar antes de perguntar

O registro só vira ativo se for lido. Antes de pedir resultado de peças anteriores ou de propor um ângulo, procure no registro do cliente:

1. **Aprendizado do mesmo fluxo ou canal.** Se existe, use a conclusão como premissa do diagnóstico e não pergunte de novo como a última peça performou.
2. **Aprendizado de fluxo que herda** (o campo "Aplicável a"). Ele vale como hipótese de partida, declarada como herdada.
3. **Ângulo que já falhou.** Não repita sem motivo novo; se repetir, diga por que agora seria diferente.

Na entrega, cite o que usou: "Partindo do aprendizado de 2026-09-03 (carrinho abandonado: interrupção, não dúvida), testo remoção de atrito contra objeção de frete." Se o registro não existe ou não cobre o caso, aí sim pergunte pelas peças anteriores, como no briefing.
