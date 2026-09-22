# Histograma e séries temporais

## Setup

```python
import pandas as pd
import altair as alt
```

## Histograma básico

```python
alt.Chart(df).mark_bar().encode(
    alt.X('coluna:Q', bin=True),
    y='count()'
)

# controlando a largura das classes (bins)
alt.Chart(df).mark_bar().encode(
    alt.X('coluna:Q', bin=alt.Bin(step=5)),   # classes de largura 5
    y='count()'
)

# limitando o domínio do eixo (começar em 0, por ex.)
alt.Chart(df).mark_bar().encode(
    alt.X('coluna:Q', bin=alt.Bin(step=1, extent=[0, 100])),
    y='count()'
)

# histograma em percentual em vez de contagem (útil pra comparar bases de tamanhos diferentes)
alt.Chart(df).transform_joinaggregate(
    total='count(*)'
).transform_calculate(
    pct='1 / datum.total'
).mark_bar().encode(
    alt.X('coluna:Q', bin=alt.Bin(step=1)),
    alt.Y('sum(pct):Q', axis=alt.Axis(format='%'))
)
```

## Interpretação de histograma (os 4 pontos que a professora sempre pede)

1. **Forma** — simétrica / assimétrica à direita (cauda longa à direita, média > mediana) / assimétrica à esquerda / unimodal / plurimodal
2. **Centro** — mediana (ou média, se simétrica)
3. **Variabilidade** — amplitude (máx - mín) e/ou amplitude interquartil (AIQ)
4. **Valores atípicos** — algum ponto fora do padrão geral? (ver regra 1.5×AIQ em `04-medidas-descritivas.md`)

> Modelo: "A distribuição é assimétrica à direita, com um único pico em [faixa]. O centro (mediana) está em torno de [valor]. Os valores variam de [mín] a [máx], mostrando [pouca/grande] variabilidade. [Não há / há] valores atípicos aparentes."

## Séries temporais

```python
# garantir que a coluna de data é datetime
df['data'] = pd.to_datetime(df['data'])

# gráfico de linha
alt.Chart(df).mark_line().encode(
    x='data:T',
    y='valor:Q',
    tooltip=['data', 'valor']
)

# limitando o eixo y pra ver variação com mais destaque
alt.Chart(df).mark_line().encode(
    x='data:T',
    y=alt.Y('valor:Q', scale=alt.Scale(domain=[10, 40]))
)
```

## Agregação por período (resample) — média/soma por mês, ano etc.

> ⚠️ **ATENÇÃO — pegadinha de versão que trava a prova.** O gabarito de 2025 e as aulas usam `resample('M')`. Nas versões atuais do pandas isso mudou: mês virou `'ME'` e ano virou `'YE'`. Se você usar `'M'` e o Colab estiver no pandas 3, dá **erro**: `'M' is no longer supported for offsets. Please use 'ME' instead.` Se der esse erro, é só trocar a letra.

| Período | Escrita atual | Escrita antiga (pandas < 2.2) |
|---|---|---|
| dia | `'D'` | `'D'` |
| semana | `'W'` | `'W'` |
| mês | `'ME'` | `'M'` |
| trimestre | `'QE'` | `'Q'` |
| ano | `'YE'` | `'Y'` |

```python
df_idx = df.set_index('data')

# média mensal
serie_mensal = df_idx.resample('ME').valor.mean()   # se der erro, tente 'M'

alt.Chart(serie_mensal.reset_index()).mark_line().encode(
    x='data:T',
    y='valor:Q'
)
```

Versão à prova de versão (tenta o novo, cai pro antigo sozinha):

```python
try:
    serie_mensal = df.set_index('data').resample('ME').valor.mean()
except ValueError:
    serie_mensal = df.set_index('data').resample('M').valor.mean()
```

## Taxa de variação percentual entre períodos

```python
df['variacao_pct'] = df['valor'].pct_change() * 100
```

## Facetamento (um gráfico por categoria/ano, mesmos eixos)

```python
df['ano'] = df['data'].dt.year
df['mes_dia'] = df['data'].dt.strftime('%m-%d')

alt.Chart(df).mark_line().encode(
    x='mes_dia:T',
    y=alt.Y('valor:Q', scale=alt.Scale(domain=[5, 9])),
    color='ano:N',
    facet=alt.Facet('ano:N', columns=1)
).properties(height=50, width=400)
```

## Sobreposição (várias séries no mesmo gráfico, para comparar)

```python
alt.Chart(df).mark_line().encode(
    x='mes_dia:T',
    y='valor:Q',
    color='ano:N'          # uma linha por categoria, mesmo eixo
).properties(height=500, width=800)
```

## Interpretação de série temporal (modelo)

> "O gráfico mostra um comportamento cíclico/tendência de [alta/baixa] ao longo do tempo. Destaca-se o período de [X a Y], em que [descrição do desvio do padrão — pico, queda, aumento acelerado]."
