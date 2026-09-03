# bx-copywriting-brasil

Skill de agente para **copywriting em português brasileiro** — escrita e revisão de copy persuasiva para marketing digital: CRM (push, e-mail, SMS, WhatsApp), PDP, banners, anúncios e cartas de vendas.

Pensada para rodar em agentes compatíveis com o formato de *skills* de instruções em Markdown (OpenCode, Claude Code e similares): um `SKILL.md` com o fluxo principal + referências carregadas sob demanda (*progressive disclosure*).

## O que a skill faz

- **Exige briefing antes de escrever** — copy sem objetivo, público, canal e promessa sustentada em fonte é invenção, e a skill para em vez de inventar.
- **Terminologia de mercado em PB** — como o mercado brasileiro realmente fala (`copy`, `copywriter`, `copywriting`), com gênero, flexões e a distinção entre tipos reais de copy (`copy de vendas`, `copywriter de resposta direta`) e adjetivos vazios que não especificam nada (`copy matadora`, `copy de sucesso`).
- **Canais e formatos** — limites e estrutura por canal: push (40–120 chars), e-mail (assunto + preheader + corpo), SMS/WhatsApp, PDP, banner/hero, anúncio Meta e carta de vendas longa.
- **Checklist editorial** — gatilhos mentais usados com verdade (escassez com prazo real, prova social com número verificável), clichês a evitar ("conforto e sofisticação", "versátil/atemporal" sem função), teste do "e daí?" antes de entregar.

## Estrutura

```
SKILL.md                            # fluxo principal (sempre carregado)
references/
  terminologia-pb.md                # corpus linguístico do copywriting no Brasil
  canais-e-formatos.md              # limites e CTA por canal
  checklist-editorial.md            # evidência, tom, gatilhos, clichês
```

## Base teórica

- **Curti-Contessoto, B. & Rocha, J. M. P. (2023).** *Marketing Digital e os textos persuasivos: formações terminológicas relacionadas ao copywriting.* Revista Moara, n. 63 — estudo de terminologia com corpus real da web brasileira (gênero, empréstimo, sintagmas).
- **Santos, S. S., Silva, M. & Aoki, V. C. G. (2022).** *Creative failure in advertising: influencing the creative process.* Revista de Psicología, 40(2) — processo criativo de redatores e diretores de arte em agências brasileiras (briefing, brainstorm, insight, bloqueios).
- Padrão editorial consolidado de operação real de CRM/e-commerce brasileiro (canal, validação, tom), descontextualizado de marca.

## Uso

Copie a pasta para o diretório de skills do seu agente (ex.: `~/.config/opencode/skills/bx-copywriting-brasil`). A skill dispara automaticamente quando o pedido envolve escrever/revisar copy em PB: "escreve um push de carrinho abandonado", "revisa essa headline", "cria variações de CTA".

## Licença

MIT
