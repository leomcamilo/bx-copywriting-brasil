# Avaliação da skill

O conjunto em `evals.json` existe para provar que a skill se comporta como promete — especialmente nos casos em que o comportamento correto é **não escrever**. Recusar bem é mais difícil de acertar do que escrever bem, e é o que quebra primeiro quando a skill é editada.

Os 12 casos cobrem três classes de comportamento:

| Classe | Casos | O que quebra se falhar |
|---|---|---|
| **Guardrail de evidência** | 1, 12 | A skill volta a inventar promessa e o cliente assume um claim que não pode provar |
| **Conformidade** | 4, 5, 11 | A skill escreve claim ilegal e vira passivo para o cliente |
| **Qualidade e contrato** | 2, 3, 6, 7, 8, 9, 10 | A entrega perde formato, ângulo ou precisão de contagem |

Casos 1, 4 e 10 são obrigatórios: eles testam, respectivamente, o guardrail principal, o bloqueio em setor regulado e o contrato de saída. Se qualquer um dos três falha, a skill não deve ser publicada.

---

## Como rodar

Não há runner automatizado — a avaliação é manual, porque o que está sendo avaliado é o comportamento de um agente, não a saída de uma função.

1. Carregue a skill no agente, em sessão limpa (sem contexto de conversas anteriores, que contaminam o resultado).
2. Cole o `prompt` do caso, sozinho, sem instrução adicional.
3. Compare a resposta contra cada item de `assertions`, um por um.
4. Registre passou/falhou por asserção, não por caso — um caso que passa em 4 de 5 asserções informa mais do que um "falhou".

Asserções que mencionam contagem de caractere ou detecção de clichê são verificáveis por script, e devem ser conferidas por script:

```bash
# confere a contagem que a resposta declarou
echo '{"canal":"push","campos":{"titulo":"<título da resposta>"}}' \
  | python3 ../scripts/validar_limites.py --formato texto

# confere se a reescrita realmente saiu limpa
echo "<copy da resposta>" | python3 ../scripts/lint_cliches.py --formato texto
```

A validação estrutural do próprio conjunto:

```bash
python3 -c "import json; d=json.load(open('evals.json')); print(len(d['evals']), 'casos')"
```

---

## Como interpretar falha

| Sintoma | Provável causa | Onde corrigir |
|---|---|---|
| A skill escreveu copy sem briefing (caso 1) | O gatilho de parada não está forte o bastante no corpo do SKILL.md | `SKILL.md`, passos 1 e "Quando parar e pedir" |
| A skill entregou o claim bloqueado (casos 4, 5) | A skill não carregou `compliance-br.md` | Descrição da skill e passo 5 do fluxo |
| A skill declarou "pendente" onde deveria ser "bloqueado" | Os três estados não estão distinguíveis o suficiente | `references/compliance-br.md`, seção F |
| As variações são sinônimos (casos 2, 9) | A regra de ângulo não está sendo aplicada na geração | `references/frameworks.md`, seção E |
| A contagem de caractere está errada (casos 2, 7, 9) | A skill estimou em vez de rodar o script | `SKILL.md`, passo 7 — este é o erro que o script existe para eliminar |
| Faltam blocos na entrega (caso 10) | O contrato de saída não está sendo seguido | `assets/entregavel-template.md` |

Falha em asserção de **conteúdo** (a copy não usou a palavra do cliente) costuma ser problema de reference. Falha em asserção de **comportamento** (escreveu quando deveria parar) é quase sempre problema do `SKILL.md` — é lá que o comportamento é decidido.

---

## Registro de rodadas

Anote data, modelo e agente a cada rodada. Uma skill pode passar em um modelo e falhar em outro, e o modelo é parte do resultado.

| Data | Modelo | Agente | Casos passados | Observações |
|---|---|---|---|---|
| — | — | — | — | Nenhuma rodada registrada até aqui. O conjunto foi escrito junto com a skill; a primeira rodada precisa ser feita em sessão limpa para valer. |
