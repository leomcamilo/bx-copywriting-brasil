# Pesquisa VoC — a linguagem do próprio cliente

A skill exige fonte para toda promessa. Este arquivo ensina a **obter** essa fonte quando ela não veio no briefing, em vez de apenas recusar.

Voice of Customer (VoC) é extrair as palavras literais que o comprador usa sobre o problema, a objeção e o resultado. É a diferença entre "escrevi um texto" e "usei a linguagem dos seus próprios compradores".

---

## A. Onde buscar

| Fonte | O que extrair | Limitação |
|---|---|---|
| **Reviews da própria PDP** | Palavras literais de benefício e de objeção resolvida | Viés de quem já comprou — não mostra quem desistiu |
| **Reviews de concorrente direto** | Objeção não resolvida, expectativa frustrada, promessa que não se cumpriu | Não é exatamente o seu público |
| **Tickets de suporte / SAC** | Dúvida recorrente pré-compra, ponto de confusão | Viés de quem teve problema |
| **Conversas de WhatsApp comercial** | Objeção real no momento da decisão, com as palavras da negociação | Requer base legal e anonimização (LGPD) |
| **Comentários em anúncio** | Reação a um ângulo específico — validação barata de ângulo | Ruído alto; muito comentário fora de contexto |
| **Pesquisa com cliente novo** | Gatilho de compra e alternativa considerada — o que é impossível inferir | Custo e tempo |
| **Busca interna do site** | Vocabulário real de produto e demanda não atendida | Só quem já navega; não alcança público frio |
| **Grupos, fóruns e comunidades do nicho** | Como o problema é nomeado fora do contexto de venda | Não representa quem compra, só quem discute |

Ordem prática de esforço: reviews próprios → reviews de concorrente → tickets → busca interna → pesquisa ativa.

---

## B. O que procurar

Quatro categorias. Extraia **literalmente**; parafrasear destrói o ativo.

1. **Vocabulário** — como o cliente nomeia o produto e o problema. Costuma ser diferente do vocabulário interno da empresa. A empresa diz "revestimento antiaderente de alta durabilidade"; o cliente diz "não descasca".
2. **Objeção** — o que impede a compra, ordenado por frequência. É o que vira bloco de prova, FAQ ou headline de objeção invertida.
3. **Gatilho** — o que aconteceu na vida do cliente logo antes da compra. Define segmentação e momento de envio, não só texto.
4. **Resultado percebido** — o benefício que o cliente cita espontaneamente. Frequentemente não é o que o marketing destaca, e essa divergência é o achado mais valioso da pesquisa.

**Regra operacional: prefira a palavra do cliente à palavra da marca.** Se o cliente escreve "não descasca" e a ficha técnica diz "revestimento antiaderente de alta durabilidade", a headline usa "não descasca" e a ficha técnica vira prova logo abaixo.

---

## C. Protocolo de mineração

Executável quando o cliente entrega um arquivo de reviews, tickets ou exportação de conversas.

1. **Amostragem.** Mínimo 50 itens. Priorize avaliações de 2 e 3 estrelas: 5 estrelas elogia sem informação ("amei, chegou rápido") e 1 estrela costuma ser logística, não produto. As objeções úteis estão no meio.
2. **Extração.** Liste verbatim, uma linha por trecho. Não corrija gramática, não parafraseie, não junte dois trechos parecidos.
3. **Agrupamento.** Classifique cada trecho em vocabulário, objeção, gatilho ou resultado percebido. Um trecho pode cair em duas categorias.
4. **Frequência.** Ordene por recorrência dentro de cada categoria. Registre a contagem, não o "muito citado".
5. **Saída.** Uma tabela: trecho literal · categoria · frequência · uso sugerido na copy.

Formato da saída:

| Trecho literal | Categoria | Freq. | Uso sugerido |
|---|---|---|---|
| "achei que ia descascar tipo as outras e não descascou" | resultado percebido | 14/50 | Headline |
| "não sabia se servia em fogão de indução" | objeção | 9/50 | FAQ + bullet de PDP |
| "comprei porque a antiga soltou o cabo" | gatilho | 7/50 | Segmentação de remarketing |

---

## D. Exemplo completo: do review à headline

**Review bruto (3 estrelas, e-commerce de utilidades domésticas):**

> "Comprei meio desconfiada porque já tive duas dessas que descascaram em três meses. Essa aqui tá com sete meses e continua lisa. Só tirei uma estrela porque não achei em lugar nenhum a informação se podia usar em indução, tive que perguntar no chat."

**Extração:**

| Trecho | Categoria |
|---|---|
| "já tive duas dessas que descascaram em três meses" | objeção (ceticismo por experiência anterior) |
| "tá com sete meses e continua lisa" | resultado percebido |
| "não achei em lugar nenhum a informação se podia usar em indução" | objeção (informação ausente) |

**Diagnóstico que sai daí:** mercado sofisticado (nível 3 a 4 — o cliente já testou a categoria e desconfia da promessa), leitor consciente da solução. A copy precisa de mecanismo, não de promessa.

**Headline resultante:**

> "Sete meses de uso e ainda lisa — porque o revestimento é aplicado em três camadas, não em uma."

**Bloco de prova logo abaixo:** o dado da ficha técnica que sustenta as três camadas.
**Bullet de PDP obrigatório:** compatibilidade com indução, em posição visível — a objeção mais frequente é uma informação ausente, não uma dúvida sobre qualidade.

Repare que a headline não inventou nada: "sete meses e continua lisa" veio do cliente, "três camadas" veio da ficha técnica. A copy só juntou resultado percebido com mecanismo.

---

## E. LGPD na pesquisa

Reviews, tickets e conversas de WhatsApp são dados de clientes reais. Antes de qualquer trecho entrar em material, apresentação ou prompt de agente:

- **Base legal.** O uso de dado pessoal para pesquisa de comunicação precisa de base legal — normalmente consentimento ou legítimo interesse, e a escolha muda o que se pode fazer com o dado.
- **Anonimização.** Remova nome, telefone, e-mail, número de pedido, CPF e qualquer identificador direto antes de copiar o trecho para fora do sistema de origem. O texto do trecho basta; a identidade não acrescenta nada à copy.
- **Minimização.** Extraia só o trecho relevante, não a conversa inteira.
- **Depoimento é caso à parte.** Usar um trecho identificado como depoimento público exige autorização expressa do titular — e o depoimento precisa refletir resultado típico, não excepcional.

Detalhes e os artigos aplicáveis em `references/compliance-br.md`.
