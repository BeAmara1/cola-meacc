# Conceitos fundamentais (a teoria que sustenta tudo)

Esses conceitos não aparecem como "código", mas **aparecem como pergunta na prova** — a questão 2 da lista de revisão, por exemplo, pergunta literalmente "quem eram, originalmente, as observações (unidades de análise) que geraram esses dados percentuais?". Sem esse vocabulário, não tem como responder.

---

## 1. Unidade de análise (ou unidade de observação)

**É "quem" ou "o que" cada linha da sua base representa.**

Parece bobo, mas é a pergunta que mais confunde, porque muitas bases chegam **já agregadas** — e aí a unidade de análise da tabela não é a mesma de quem gerou o dado.

Exemplos:
- Base com uma linha por estado brasileiro → unidade de análise = **o estado**
- Base do ENEM com uma linha por inscrito → unidade de análise = **o participante**
- Tabela com "% de calouros que pretendem cada área de estudo" → a tabela tem uma linha por **área**, mas **quem gerou o dado foi cada estudante**. Os estudantes são as observações originais; a tabela é um resumo (distribuição de frequência) delas.

> **Pegadinha clássica:** quando a pergunta diz "originalmente", ela quer a unidade que *gerou* o dado (o estudante, a pessoa entrevistada), não a linha da tabela resumida (a área de estudo).

## 2. População vs. amostra

- **População**: todo o conjunto que você quer descrever (ex: todos os participantes do ENEM 2023).
- **Amostra**: o subconjunto que você de fato observou (ex: a amostra de 1% dos participantes usada na prova de 2025).
- **Censo**: quando você observa a população inteira (por isso "Censo Demográfico" — o IBGE tenta alcançar todo mundo).

**Por que importa na resposta:** se o dado é amostra, suas conclusões valem *para a amostra* e só se generalizam para a população se a amostra for representativa. Escreva isso — é o tipo de ressalva que ganha ponto.

> **Frase-modelo:** "Como se trata de uma amostra de 1% dos participantes, os padrões observados descrevem essa amostra; a generalização para todos os participantes depende de a amostragem ser representativa."

## 3. Representatividade e viés

Uma amostra é **representativa** quando reproduz as características relevantes da população. Ela deixa de ser quando o jeito de selecionar favorece certos grupos (**viés de seleção**).

Sinais de problema que valem mencionar numa resposta:
- **Não resposta**: muitos casos em branco/"não informado" numa variável (aconteceu com `TP_ESCOLA` na prova de 2025 — a maioria não respondeu, o que enfraquece qualquer conclusão sobre aquela variável)
- **Autosseleção**: só quem quis participar respondeu
- **Cobertura**: quem não tem acesso ao meio da pesquisa fica de fora

> **Frase-modelo:** "Vale ressaltar o alto percentual de não resposta nessa variável, o que limita a força de qualquer conclusão tirada a partir dela."

## 4. Distribuição de frequência

É o retrato de **como os valores de uma variável se repartem**: quais valores aparecem e com que frequência.

- **Frequência absoluta**: a contagem (quantas observações em cada categoria/classe)
- **Frequência relativa**: o percentual (contagem ÷ total × 100)

Quando comparar dois grupos de **tamanhos diferentes**, sempre use frequência **relativa** — senão o grupo maior parece "ter mais de tudo" só por ser maior. É exatamente por isso que o gráfico de barras segmentadas com `stack="normalize"` (percentual) é melhor que o de contagem absoluta pra comparar.

## 5. Variável explicativa vs. variável resposta

- **Variável resposta** (ou dependente): o que você quer explicar/prever
- **Variável explicativa** (ou independente): o que você acha que ajuda a explicar

**Convenção de gráfico:** a explicativa vai no **eixo x**, a resposta no **eixo y**. Se a questão fala "faça um diagrama de dispersão de A (variável resposta) contra B (variável explicativa)", então B vai no x e A vai no y.

Isso também decide **qual distribuição condicional** calcular numa tabela de dupla entrada: você condiciona na **explicativa** (ou seja, dentro de cada categoria da explicativa, veja como se distribui a resposta).

## 6. Estatística descritiva (que é tudo que essa matéria faz)

O que você faz nessa matéria é **descrever** dados: resumir, visualizar, comparar. Você **não** está fazendo inferência (testar hipótese, calcular p-valor, intervalo de confiança). Por isso:

- Nunca escreva "a diferença é estatisticamente significativa" — isso é inferência, não foi visto e não se sustenta com o que você calculou.
- Escreva "os dados sugerem", "há indícios de", "observa-se uma diferença de X pontos" — linguagem descritiva.

## 7. Resistência (robustez) de uma medida

Uma medida é **resistente** quando valores extremos não a mudam muito.

| Medida | Resistente? |
|---|---|
| Média | ❌ não — um único valor extremo puxa bastante |
| Mediana | ✅ sim |
| Desvio padrão | ❌ não |
| Amplitude total (máx - mín) | ❌ não (é definida pelos extremos!) |
| Amplitude interquartil (AIQ) | ✅ sim |
| Correlação de Pearson | ❌ não |

**Consequência prática:** em distribuição assimétrica ou com atípico, relate **mediana + AIQ**. Em distribuição simétrica e sem atípico, **média + desvio padrão** descreve bem.

## 8. O vocabulário mínimo para descrever uma distribuição

Toda vez que você olhar uma variável quantitativa, responda essas 4 coisas (nessa ordem):

1. **Forma** — simétrica, assimétrica à direita, assimétrica à esquerda; unimodal ou plurimodal
2. **Centro** — mediana (ou média, se simétrica)
3. **Variabilidade/dispersão** — amplitude, AIQ, desvio padrão
4. **Valores atípicos** — tem? quais? (regra 1,5×AIQ)

Decorar essa sequência resolve metade das questões abertas da prova.

## 9. Assimetria — como lembrar para que lado é

A distribuição é assimétrica **para o lado da cauda** (o "rabo" comprido), não para o lado do monte de dados.

- **Assimétrica à direita**: pico à esquerda, cauda se estende à direita. Média **>** mediana. Típico de **renda** (muita gente ganhando pouco, poucos ganhando muito).
- **Assimétrica à esquerda**: pico à direita, cauda à esquerda. Média **<** mediana. Típico de **notas de prova fácil** (quase todo mundo tira nota alta, poucos tiram muito baixa).
