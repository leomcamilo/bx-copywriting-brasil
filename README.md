# bx-copywriting-brasil

**Skill de agente que escreve copy em português brasileiro — e recusa escrever quando não há evidência para a promessa.**

A maioria das skills de copywriting é uma máquina de gerar promessa inventada. Esta para e pede a fonte.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![SKILL.md](https://img.shields.io/badge/formato-SKILL.md-blue)
![Português brasileiro](https://img.shields.io/badge/idioma-pt--BR-yellow)
![Agentes](https://img.shields.io/badge/agentes-Claude%20Code%20%7C%20OpenCode%20%7C%20Codex-lightgrey)

---

## Em 30 segundos

**Entrada:**

```
revisa essa copy de PDP: "Colchão de qualidade, moderno e versátil,
pensado nos mínimos detalhes para o seu descanso."
```

**Saída:**

```
Cinco achados, por lista fechada (scripts/lint_cliches.py):

  [adjetivo_vazio]   "de qualidade"
  [trinca_generica]  "de qualidade, moderno e versátil"
  [adjetivo_vazio]   "moderno"
  [adjetivo_vazio]   "versátil"
  [filler_editorial] "pensado nos mínimos detalhes"

Três adjetivos vazios encadeados têm categoria própria porque são o
padrão mais comum de copy genérica em PB. Nenhum dos três diz o que o
produto é.

Além disso: não há densidade, altura, tipo de núcleo nem perfil de quem
vai dormir nele — o padrão de evidência que a PDP exige. Nada aqui passa
no teste do "e daí?".

Não reescrevo ainda. PDP não carrega promessa de performance sem teste,
e eu não tenho a ficha do produto.

Me manda a composição do núcleo, densidade, altura e o perfil de uso.
A reescrita sai no padrão material + modelo + uso real.

Conformidade: pendente — falta a ficha técnica.
```

Essa é a diferença: a skill não te devolve uma versão mais bonita do vazio. Ela nomeia o que falta.

---

## Por que ela existe

Copy gerada por agente tem quatro falhas recorrentes:

| Falha | O que esta skill faz |
|---|---|
| Inventa benefício que o produto não tem | Exige fonte antes de escrever. Sem briefing, não escreve. |
| Escreve em "português de tradução" | Terminologia de mercado em PB, baseada em estudo de corpus real. |
| Estoura limite de caractere do canal | Contagem por script, não por estimativa do modelo. Limites versionados em JSON. |
| Escreve claim que o cliente não pode provar | Camada de conformidade brasileira: CDC, CONAR, LGPD e setores regulados. |

---

## Instalação

**Claude Code / OpenCode**

```bash
git clone https://github.com/leomcamilo/bx-copywriting-brasil.git \
  ~/.config/opencode/skills/bx-copywriting-brasil
```

Para o Claude Code, use o diretório de skills do seu projeto ou o global (`~/.claude/skills/`).

**Outros agentes com formato SKILL.md:** copie a pasta para o diretório de skills do seu agente. Não há dependência externa, nem build, nem instalação de pacote. Os dois validadores precisam apenas de Python 3 no PATH — só biblioteca padrão:

```bash
python3 scripts/validar_limites.py --testes
python3 scripts/lint_cliches.py --testes
```

A skill dispara sozinha quando o pedido envolve copy em PB. Não precisa invocar por nome.

---

## Como usar

```
escreve um push de carrinho abandonado pra loja de calçados
revisa essa headline: "A solução definitiva para seu negócio"
cria 3 variações de CTA pro checkout
adapta essa copy de e-mail pra WhatsApp
```

Se o briefing estiver incompleto, a skill pede o que falta antes de escrever. Isso é comportamento pretendido, não bug.

---

## O que tem dentro

```
SKILL.md                          # fluxo de 9 passos e roteamento (sempre carregado)
references/
  diagnostico-estrategico.md      # estágio de consciência, sofisticação, ideia central
  frameworks.md                   # tabela de seleção, PAS/AIDA/4Ps/BAB/SB7/FAB, headline
  pesquisa-voc.md                 # linguagem do cliente: onde buscar e como minerar
  ciclo-de-vida-crm.md            # 14 fluxos com estágio, métrica e erro comum
  canais-e-formatos.md            # limites, estrutura e CTA por canal
  paginas-completas.md            # homepage, preços, funcionalidade: objeções e prova
  edicao-e-voz-recebida.md        # edição pontual, reescrita e a voz do texto recebido
  compliance-br.md                # CDC, CONAR, LGPD, setores regulados
  hipotese-e-metrica.md           # métrica primária, guardrail, falsificação
  terminologia-pb.md              # como o mercado brasileiro realmente fala
  checklist-editorial.md          # evidência, tom, gatilhos, copy genérica de IA
assets/
  briefing-template.md            # campos obrigatórios e o que perguntar quando faltam
  brand-voice-intake.md           # voz da marca, preenchido uma vez por cliente
  entregavel-template.md          # contrato de saída
scripts/
  validar_limites.py              # contagem determinística por canal e campo
  lint_cliches.py                 # detecção de clichê e de trinca genérica
  limites_canais.json             # fonte única dos limites
  cliches.json                    # fonte única dos clichês
  requirements.txt                # vazio por decisão — só biblioteca padrão
evals/
  evals.json                      # 16 casos com asserções verificáveis
  README.md                       # como rodar e como interpretar falha
```

Arquitetura de *progressive disclosure*: o `SKILL.md` é curto e roteia; as referências carregam só quando o caso exige. Isso mantém o custo de contexto baixo mesmo com a base de conhecimento crescendo.

O que é determinístico não fica em prosa. Contagem de caractere e detecção de clichê são script, porque modelo de linguagem erra contagem e varia entre execuções. Os dados moram em JSON e têm dono único: limite só em `limites_canais.json`, clichê só em `cliches.json`.

### Cobertura por canal

Push · E-mail (assunto, preheader, corpo) · SMS · WhatsApp · PDP · Banner e hero · Anúncio Meta · Google Ads RSA · Google Ads Performance Max · Landing page (above the fold) · Carta de vendas longa · Roteiro de vídeo curto (Reels, Shorts, TikTok) · LinkedIn e B2B · Notificação in-app · E-mail transacional vs. promocional

### Princípios que a skill não negocia

- **Evidência antes de promessa.** Benefício sem fonte no briefing não vira copy.
- **Clichê não é estilo, é ausência de informação.** "Versátil" sem função é vazio.
- **Gatilho mental precisa ser verdadeiro.** Escassez com prazo real, prova social com número verificável.
- **O canal define o registro.** Push não é e-mail encurtado.
- **Variação é ângulo, não sinônimo.** Duas opções que dizem a mesma coisa não são um teste.

---

## Base teórica

**Estudos com corpus brasileiro**

- **Curti-Contessoto, B. & Rocha, J. M. P. (2023).** *Marketing Digital e os textos persuasivos: formações terminológicas relacionadas ao copywriting.* Revista Moara, n. 63. Estudo de terminologia com corpus real da web brasileira.
- **Santos, S. S., Silva, M. & Aoki, V. C. G. (2022).** *Creative failure in advertising: influencing the creative process.* Revista de Psicología, 40(2). Processo criativo em agências brasileiras.

**Conceitos usados com atribuição** — explicados com palavras próprias, sem reprodução de trecho:

Schwartz (*Breakthrough Advertising*, 1966), estágios de consciência e sofisticação de mercado · Sugarman (*The Adweek Copywriting Handbook*, 1998), mecânica de frase · Cialdini (*Influence*, 1984), gatilhos de persuasão · Caples (*Tested Advertising Methods*, 1932), teste como método · Miller (*Building a StoryBrand*, 2017), SB7 · Sharp (*How Brands Grow*, 2010) e Binet & Field (*The Long and the Short of It*, IPA, 2013), ativação vs. construção de marca.

**Base normativa** — Lei 8.078/1990 (CDC), Lei 13.709/2018 (LGPD) e o Código Brasileiro de Autorregulamentação Publicitária. Traduzidos em regra de copy em `references/compliance-br.md`.

Além disso: padrão editorial consolidado de operação real de CRM e e-commerce brasileiro, descontextualizado de marca.

---

## Adaptando para outro mercado

Se você quer a mesma arquitetura em outro idioma, estes são os arquivos que trocam e os que ficam:

| Arquivo | Específico de PB? |
|---|---|
| `SKILL.md` (fluxo) | Não — a arquitetura é universal |
| `diagnostico-estrategico.md`, `frameworks.md`, `hipotese-e-metrica.md`, `ciclo-de-vida-crm.md` | Não — traduzir os exemplos, manter a estrutura |
| `assets/` (briefing, voz, entregável) | Não — traduzir |
| `pesquisa-voc.md` | Quase — só a seção de LGPD vira a lei local |
| `canais-e-formatos.md` e `limites_canais.json` | Parcialmente — limites são globais, exemplos são locais |
| `checklist-editorial.md` | Parcialmente — princípios são universais |
| `cliches.json` | Sim — as categorias são universais, os termos não |
| `terminologia-pb.md` | Sim — reescrever inteiro para o idioma de destino |
| `compliance-br.md` | Sim — reescrever inteiro para o regime local |

Em uma frase: troque `compliance-br.md`, `terminologia-pb.md` e `cliches.json`; o resto traduz.

Fork é bem-vindo. Se você adaptar para outro idioma, abra uma issue com o link — vale referenciar aqui.

---

## Limitações

- Não substitui revisão humana antes de publicar.
- Não dá parecer jurídico. Sinaliza risco; a decisão é do time e do jurídico do cliente.
- Limites de caractere de plataforma mudam sem aviso. Revalide na documentação oficial antes de campanha grande.
- Escrita e revisão em português brasileiro. Não faz tradução nem copy em outros idiomas.
- O conjunto em `evals/` ainda não teve rodada registrada. Foi escrito junto com a skill, o que é o pior cenário para avaliação.

---

## Contribuindo

Issues e PRs são bem-vindos, especialmente:

- clichês de mercado que faltam na lista;
- limites de canal desatualizados;
- exemplos reais de copy em PB que a skill trata mal.

Se for reportar um caso ruim, cole o prompt e a saída. É o tipo de issue mais útil aqui.

---

## Licença

MIT — ver [LICENSE](LICENSE).
