# Contrato de saída — template de entregável

Toda entrega da skill segue este formato, na mesma ordem de blocos. Inconsistência de formato é a primeira coisa que o cliente nota, e o formato fixo é o que torna a entrega comparável entre campanhas.

Regras do contrato:

- A contagem de caracteres vem de `scripts/validar_limites.py`, **nunca** de estimativa do modelo.
- Todo item do diagnóstico que foi inferido, e não veio do briefing, é marcado como inferido.
- Toda variação declara o **eixo de ângulo** que ocupa. Duas variações no mesmo eixo contam como uma.
- O bloco de conformidade tem exatamente três estados possíveis.

---

## Template

```markdown
## Entregável — [canal] · [campanha/fluxo]

**Diagnóstico**
Estágio de consciência: [ ] · Sofisticação do mercado: [1-5] · Ideia central: [uma frase]
[Se algum item foi inferido e não veio do briefing: "inferido a partir de canal + momento da jornada"]

**Hipótese**
Se [mudança específica], então [métrica primária] varia, porque [razão ligada ao diagnóstico].
Métrica primária: [ ] · Guardrail: [métrica que não pode piorar] · Falsificação: [o que provaria que a hipótese está errada]

---

### Variação A — [nome do ângulo]
[copy]

`Limites: [campo] XX/YY ✅ · [campo] XX/YY ✅`
**Racional:** [por que este ângulo, ligado ao diagnóstico — 1 a 2 frases]

### Variação B — [ângulo diferente, não sinônimo]
[copy]

`Limites: ...`
**Racional:** ...

---

**Conformidade:** [aprovado | pendente: claim X precisa de fonte Y | bloqueado: motivo]
**Fontes usadas:** [briefing, PDP, review #, ficha técnica, pesquisa VoC]
**Próximo passo sugerido:** [o que testar depois, se esta hipótese se confirmar]
```

---

## Exemplo preenchido

```markdown
## Entregável — push · carrinho abandonado (1h)

**Diagnóstico**
Estágio de consciência: mais consciente (inferido a partir de canal + momento da jornada — o briefing não declarou) · Sofisticação do mercado: 3 · Ideia central: o pedido está a um toque de terminar.

**Hipótese**
Se o push remover o atrito declarado em vez de reapresentar o produto, então a taxa de recuperação de carrinho varia, porque o leitor mais consciente já decidiu e foi interrompido — reapresentar produto é atrito, não argumento.
Métrica primária: taxa de recuperação de carrinho · Guardrail: taxa de desativação de push · Falsificação: se a variação com reapresentação de produto empatar ou vencer, o público não está no estágio inferido.

---

### Variação A — remoção de atrito
**Título:** Seu carrinho está guardado
**Corpo:** Frete e forma de pagamento já estão preenchidos. Falta só confirmar.

`Limites: titulo 26/50 ✅ · corpo 62/120 ✅`
**Racional:** leitor mais consciente foi interrompido, não convencido do contrário. A copy elimina os dois passos que ele ainda teria pela frente.

### Variação B — objeção antecipada (frete)
**Título:** Frete grátis acima de R$ 199
**Corpo:** Seu carrinho está em R$ 214. Confirme antes que o preço mude.

`Limites: titulo 30/50 ✅ · corpo 63/120 ✅`
**Racional:** eixo diferente do A — endereça a objeção mais frequente de abandono nesta base em vez de simplificar o caminho. Testa causa (frete) contra atrito (passos).

---

**Conformidade:** pendente — "antes que o preço mude" só entra se houver data ou regra de reajuste real; sem isso é escassez vazia. Alternativa conforme já aplicável: "Confirme e garanta o frete grátis."
**Fontes usadas:** briefing (política de frete grátis acima de R$ 199), export de carrinhos abandonados (valor médio), `references/ciclo-de-vida-crm.md`.
**Próximo passo sugerido:** se B vencer, o gargalo é frete — testar exibição do frete grátis na página de produto, antes do carrinho.
```

---

## Os três estados de conformidade

| Estado | Quando | O que a entrega faz |
|---|---|---|
| **Aprovado** | Todo claim tem fonte, nenhum item do checklist falhou | Entrega normal |
| **Pendente** | Um claim depende de informação que o cliente tem, mas não forneceu | Entrega com o claim marcado, nomeando **qual fonte** falta, e com a formulação alternativa que já é utilizável |
| **Bloqueado** | O claim viola regra de setor regulado ou é enganoso por natureza | Não escreve o claim. Explica a regra, cita o dispositivo e oferece a formulação conforme |

Ver `references/compliance-br.md` para o checklist que produz esses estados.
