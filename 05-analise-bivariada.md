# Análise bivariada

## Duas variáveis qualitativas → Tabela de dupla entrada

```python
# formato matricial (wide) — bom pra visualizar
tabela = df.groupby(['var1', 'var2']).size().unstack(1)
tabela.loc['Total', :] = tabela.sum(axis=0)
tabela.loc[:, 'Total'] = tabela.sum(axis=1)
tabela.fillna(0, inplace=True)
tabela

# formato long — bom pra plotar depois
tabela_long = df.groupby(['var1', 'var2']).size()
# ou:
tabela_long = pd.pivot_table(df, index=['var1', 'var2'], aggfunc='size')
```

### Distribuição marginal vs. condicional (os dois nomes são cobrados)

- **Distribuição marginal** = a distribuição de **uma só** das variáveis, ignorando a outra. São os **totais nas margens** da tabela (daí o nome) — a última linha e a última coluna.
- **Distribuição condicional** = a distribuição de uma variável **dentro de cada categoria** da outra. É ela que responde se há associação.

```python
tabela = df.groupby(['var1', 'var2']).size().unstack(1)

# marginais: os totais das margens
marginal_var1 = tabela.sum(axis=1)          # total de cada categoria de var1
marginal_var2 = tabela.sum(axis=0)          # total de cada categoria de var2

# marginais em percentual
marginal_var1_pct = (marginal_var1 / marginal_var1.sum() * 100).round(1)
```

**Como usar cada uma na resposta:** a marginal descreve o perfil geral da amostra ("60% dos respondentes são do grupo A"); a condicional é que revela **associação** ("entre os do grupo A, 80% têm X, contra 30% entre os do grupo B").

### Distribuição condicional (percentual em relação a UMA das variáveis)

```python
# % de var2 dentro de cada categoria de var1 (condicional em var1 — level=0)
(tabela_long / tabela_long.groupby(level=0).transform(sum) * 100)

# % de var1 dentro de cada categoria de var2 (condicional em var2 — level=1)
(tabela_long / tabela_long.groupby(level=1).transform(sum) * 100)
```

### Gráfico de barras segmentadas

```python
import altair as alt

base = tabela_long.reset_index().rename(columns={0: 'contagem'})

# em valores absolutos
alt.Chart(base).mark_bar().encode(
    x='contagem:Q',
    y='var1:N',
    color='var2:N'
)

# em percentual (normalize) — melhor pra COMPARAR proporções entre categorias
alt.Chart(base).mark_bar().encode(
    x=alt.X('contagem:Q', stack='normalize'),
    y='var1:N',
    color='var2:N'
)
```

### Interpretação (modelo)

> "Olhando a distribuição condicional de [var2] dentro de cada categoria de [var1], observamos que [categoria] apresenta a maior proporção de [valor], enquanto [categoria] apresenta a menor. Isso sugere [associação/ausência de associação] entre as duas variáveis."

---

## Duas variáveis quantitativas → Diagrama de dispersão + correlação de Pearson

```python
alt.Chart(df).mark_circle().encode(
    x='var1:Q',
    y='var2:Q',
    tooltip=['id', 'var1', 'var2']
)

# correlação de Pearson
df[['var1', 'var2']].corr(numeric_only=True)

# testando sensibilidade a um valor atípico (remover e recalcular)
df.drop([indice_do_atipico])[['var1', 'var2']].corr(numeric_only=True)
```

### Incluindo uma terceira variável qualitativa no diagrama

Colorir os pontos por uma variável categórica mostra **três variáveis num gráfico só** — e às vezes revela que a relação é diferente dentro de cada grupo. É o que o caso Shipman faz (ano da morte × idade, colorido por gênero).

```python
alt.Chart(df).mark_circle(size=60).encode(
    x='var1:Q',
    y='var2:Q',
    color='categoria:N',          # <- a terceira variável, qualitativa
    tooltip=['var1', 'var2', 'categoria']
)
```

> **Frase-modelo:** "Ao colorir os pontos por [categoria], nota-se que [grupo] se concentra em [região do gráfico], sugerindo que a relação entre [var1] e [var2] se comporta de forma diferente entre os grupos."

### Lendo o coeficiente de Pearson

| Valor de r | Interpretação |
|---|---|
| perto de **+1** | relação linear positiva forte (quando um sobe, o outro sobe) |
| perto de **-1** | relação linear negativa forte (quando um sobe, o outro desce) |
| perto de **0** | pouca ou nenhuma relação **linear** (mas pode haver relação não linear — ver Datasaurus Dozen: `r≈0` não significa ausência de padrão!) |

### Interpretação — os 3 itens do "padrão geral" + o desvio

A professora pede a leitura da dispersão por **direção, forma e intensidade** (padrão geral) mais o **desvio**:

| Item | O que responder |
|---|---|
| **Direção** | positiva (sobe junto) ou negativa (um sobe, outro desce) |
| **Forma** | **linear** ou **não linear** (curva) — é o item que mais se esquece |
| **Intensidade** | fraca, moderada ou forte (o quão perto os pontos estão de uma reta) |
| **Desvio** | pontos fora do padrão geral (atípicos) |

> "O diagrama de dispersão mostra uma relação **linear** e **negativa** entre [var1] e [var2], de intensidade **forte**, confirmada pelo coeficiente de Pearson de [valor]. [Se houver atípico:] Ao removermos o valor atípico de [observação], o coeficiente [aumenta/diminui] para [valor], mostrando que o ponto estava [atenuando/inflando] a relação."

---

## Uma quantitativa comparada entre grupos (qualitativa x quantitativa)

Ver boxplots lado a lado em `04-medidas-descritivas.md`.

## Criar variável qualitativa a partir de quantitativa (faixas/categorias)

```python
df['faixa'] = pd.cut(
    df['idade'],
    bins=[0, 18, 30, 55, 100],
    labels=['Criança', 'Jovem Adulto', 'Adulto', 'Idoso'],
    right=True   # intervalo fechado à direita
)
```
