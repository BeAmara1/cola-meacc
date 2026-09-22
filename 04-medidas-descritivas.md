# Medidas descritivas (centro, dispersão, atípicos)

## Tudo de uma vez

```python
df['coluna'].describe()
# count, mean, std, min, 25% (Q1), 50% (mediana), 75% (Q3), max
```

## Medidas de centro

```python
df['coluna'].mean()      # média — sensível a valores atípicos
df['coluna'].median()    # mediana — resistente a valores atípicos
df['coluna'].mode()      # moda (pode ter mais de uma = plurimodal)
df['coluna'].value_counts()  # pra achar a moda "na mão" e ver se é multimodal
```

## Medidas de dispersão

```python
df['coluna'].std()                     # desvio padrão
df['coluna'].var()                     # variância
df['coluna'].max() - df['coluna'].min()  # amplitude total

q1 = df['coluna'].quantile(0.25)
q3 = df['coluna'].quantile(0.75)
aiq = q3 - q1                          # amplitude interquartil (AIQ / IQR)
```

Com `statistics` (útil pra listas soltas, não Series):
```python
from statistics import mean, median, stdev
mean(lista); median(lista); stdev(lista)
```

## Regra do valor atípico (1.5 × AIQ)

```python
q1 = df['coluna'].quantile(0.25)
q3 = df['coluna'].quantile(0.75)
aiq = q3 - q1

limite_inf = q1 - 1.5 * aiq
limite_sup = q3 + 1.5 * aiq

atipicos = df[(df['coluna'] < limite_inf) | (df['coluna'] > limite_sup)]
```

## Boxplot

```python
import altair as alt

# do mínimo ao máximo (sem destacar atípicos)
alt.Chart(df).mark_boxplot(extent='min-max').encode(
    y='coluna:Q'
).properties(width=200)

# destacando atípicos pela regra 1.5xAIQ (usar esse na prova!)
alt.Chart(df).mark_boxplot(extent=1.5).encode(
    y='coluna:Q'
).properties(width=200)
```

## Boxplots lado a lado (comparar grupos — ex: homens x mulheres, brancos x negros)

```python
# 1) transformar em formato "long" com melt
df_long = df.melt(
    id_vars=['id'],
    value_vars=['grupo_A', 'grupo_B'],
    var_name='categoria',
    value_name='valor'
)

# 2) plotar
alt.Chart(df_long).mark_boxplot(extent=1.5, size=40).encode(
    alt.X('valor:Q'),
    alt.Y('categoria:N')
).properties(height=200, width=600)
```

Ou, se já são duas bases separadas:
```python
df1['origem'] = 'Grupo A'
df2['origem'] = 'Grupo B'
df_junto = pd.concat([df1, df2])

alt.Chart(df_junto).mark_boxplot(extent=1.5, size=40).encode(
    alt.X('valor:Q'),
    alt.Y('origem:N')
).properties(height=200)
```

## Interpretação (modelos)

**Um valor atípico influenciando a média:**
> "A média com o valor atípico é [X], e sem ele cai/sobe para [Y] — uma diferença de [Z]. Já a mediana muda pouco ([A] com vs [B] sem), pois é uma medida resistente a valores atípicos."

**Comparando dispersão entre grupos (boxplot lado a lado):**
> "As duas distribuições são assimétricas à direita, mas o grupo A tem AIQ maior ([valor] vs [valor]), mostrando maior dispersão/variabilidade. A mediana do grupo A ([valor]) é [maior/menor] que a do grupo B ([valor]), indicando um valor típico [maior/menor]. [Ambos apresentam / apenas um apresenta] valores atípicos segundo a regra 1.5×AIQ."
