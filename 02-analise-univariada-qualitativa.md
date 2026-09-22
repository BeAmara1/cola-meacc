# Análise univariada — variável qualitativa

## Setup

```python
import pandas as pd
import altair as alt
```

## Tabela de frequência

```python
df['coluna'].value_counts()                      # contagem
df['coluna'].value_counts(normalize=True) * 100   # percentual
```

## Checar consistência de dados percentuais (devem somar 100%)

```python
df.Percent.sum()

# se faltar categoria (ex: "outras"), some a diferença:
df.loc[len(df)] = ['Outras', 100 - df.Percent.sum()]

# se for erro de arredondamento, corrija a maior/menor categoria:
df.loc[i, 'Percent'] = df.loc[i, 'Percent'] + (100 - df.Percent.sum())
```

## Gráfico de barras (padrão mais seguro — use quase sempre)

```python
# pandas simples
df.set_index('categoria').valor.plot.bar()

# Altair, ordenado do maior pro menor
alt.Chart(df).mark_bar().encode(
    x=alt.X('categoria:N', sort='-y', axis=alt.Axis(labelAngle=-45)),
    y='valor:Q',
    tooltip=['categoria', 'valor']
)

# barras horizontais (bom quando os nomes das categorias são longos)
alt.Chart(df).mark_bar().encode(
    x='valor:Q',
    y=alt.Y('categoria:N', sort='-x'),
    tooltip=['categoria', 'valor']
)
```

## Gráfico de setores (pizza) — só quando faz sentido

Só use quando: poucas categorias (até ~5-6) **e** os valores somam 100% (partes de um todo).
Se a questão pergunta "seria correto usar gráfico de setores?" e as categorias não somam 100% (ex: só os formatos mais populares, sem "outros"), a resposta é **não**.

```python
# pandas
df.set_index('categoria').valor.plot.pie()

# Altair
alt.Chart(df).mark_arc().encode(
    theta='valor:Q',
    color='categoria:N',
    tooltip=['categoria:N', 'valor:Q']
)
```

## Contagem direto de uma coluna (sem agregar antes)

```python
alt.Chart(df).mark_bar().encode(
    x=alt.X('categoria:N', sort='-y'),
    y='count()',
    tooltip=['categoria', 'count()']
)

alt.Chart(df).mark_arc().encode(
    theta='count()',
    color='categoria:N',
    tooltip=['categoria', 'count()']
)
```

## Interpretação (modelo)

> "Pelo gráfico de barras, que representa a distribuição de frequência da variável X, observamos que a maior parte das observações se concentra em [categoria], enquanto [categoria] tem participação bem menor/rara."
