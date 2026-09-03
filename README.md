# bx-copywriting-brasil

Skill de agente para **copywriting em português brasileiro** — diagnóstico estratégico, escrita, conformidade legal e validação determinística de copy para marketing digital: CRM, anúncios, PDP, landing page, vídeo curto e carta de vendas.

Roda em agentes compatíveis com o formato de *skills* em Markdown (Claude Code, OpenCode e similares): um `SKILL.md` que roteia, referências carregadas sob demanda e scripts que fazem o que modelo de linguagem faz mal.

---

## A arquitetura, e por que ela é assim

A maior parte das skills de copywriting é uma lista de fórmulas. Esta é organizada em torno de cinco decisões, e cada uma delas resolve um modo de falha específico.

### Por que diagnóstico vem antes de briefing

O erro mais caro em copy não é escrever mal — é escrever bem a mensagem errada. Uma peça impecável para um leitor que ainda não sabe que tem o problema não converte, e nenhum ajuste posterior de tom, canal ou CTA recupera isso.

Por isso o passo 0 é determinar estágio de consciência, sofisticação de mercado e ideia central (Schwartz, *Breakthrough Advertising*, 1966) — **antes** de coletar briefing. O briefing informa o que o cliente sabe; o diagnóstico decide o que fazer com isso. Quando o briefing não permite inferir o estágio, a skill usa canal + momento da jornada como proxy e **declara a inferência na entrega**, para que ela possa ser contestada.

### Por que contagem de caractere é script, e não instrução

Modelo de linguagem não conta caractere com confiabilidade. Ele estima, acerta na maior parte das vezes, e a minoria em que erra é exatamente onde dói: um push truncado no meio do benefício, um título de RSA rejeitado pela plataforma.

Tarefa determinística vai para código. `scripts/validar_limites.py` conta sempre igual; `scripts/lint_cliches.py` aplica uma lista fechada em vez de julgamento que varia entre execuções. Os dados vivem em JSON (`limites_canais.json`, `cliches.json`), separados da lógica — quando a Meta muda um limite, o conserto é uma linha de dado, não uma reescrita de prosa espalhada por três arquivos.

Corolário disso: **cada dado tem um dono único**. Limites só existem em `limites_canais.json`; clichês só existem em `cliches.json`. O `checklist-editorial.md` ensina o princípio e aponta para o script, sem repetir a lista — porque duas cópias de um dado divergem no primeiro dia em que alguém atualiza uma delas.

### Por que é uma skill só, e não um conjunto

Skills competem por gatilho. Se existissem `bx-copy-crm`, `bx-copy-ads` e `bx-copy-compliance` separadas, o agente chamaria uma quando o pedido precisava de três — e o resultado seria um push perfeitamente formatado com um claim que o cliente não pode provar.

O volume de conteúdo se resolve por *progressive disclosure*, não por fragmentação: o `SKILL.md` fica abaixo de 200 linhas e apenas roteia; as referências são carregadas sob demanda, uma por vez. Um gatilho, muitas referências.

### Por que existe uma camada de conformidade brasileira

Copy publicada vincula quem anuncia (CDC art. 30), e o ônus de provar o que ela afirma é de quem a patrocina (CDC art. 38). O guardrail "benefício precisa de fonte" não é preciosismo editorial: é a materialização do art. 38 dentro do fluxo de produção.

Nenhuma skill de copy em inglês carrega essa camada, porque ela é específica do regime brasileiro — CDC, CONAR, LGPD e as regras setoriais de saúde, financeiro, infoproduto, bebida e público infantil. Uma skill que escreve copy comercial no Brasil sem ela é utilizável para rascunho e inutilizável para cliente corporativo.

A camada tem três estados de saída — aprovado, pendente, bloqueado — e nunca dá parecer jurídico: ela sinaliza risco, cita o dispositivo e propõe a formulação conforme.

### Por que toda entrega carrega hipótese

Copy sem métrica primária declarada não é avaliável. Ela pode ter funcionado ou não, e a operação repete o mesmo ângulo por seis meses sem descobrir.

Cada entrega declara: métrica primária, guardrail que não pode piorar, e o que falsificaria a hipótese. O guardrail existe porque otimização sem contrapeso causa dano — um título sensacionalista sobe a abertura de push e derruba a conversão, a permissão de notificação e a retenção do app na mesma semana.

Da mesma regra vem outra: **variação é ângulo, não sinônimo.** Trocar "Aproveite" por "Aproveitar" consome volume de tráfego e não produz aprendizado. Cada variação entregue declara qual eixo de ângulo ocupa, e duas variações no mesmo eixo contam como uma.

---

## Fluxo

