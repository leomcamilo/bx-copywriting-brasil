# Checklist editorial para copy em PB

Use antes de entregar. Cada item é uma falha comum que derruba conversão ou quebra confiança.

## 1. Evidência antes de promessa

- [ ] O benefício central está no briefing, card ou PDP?
- [ ] Preço, desconto ou condição foram confirmados na fonte?
- [ ] A copy promete algo que o produto entrega de fato?

Se `não` em qualquer um: **re-escreva a promessa** ou peça a fonte que falta.

## 2. Tom de voz definido

A voz da marca é decidida uma vez por cliente, em [`assets/brand-voice-intake.md`](../assets/brand-voice-intake.md) — atributos, pares "como dizer / como não dizer", palavras banidas, tratamento e uso de emoji. **Se o cliente tem esse documento preenchido, ele manda; esta seção não se aplica.**

Quando o cliente ainda não tem voz definida, escolha um destes três arquétipos como ponto de partida provisório e declare a escolha na entrega:

| Arquétipo | Quando usar | Exemplo de CTA |
|-----|-------------|----------------|
| **Direto/editorial** | Moda, alto ticket, B2B, decisão considerada | "Ver detalhes", "Conhecer a coleção" |
| **Amigável/informal** | Comunidade, reengajamento, redes sociais | "Aproveitar agora", "Quero esse" |
| **Técnico/preciso** | Software, serviço, spec comparável | "Testar grátis", "Comparar planos" |

Regra prática, válida em qualquer arquétipo: se a marca fala "você" na página de produto, a copy não fala "tu" no e-mail.

## 3. Gatilhos mentais — uso legítimo

Os gatilhos abaixo são documentados como funcionais (Cialdini, adaptados no corpus brasileiro). O erro é usá-los como adjetivo em vez de estrutura.

| Gatilho | Como usar com verdade | Como NÃO usar |
|---------|---------------------|-------------|
| **Escassez** | "Últimas unidades", "até amanhã" — com data/estoque real | "Oferta imperdível" sem prazo nem limite |
| **Prova social** | "12 mil clientes", "4.8/5 em 842 avaliações" — com número verificável | "Todo mundo ama" sem dado |
| **Autoridade** | "Recomendado por [especialista real]" com nome e origem | "Especialistas indicam" sem quem |
| **Reciprocidade** | "Baixe o guia grátis" com valor real no material | "Presente para você" que é só cupom de 5% |
| **Compromisso/coerência** | "Você já começou; falta só escolher o tamanho" | "A gente sabe que você quer" sem base |

## 4. Clichês que derrubam copy em PB

**O princípio:** o clichê é o termo que não especifica nada. Se trocá-lo por outro do mesmo campo semântico não muda o que o leitor entende, ele é enchimento — e enchimento ocupa o espaço que a informação deveria ocupar.

Substitua por **material + modelo + uso real**:

- Funciona: "Oxford de algodão com elastano, estrutura para manter o caimento ao longo do dia."
- Não funciona: "Camisa versátil para todos os momentos."

**A lista fechada de clichês não vive aqui.** Ela vive em [`scripts/cliches.json`](../scripts/cliches.json) e é aplicada por [`scripts/lint_cliches.py`](../scripts/lint_cliches.py), que também detecta a trinca genérica (três adjetivos vazios encadeados, como "moderno, elegante e sofisticado"). Rode o script — julgamento humano ou de modelo é inconsistente entre execuções; lista fechada não é.

```bash
python3 scripts/lint_cliches.py --arquivo copy.txt --formato texto
```

Quando a marca usa legitimamente um termo da lista (uma marca de cosmético pode ter direito a "sofisticado" se isso está no `brand-voice-intake.md`), use `--ignorar categoria` e registre a exceção na entrega.

## 5. Estrutura de frase e ritmo

- [ ] Frases de até 25 palavras em digital
- [ ] Um benefício por parágrafo; uma ação por CTA
- [ ] Verbo no imperativo ou infinitivo no CTA ("Compre", "Aproveite"), não no futuro ("você poderá comprar")

## 6. Revisão técnica (não-especialista lendo em voz alta)

- [ ] A copy faz sentido sem contexto visual?
- [ ] Alguém fora da área entende o que está sendo vendido?
- [ ] Lendo em voz alta, a frase trava ou flui?

Se travar, corte a subordinada ou divida em duas frases.

## 7. Conformidade de canal

**Contagem de caractere não é item de checklist humano.** Rode [`scripts/validar_limites.py`](../scripts/validar_limites.py) com os limites de [`scripts/limites_canais.json`](../scripts/limites_canais.json) e cole o resultado na entrega:

```bash
echo '{"canal":"push","campos":{"titulo":"...","corpo":"..."}}' \
  | python3 scripts/validar_limites.py --formato texto
```

O que continua sendo julgamento, e por isso fica aqui:

- [ ] E-mail: o preheader complementa o assunto em vez de repeti-lo?
- [ ] Meta: o botão de CTA é o mais forte disponível para a ação real?
- [ ] PDP: o CTA da página está presente e a copy reforça a decisão?
- [ ] RSA: os títulos fazem sentido em qualquer combinação, sem depender de ordem?
- [ ] Landing page: a primeira dobra repete a promessa do anúncio que trouxe o visitante?

## 8. Detecção de copy genérica de IA

A skill roda dentro de um agente, e o leitor de 2026 reconhece o padrão. Estes são os sinais, e cada um tem correção mecânica:

- [ ] **Estrutura repetida entre variações.** Se A e B têm o mesmo número de frases, o mesmo ritmo e o mesmo ponto de virada, elas são a mesma copy. Reescreva B a partir de outro eixo de ângulo (ver `frameworks.md`, seção E).
- [ ] **Adjetivo empilhado.** Dois ou três qualificadores antes do substantivo ("uma solução completa, moderna e intuitiva"). Corte para zero e deixe o substantivo trabalhar.
- [ ] **Transição formulaica.** "Além disso", "Não só isso", "Em um mundo cada vez mais", "Seja você um X ou um Y". Corte a transição inteira; o parágrafo quase sempre começa melhor na frase seguinte.
- [ ] **Simetria excessiva.** Três bullets do mesmo comprimento, todos começando com verbo no infinitivo. Texto humano é irregular.
- [ ] **Ausência de detalhe específico do produto.** Se a copy funcionaria trocando o nome do produto pelo de um concorrente, ela não é sobre o produto. Volte ao briefing e traga um número, um material, um prazo ou um nome próprio.
- [ ] **Fecho auto-referente.** "Em resumo", "No fim das contas", "A escolha é sua". Copy termina em CTA, não em conclusão de redação.

O teste rápido: leia só a primeira frase de cada variação. Se elas poderiam ser embaralhadas sem prejuízo, o problema não é de palavra — é de ângulo.

## 9. Última verificação: o "e daí?" test

Leia a copy como quem recebe. Se você responder "e daí?" ou "e o que eu faço agora?", a copy ainda não está pronta. O passo seguinte precisa ser óbvio, específico e possível.
