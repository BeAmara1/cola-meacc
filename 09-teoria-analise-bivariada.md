# Teoria — Análise Bivariada (pra quando você precisa ESCREVER, não só rodar código)

Esse arquivo existe pra resolver um problema específico: rodar `df.corr()` ou fazer uma tabela de dupla entrada é fácil, mas **explicar o que aquilo significa** é a parte que trava na hora da prova. Aqui vai a teoria por trás de cada técnica, em ordem de "o que perguntar a mim mesmo" → "o que escrever".

---

## 1. O que é "análise bivariada" e por que ela existe

Análise univariada descreve **uma** variável por vez (forma, centro, dispersão). Análise bivariada pergunta: **será que essas duas variáveis se movem juntas de algum jeito?** Ou seja, ela busca **associação** (também chamada de relação ou correlação, no sentido amplo) entre duas variáveis.

Existem 3 combinações possíveis, e cada uma pede uma ferramenta diferente — **a primeira coisa a decidir é o tipo das duas variáveis**:

| Combinação | Ferramenta | Teoria por trás |
|---|---|---|
| Qualitativa × Qualitativa | Tabela de dupla entrada + distribuição condicional | Seção 2 |
| Quantitativa × Quantitativa | Diagrama de dispersão + correlação de Pearson | Seção 3 |
| Qualitativa × Quantitativa | Boxplots comparativos (um por categoria) | Seção 4 |

---

## 2. Duas variáveis qualitativas — tabela de dupla entrada

### A ideia central: distribuição condicional

Uma tabela de dupla entrada (contingência) mostra quantas observações caem em cada combinação de categorias. Mas **contagem bruta não serve pra comparar** grupos de tamanhos diferentes — por isso calculamos a **distribuição condicional**: "dado que a pessoa está no grupo A, qual % dela está em cada categoria de Y?"

**Existem duas distribuições condicionais possíveis** para o mesmo par de variáveis, e elas respondem perguntas diferentes:
- Condicional em X (`level=0`): "Entre quem é X=a, como se distribui Y?" → some 100% **dentro de cada linha/categoria de X**
- Condicional em Y (`level=1`): "Entre quem é Y=b, como se distribui X?" → some 100% **dentro de cada categoria de Y**

**Por que isso importa pra prova:** a pergunta geralmente aponta qual condicional usar. Ex: "a amostra sugere associação entre renda e uso de programa social?" → normalmente você quer ver, **dentro de cada faixa de renda**, o % que usa o programa (condicional na renda), porque a pergunta trata renda como a variável "explicativa".

### Como decidir se há associação

**Não há associação** (as variáveis são "independentes") quando a distribuição condicional de Y é **praticamente igual** em todas as categorias de X — ou seja, saber o valor de X não muda o que você espera de Y.

**Há associação** quando a distribuição condicional de Y **muda** de categoria para categoria de X.

> **Frase-modelo:** "Observando a distribuição condicional de [Y] em cada categoria de [X], vemos que ela [varia bastante / é praticamente igual] entre as categorias — o que [sugere / não sugere] associação entre as duas variáveis. Especificamente, [categoria de X] se destaca por ter [percentual]% em [categoria de Y], acima/abaixo da média geral."

### Cuidado: associação não é a mesma coisa em toda tabela

Se a tabela tiver muitas categorias, procure o **maior contraste** entre linhas/colunas — é isso que sustenta a resposta. Não basta dizer "parece que sim"; aponte o número.

---

## 3. Duas variáveis quantitativas — correlação de Pearson

### O que o coeficiente de Pearson (r) mede, exatamente

**r mede o grau de associação LINEAR entre duas variáveis quantitativas.** Ele varia de -1 a +1:

| Valor de r | Direção | Força (regra de bolso comum) |
|---|---|---|
| +0.7 a +1.0 | positiva | forte |
| +0.3 a +0.7 | positiva | moderada |
| 0 a +0.3 | positiva | fraca |
| 0 | — | nenhuma relação linear |
| 0 a -0.3 | negativa | fraca |
| -0.3 a -0.7 | negativa | moderada |
| -0.7 a -1.0 | negativa | forte |

- **Positiva**: quando uma variável aumenta, a outra tende a aumentar também (ex: renda e escolaridade).
- **Negativa**: quando uma aumenta, a outra tende a diminuir (ex: renda e taxa de analfabetismo).

### As 3 armadilhas mais cobradas em prova

**(1) Correlação não implica causalidade.** r alto entre X e Y não prova que X causa Y. Pode ser o contrário (Y causa X), pode ser coincidência, ou pode haver uma **variável de confusão** (confounder) — uma terceira variável que causa as duas ao mesmo tempo, criando uma relação aparente entre elas. Exemplo clássico: cidades com mais sorveterias têm mais afogamentos — a variável de confusão é a temperatura/verão, não uma causa a outra.

