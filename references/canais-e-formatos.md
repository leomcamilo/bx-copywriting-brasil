# Canais e formatos de copy em PB

Cada canal tem limite físico, convenção e um CTA que funciona. Escrever igual para push e para e-mail é o erro mais comum.

> **Fonte de verdade dos limites numéricos: `scripts/limites_canais.json`.** Os números citados aqui são orientação de escrita; a validação da peça entregue é feita por `scripts/validar_limites.py`, nunca por contagem estimada. Plataformas mudam limites sem aviso — quando mudarem, atualize o JSON, não este arquivo.

## Push App / notificação push

- **Tamanho**: título ≈ 40–50 caracteres; corpo ≈ 100–120 caracteres. Trate como **faixa conservadora**, não como limite exato de plataforma: o ponto de truncamento difere entre iOS e Android, entre lockscreen e central de notificações, e muda com o tamanho de fonte que o usuário escolheu. Escreva de modo que a mensagem faça sentido mesmo cortada na metade do corpo.
- **Uso**: lembrete, urgência, promoção, reengajamento.
- **Estrutura**: Título com gancho + corpo com benefício + CTA implícito no toque.
- **Exemplos de CTA**: "Ver oferta", "Finalizar compra", "Compre agora". Evite "Clique aqui" quando a ação real é mais forte.
- **Proibido**: preço direto em push sem validação de oferta; emojis demais; caixa alta.

## E-mail marketing / newsletter

- **Assunto**: 40–60 caracteres (visível no mobile). Pergunta ou benefício direto.
- **Preheader**: complemento do assunto, não repetição. 70–90 caracteres.
- **Corpo**: parágrafos de 1–2 linhas; uma ideia por e-mail; botão de CTA com texto de ação.
- **Estrutura clássica**: Assunto → preheader → headline curta → 1 bloco de contexto → benefício em destaque → CTA.
- **Exemplos de CTA**: "Quero aproveitar", "Ver coleção", "Comprar com desconto" (desconto só se confirmado na fonte).

## SMS / WhatsApp

- **Tamanho**: SMS ≈ 160 caracteres; WhatsApp tolera mais, mas mensagem longa corta atenção.
- **Uso**: confirmação, urgência real, recuperação de carrinho, lembrete de agendamento.
- **Estrutura**: saudação opcional + informação essencial + CTA curto.
- **Exemplos de CTA**: "Responda SIM", "Acesse o link", "Chame no WhatsApp".
- **Proibido**: WhatsApp sem opt-in claro é bloqueio legal; SMS de vendas sem identificação da marca é spam.

## PDP (página de produto) / descrição de produto

- **Objetivo**: transformar dúvida em confiança de compra.
- **Estrutura**: título com o produto + 1 frase de uso real + bullet points de material/modelagem/cuidado + CTA "Adicionar à sacola".
- **Padrão de evidência**: material de onde vem, modelagem como veste, tecido/composição com sensação real, ocasião de uso.
- **Proibido**: adjetivo sem sustentação ("tecido nobre" sem composição); promessa de performance sem teste.

## Banner / hero / card promocional

- **Estrutura**: título curto (até 8 palavras) + subtítulo opcional + CTA.
- **CTA**: "Ver coleção", "Comprar agora", "Conhecer a linha".
- **Regra**: se o banner vende oferta, a oferta precisa estar lá e valer; se vende lançamento, o produto precisa estar disponível no clique.

## Anúncio Meta / Instagram / Facebook

- **Estrutura**: texto principal (corte do "ver mais" por volta de 125 caracteres) + título (~40, recomendado até 25 para não truncar em feed mobile) + descrição do link (~30) + CTA do botão. **Estes valores a plataforma altera sem aviso** — a fonte de verdade é `scripts/limites_canais.json`, que precisa ser atualizado quando a Meta mudar. Não afirme um limite de cabeça na entrega; rode o script.
- **Botões Meta**: "Comprar agora", "Saiba mais", "Cadastre-se", "Enviar mensagem", "Ver loja".
- **Regra legal**: preço em criativo Meta pode quebrar com catálogo dinâmico; valide se a estratégia permite antes de sugerir.
- **Copy de anúncio**: gancho na primeira linha, benefício ou prova social no meio, CTA explícito no fim.

## Carta de vendas / landing page longa

- **Uso**: produto com ticket alto ou decisão complexa.
- **Estrutura**: headline com promessa forte → dor do leitor → prova/escalada de benefícios → oferta → garantia → CTA.
- **Extensão**: sem teto fixo, mas cada parágrafo precisa empurrar para a próxima linha. Se o leitor pode parar no meio, a copy falhou.
- **Página inteira** (homepage, preços, funcionalidade, landing de campanha): mapa de objeções e prova ao longo da página em `references/paginas-completas.md`.

## Google Ads — RSA (Responsive Search Ads)

- **Estrutura**: até 15 títulos de 30 caracteres, até 4 descrições de 90 caracteres, mais os caminhos de exibição da URL. O sistema combina títulos e descrições em tempo de leilão.
- **Regra que muda tudo**: os títulos precisam funcionar **em qualquer ordem e em qualquer combinação**, porque você não controla qual par será exibido. Não escreva títulos que dependem de sequência ("Primeiro, entenda o problema" / "Agora veja a solução").
- **Cobertura recomendada**: não escreva 15 variações do mesmo ângulo. Distribua: 3–4 com a palavra-chave principal, 3–4 com benefício, 2–3 com prova ou número, 2 com CTA, 2 com objeção invertida.
- **Exemplos de CTA**: "Peça um orçamento", "Comece o teste grátis", "Fale com um especialista".
- **Proibido**: título que só faz sentido colado a outro; repetição de palavra-chave em todos os títulos (reduz a variedade de combinação); promessa que não está na landing page de destino.