```
  0  Diagnóstico estratégico   estágio de consciência · sofisticação · ideia central
  │                            references/diagnostico-estrategico.md
  ▼
  1  Briefing e evidência      objetivo · público · canal · promessa · FONTE DA PROMESSA
  │                            assets/briefing-template.md          ── sem fonte, para aqui
  ▼
  2  Voz da marca              atributos · banidas · tratamento · emoji por canal
  │                            assets/brand-voice-intake.md
  ▼
  3  Estrutura persuasiva      PAS · AIDA · 4Ps · BAB · carta · SB7 · FAB
  │                            references/frameworks.md
  ▼
  4  Registro do canal         limites · estrutura · CTA · proibido
  │                            references/canais-e-formatos.md
  ▼
  5  Conformidade legal        CDC · CONAR · LGPD · setor regulado
  │                            references/compliance-br.md          ── bloqueado, para aqui
  ▼
  6  Hipótese e métrica        primária · guardrail · falsificação
  │                            references/hipotese-e-metrica.md
  ▼
  7  Validação determinística  contagem por script · clichê por lista fechada
  │                            scripts/validar_limites.py · scripts/lint_cliches.py
  ▼
  8  Entrega                   diagnóstico · hipótese · variações · conformidade · fontes
                               assets/entregavel-template.md
```

Os passos 0, 4, 7 e 8 nunca são pulados. Os demais têm condição de pulo declarada no `SKILL.md`.

---

## Estrutura

```
SKILL.md                              fluxo de 9 passos e roteamento (sempre carregado)
references/
  diagnostico-estrategico.md          estágios de consciência, sofisticação, mecanismo, ideia central
  frameworks.md                       tabela de seleção, 7 frameworks, headline, ângulos vs. sinônimos
  pesquisa-voc.md                     onde buscar linguagem de cliente e como minerá-la
  ciclo-de-vida-crm.md                14 fluxos com estágio, métrica e erro comum
  canais-e-formatos.md                estrutura, CTA e "proibido" por canal
  compliance-br.md                    CDC, CONAR, LGPD, setores regulados, três estados
  hipotese-e-metrica.md               formato de hipótese, métrica por canal, guardrail
  terminologia-pb.md                  como o mercado brasileiro fala do ofício
  checklist-editorial.md              evidência, gatilhos, ritmo, copy genérica de IA
assets/
  briefing-template.md                campos obrigatórios e o que perguntar quando faltam
  brand-voice-intake.md               voz da marca, preenchido uma vez por cliente
  entregavel-template.md              contrato de saída
scripts/
  limites_canais.json                 fonte única dos limites (13 canais)
  cliches.json                        fonte única dos clichês (7 categorias)
  validar_limites.py                  contagem determinística por canal e campo
  lint_cliches.py                     detecção de clichê e de trinca genérica
  requirements.txt                    vazio por decisão — só biblioteca padrão
evals/
  evals.json                          12 casos com asserções verificáveis
  README.md                           como rodar e como interpretar falha
```

---

## Instalação

**Claude Code**

```bash
git clone https://github.com/leomcamilo/bx-copywriting-brasil.git \
  ~/.claude/skills/bx-copywriting-brasil
```

**OpenCode**

```bash
git clone https://github.com/leomcamilo/bx-copywriting-brasil.git \
  ~/.config/opencode/skills/bx-copywriting-brasil
```

**Outros agentes** — copie a pasta para o diretório de skills do agente. O formato é apenas Markdown com frontmatter YAML (`name`, `description`) mais arquivos de apoio; qualquer agente que carregue skills em Markdown roda esta.

Os scripts precisam de Python 3 no PATH. Nenhuma dependência externa:

```bash
python3 scripts/validar_limites.py --testes
python3 scripts/lint_cliches.py --testes
```

---

## Uso

A skill dispara sozinha quando o pedido envolve copy em PB. Três exemplos do que esperar de volta:

**"Escreve um push de carrinho abandonado."**
Não recebe copy. Recebe o pedido dos campos de briefing que faltam, com a fonte da promessa nomeada explicitamente. É o comportamento correto — e é o caso 1 do conjunto de avaliação.

**"Briefing completo [...]. Quero 3 variações para anúncio Meta."**
Recebe diagnóstico (estágio, sofisticação, ideia central), hipótese com métrica e guardrail, três variações em **eixos de ângulo distintos**, contagem de caractere verificada por script, estado de conformidade, fontes usadas e o próximo teste sugerido.

**"Anúncio pro suplemento: emagreça 7 kg em 30 dias."**
Recebe uma recusa fundamentada — estado bloqueado, com a regra citada, o motivo em duas frases e uma formulação alternativa conforme, baseada em composição e indicação de uso.

---

## Adaptando para outro idioma ou mercado

A arquitetura é universal; a camada regulatória e linguística é brasileira. Ao forkar para outro mercado:

