# Banco de frases de interpretação

A professora sempre cobra interpretação por escrito — nunca deixe um gráfico ou número "solto". Adapte estas frases.

## Forma da distribuição

- "A distribuição é assimétrica à direita, com a maior parte das observações concentrada em valores mais baixos e uma cauda longa de poucos valores altos."
- "A distribuição é aproximadamente simétrica, com média e mediana próximas."
- "A distribuição é unimodal, com um único pico em torno de [valor]."
- "A distribuição é plurimodal, com picos em [valores], sugerindo subgrupos distintos na base."

## Média vs. mediana

- "A média ([valor]) é maior que a mediana ([valor]), o que reforça a assimetria à direita — a média não é resistente a valores atípicos, enquanto a mediana é."
- "Ao remover o valor atípico de [observação], a média cai de [X] para [Y], uma redução de [Z], enquanto a mediana praticamente não se altera, confirmando sua resistência a valores extremos."

## Valores atípicos

- "Pela regra 1,5×AIQ, o intervalo esperado é [limite inferior; limite superior]. O valor de [observação] ([valor]) está fora desse intervalo, sendo considerado um potencial valor atípico."
- "Apesar de ser o valor mais alto da distribuição, [observação] está dentro do intervalo [limite inferior; limite superior] e, portanto, não é considerado um valor atípico pela regra 1,5×AIQ — é apenas a maior observação."

## Dispersão

- "O desvio padrão de [valor] indica que as observações estão [pouco/muito] dispersas em torno da média."
- "A amplitude interquartil (AIQ) de [valor] mostra que os 50% centrais dos dados estão contidos em um intervalo relativamente [estreito/amplo], indicando [baixa/alta] variabilidade."

## Correlação de Pearson

- "O coeficiente de Pearson de [valor] indica uma relação linear [positiva/negativa] de intensidade [fraca (perto de 0) / moderada / forte (perto de ±1)] entre [var1] e [var2]."
- "Apesar do coeficiente de Pearson próximo de 0, o diagrama de dispersão revela um padrão não linear evidente — o coeficiente de Pearson só capta relações lineares."
- "Ao remover o valor atípico de [observação], o coeficiente passa de [X] para [Y], mostrando que esse ponto estava [atenuando/inflando] a força da relação linear."

## Tabela de dupla entrada / distribuição condicional

- "Olhando a distribuição condicional de [var2] em cada categoria de [var1], nota-se que [categoria] se destaca com [percentual]%, bem acima/abaixo das demais categorias."
- "A distribuição de [var2] muda consideravelmente entre as categorias de [var1], sugerindo associação entre as duas variáveis." / "A distribuição de [var2] é semelhante entre as categorias de [var1], sugerindo pouca ou nenhuma associação."

## Comparação entre grupos (boxplot lado a lado)

- "Ambos os grupos apresentam distribuições assimétricas à direita, mas o grupo [A] tem mediana maior ([valor] vs [valor]), indicando um valor típico mais alto."
- "O grupo [A] apresenta maior amplitude interquartil ([valor] vs [valor]), mostrando maior dispersão interna do que o grupo [B]."
- "Apenas o grupo [A] apresenta valor(es) atípico(s) pela regra 1,5×AIQ, evidenciando maior heterogeneidade nesse grupo."

## Série temporal

- "A série apresenta um comportamento cíclico claro, com picos entre [período] e vales entre [período], refletindo [sazonalidade/fator explicativo]."
- "Observa-se uma tendência de [alta/baixa] ao longo do período, com um desvio notável em [ano/período], quando [descrição do evento]."
- "A agregação mensal/anual (via `resample`) suaviza a variação de curto prazo e evidencia melhor a tendência de longo prazo."