## Google Ads — Performance Max / ativos

- **Estrutura**: títulos curtos (~30 caracteres), títulos longos (~90), descrições (curta ~60 e longas ~90), nome da empresa, além dos ativos visuais.
- **Requisito de variedade**: o formato exige um conjunto diverso de ativos porque o sistema monta a peça para superfícies muito diferentes (busca, YouTube, Gmail, Display). Ativos redundantes reduzem o alcance do que o sistema consegue montar.
- **Regra**: cada título longo precisa se sustentar sozinho como frase completa — ele pode aparecer sem nenhum outro texto ao lado.
- **Exemplos de CTA**: "Comece agora", "Peça uma demonstração", "Assine hoje", "Simule seu plano".
- **Proibido**: reaproveitar o mesmo texto entre título curto e longo; escrever para uma superfície só.

## Landing page — above the fold

- **Estrutura da primeira dobra**: headline (a promessa) + subheadline (o mecanismo ou a qualificação) + prova imediata (número, selo, logo de cliente) + CTA primário + elemento de confiança (garantia, segurança, política de troca).
- **Regra do message match**: quem chega de um anúncio precisa ver **a mesma promessa do anúncio** na primeira dobra, de preferência com as mesmas palavras. Se o anúncio prometeu "fechamento em 4 horas" e a página abre com "gestão financeira completa", a rejeição dispara — o visitante acha que clicou errado.
- **Um CTA primário.** Botões secundários competem com o principal e derrubam conversão.
- **Exemplos de CTA**: "Começar o teste grátis", "Quero minha simulação", "Agendar demonstração", "Criar minha conta". Prefira a primeira pessoa quando a ação é do usuário e o compromisso é baixo.
- **Proibido**: carrossel na primeira dobra; headline institucional em página de conversão; pedir dados antes de entregar qualquer valor.
- **O resto da página**: `references/paginas-completas.md`.

## Roteiro de vídeo curto (Reels / Shorts / TikTok)

- **Gancho**: os 2 primeiros segundos decidem tudo. O gancho é falado *e* visual — pressuponha som desligado e legenda ligada.
- **Estrutura de retenção**: gancho → contexto em uma frase → entrega do que o gancho prometeu → CTA. Sem apresentação de marca no começo; a marca aparece quando já há atenção.
- **CTA falado vs. CTA em tela**: o falado converte melhor para ação fora da plataforma; o em tela funciona para ação dentro dela. Escreva os dois, com textos diferentes — o falado é conversa, o em tela é comando curto.
- **Legenda é canal separado**: ela tem outra função (contexto, palavra-chave, primeira linha que aparece no feed), não é transcrição do áudio.
- **Proibido**: gancho que só faz sentido depois de 10 segundos; ler a legenda em voz alta; CTA antes de ter entregue algo.

## LinkedIn / B2B

- **Registro**: profissional, mas não corporativês. A diferença em relação a B2C é a **decisão em grupo** — quem lê raramente decide sozinho, então a copy precisa dar munição para a conversa interna dele (número, comparação, argumento de risco).
- **Post orgânico**: primeira linha antes do "ver mais" (~200 caracteres) carrega o gancho. Parágrafos de uma linha.
- **Anúncio**: texto introdutório curto (~150 caracteres antes do corte) + título (~70 no formato de imagem única).
- **InMail / mensagem**: personalização real ou não envie. Assunto curto, primeira linha sobre o destinatário, um pedido pequeno e específico — nunca "vamos marcar 30 minutos" na primeira mensagem.
- **Exemplos de CTA**: "Baixar o relatório", "Ver o estudo de caso", "Falar com um especialista", "Posso te mandar o número?" (em InMail, o CTA é uma pergunta respondível, não um agendamento).
- **Proibido**: humildade encenada ("fiquei emocionado ao compartilhar"); post que só faz sentido para quem já é cliente; CTA de compra em primeiro contato B2B de ticket alto.

## Notificação in-app e banner de app

- **Diferente de push**: o usuário já está no aplicativo, com contexto ativo e intenção. O atrito é menor e a tolerância a texto é maior — mas a interrupção é mais cara, porque corta uma ação em andamento.
- **Estrutura**: título curto + uma frase de valor + ação primária, com dispensa fácil e visível.
- **Regra**: dispare por comportamento, não por calendário. In-app disparada fora de contexto é a forma mais rápida de treinar o usuário a fechar sem ler.
- **Exemplos de CTA**: "Ativar agora", "Continuar de onde parei", "Ver meu resumo", "Agora não" (a dispensa também é copy, e uma dispensa clara preserva a próxima interrupção).
- **Proibido**: bloquear a tela sem saída óbvia; usar in-app para o que caberia num push; repetir a mesma notificação na mesma sessão.

## Assunto de e-mail: transacional vs. promocional

| | Transacional | Promocional |
|---|---|---|
| **Base legal e opt-in** | Decorre da relação de consumo | Exige opt-in de marketing |
| **Assunto** | Factual e previsível: "Pedido 48213 a caminho" | Gancho, benefício ou pergunta |
| **Expectativa** | O usuário abre para resolver algo | O usuário abre se valer a pena |
| **Oferta** | Não carrega | É o objetivo |

- **Regra**: transacional **não** carrega oferta escondida. Além de quebrar a confiança do canal mais aberto que a marca tem, misturar os dois expõe a operação a reclamação de spam e a problema de conformidade de opt-in.
- **Proibido**: assunto transacional falso em peça promocional ("Sobre o seu pedido" quando não há pedido). É engano, e engano em publicidade é vedado — ver `references/compliance-br.md`.