> **Frase-modelo:** "Apesar da forte correlação, isso não implica causalidade — pode haver uma variável de confusão explicando a relação entre [X] e [Y], como [sugestão de terceira variável]."

**(2) Pearson só enxerga relação LINEAR.** Duas variáveis podem ter uma relação clara e forte (ex: em forma de U, ou circular) e o coeficiente de Pearson dar próximo de zero, porque essa relação não é uma linha reta. **Sempre olhe o gráfico de dispersão, nunca confie só no número.** É exatamente o que o dataset "Datasaurus Dozen" (visto em aula) demonstra: vários formatos de nuvens de pontos completamente diferentes (incluindo um dinossauro!) podem ter o mesmíssimo r ≈ 0, e cada um conta uma história visual diferente.

> **Frase-modelo:** "O coeficiente de Pearson é próximo de zero, mas o diagrama de dispersão revela um padrão [não linear / em forma de X], o que mostra que ausência de correlação linear não significa ausência de relação entre as variáveis."

**(3) Sensibilidade a valores atípicos.** Como a fórmula de Pearson usa médias (que não são resistentes), **um único ponto atípico pode inflar ou atenuar bastante o valor de r**, especialmente em amostras pequenas (poucos países, poucos hospitais etc.). Por isso sempre vale recalcular removendo o suspeito de atípico e comparar.

> **Frase-modelo:** "Ao remover o valor atípico de [observação], o coeficiente de Pearson passa de [X] para [Y] — uma mudança [pequena/grande], o que mostra que a relação [é robusta / dependia bastante] desse ponto específico."

### Roteiro pra responder uma questão de correlação

1. Olhe o **diagrama de dispersão** primeiro — existe um padrão visual? É reto ou curvo?
2. Calcule **r** com `.corr()`.
3. Diga a **direção** (positiva/negativa) e a **força** (fraca/moderada/forte) usando a tabela acima.
4. Tem algum ponto **fora do padrão** no gráfico? Se sim, teste removendo e recalculando r.
5. **Nunca afirme causalidade** — no máximo, sugira uma explicação plausível e mencione que correlação não é causalidade.

---

## 4. Qualitativa × Quantitativa — comparando grupos com boxplot

Aqui a pergunta é: **a distribuição da variável quantitativa muda dependendo do grupo (categoria)?**

O boxplot comparativo (lado a lado) permite comparar, entre os grupos:
- **Centro** (a linha da mediana) — qual grupo tem valores tipicamente mais altos/baixos?
- **Dispersão** (tamanho da caixa = AIQ) — qual grupo é mais heterogêneo/variável?
- **Forma** (posição da mediana dentro da caixa e tamanho dos "bigodes") — simetria ou assimetria
- **Valores atípicos** (pontos fora dos bigodes) — algum grupo tem mais casos extremos?

> **Frase-modelo:** "Comparando os boxplots, o grupo [A] tem mediana [maior/menor] que o grupo [B] ([valor] vs [valor]), indicando que seus valores típicos são [maiores/menores]. Além disso, o grupo [A] apresenta [maior/menor] amplitude interquartil, mostrando [maior/menor] dispersão interna. [Só um dos grupos / ambos os grupos] apresentam valores atípicos pela regra 1,5×AIQ."

**Importante:** isso NÃO é a mesma coisa que correlação — aqui não faz sentido calcular Pearson (uma das variáveis não é numérica). O que se compara é a **distribuição condicional da quantitativa, dado o grupo**.

---

## 5. Estrutura geral pra escrever qualquer resposta de bivariada na prova

Isso serve de "esqueleto" pra qualquer questão de bivariada, independente da combinação de tipos:

1. **Diga o que você está comparando** — "Para avaliar a relação entre [X] e [Y], ..."
2. **Descreva o padrão observado** — direção, força, ou diferença entre grupos, com o número que sustenta isso (r, %, mediana, etc.)
3. **Aponte exceções/atípicos**, se houver, e o efeito deles na conclusão
4. **Conclua respondendo à pergunta feita** — não deixe a conclusão implícita, escreva a frase que responde exatamente o que foi perguntado
5. (Se pedido) **Contextualize** — o que esse resultado significa no mundo real, fora da estatística (ex: desigualdade racial, econômica, regional)

## 6. Erros comuns que derrubam nota

- Calcular Pearson entre uma variável qualitativa e uma quantitativa (não faz sentido — Pearson exige duas quantitativas)
- Dizer "há correlação" sem nunca escrever direção e força
- Afirmar causalidade ("X causa Y") a partir de correlação
- Não checar o gráfico e confiar só no coeficiente
- Esquecer de interpretar — deixar só o código e o gráfico "falando por si"
- Confundir qual distribuição condicional calcular (condicional em X vs em Y) — releia a pergunta pra ver qual variável é a "explicativa"