| Arquivo | Status | O que fazer |
|---|---|---|
| `references/diagnostico-estrategico.md` | **Universal** | Traduzir os exemplos, manter a estrutura |
| `references/frameworks.md` | **Universal** | Traduzir os exemplos, manter o produto fictício único |
| `references/hipotese-e-metrica.md` | **Universal** | Traduzir |
| `references/ciclo-de-vida-crm.md` | **Universal** | Traduzir |
| `references/pesquisa-voc.md` | **Quase universal** | A seção de LGPD vira a lei local (GDPR, CCPA, etc.) |
| `SKILL.md`, `assets/*` | **Universal** | Traduzir; a arquitetura do fluxo não muda |
| `references/compliance-br.md` | **Específico** | **Reescrever inteiro** para o regime local. Manter a forma: regra → consequência para a copy → checklist fechado → três estados |
| `references/terminologia-pb.md` | **Específico** | Substituir pelo corpus terminológico do idioma-alvo |
| `scripts/cliches.json` | **Específico** | Substituir a lista. As categorias (adjetivo vazio, fórmula fechada, urgência vazia, prova vazia) são universais; os termos não |
| `scripts/limites_canais.json` | **Quase universal** | Limites de plataforma são globais, mas revalide — alguns variam por região e por idioma |
| `evals/evals.json` | **Misto** | Casos 1, 2, 3, 6, 7, 9, 10 traduzem direto; 4, 5, 11, 12 precisam do claim ilegal equivalente no regime local |

Em uma frase: **troque `compliance-*.md`, `terminologia-*.md` e `cliches.json`; o resto traduz.**

---

## Base teórica

Conceitos são usados com atribuição e explicados com palavras próprias — nenhum trecho, tabela ou lista é reproduzido das obras protegidas.

**Estudos com corpus brasileiro**

- **Curti-Contessoto, B. & Rocha, J. M. P. (2023).** *Marketing Digital e os textos persuasivos: formações terminológicas relacionadas ao copywriting.* Revista Moara, n. 63 — terminologia do copywriting em corpus real da web brasileira: gênero, empréstimo, sintagmas terminológicos vs. qualificadores vazios.
- **Santos, S. S., Silva, M. & Aoki, V. C. G. (2022).** *Creative failure in advertising: influencing the creative process.* Revista de Psicología, 40(2) — processo criativo de redatores e diretores de arte em agências brasileiras.

**Conceitos de copywriting e marketing usados como referência**

- **Schwartz, E. (1966).** *Breakthrough Advertising* — estágios de consciência e sofisticação de mercado, que estruturam o passo 0.
- **Sugarman, J. (1998).** *The Adweek Copywriting Handbook* — mecânica de frase: a função de cada frase é fazer ler a próxima.
- **Cialdini, R. (1984).** *Influence* — gatilhos de persuasão, aplicados no checklist com a exigência de que sejam verdade.
- **Caples, J. (1932).** *Tested Advertising Methods* — teste como método e a primazia da headline.
- **Miller, D. (2017).** *Building a StoryBrand* — SB7 como framework de mensagem de marca.
- **Sharp, B. (2010).** *How Brands Grow* — disponibilidade mental, ativos distintivos e o limite da segmentação.
- **Binet, L. & Field, P. (2013).** *The Long and the Short of It*, IPA — a tensão entre ativação de vendas e construção de marca, e por que elas não compartilham métrica.

**Base normativa** — Lei 8.078/1990 (CDC), Lei 13.709/2018 (LGPD), Código Brasileiro de Autorregulamentação Publicitária (CONAR) e normas setoriais. Ver `references/compliance-br.md` para a tradução em regra de copy e para as marcações de verificação pendente.

---

## Limitações

- **Não é parecer jurídico.** A camada de conformidade sinaliza risco e propõe alternativa. A decisão é do cliente e do jurídico dele.
- **Não substitui revisão humana.** Ela reduz uma classe de erro (contagem, clichê, claim descoberto); não elimina julgamento editorial.
- **Limites de plataforma mudam.** `scripts/limites_canais.json` carrega a data da última atualização e valores conservadores onde não houve confirmação oficial. Revalide antes de campanha.
- **Normas mudam.** Itens marcados `[verificar norma vigente]` em `compliance-br.md` estão funcionalmente corretos mas com numeração a confirmar na fonte oficial.
- **Não faz pesquisa de mercado.** Ela ensina a minerar VoC de material que o cliente já tem; não coleta dado por conta própria.
- **O conjunto de avaliação é manual.** Não há runner automatizado — o que se avalia é comportamento de agente, não saída de função.

---

## Contribuição

Ao propor mudança, respeite as três regras que sustentam a arquitetura:

1. `SKILL.md` fica abaixo de 200 linhas e não ensina — roteia.
2. Cada dado tem um dono único. Limite novo vai para `limites_canais.json`; clichê novo vai para `cliches.json`; não duplique em prosa.
3. Conceito emprestado entra explicado com palavras próprias e com atribuição inline. Nunca reproduza trecho de obra protegida.

Mudança de comportamento (fases de diagnóstico e conformidade) merece PR separado das mudanças de conteúdo — o conjunto em `evals/` existe para revisar exatamente isso.

## Licença

MIT
