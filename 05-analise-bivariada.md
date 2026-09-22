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

### Lendo o coeficiente de Pearson

| Valor de r | Interpretação |
|---|---|
| perto de **+1** | relação linear positiva forte (quando um sobe, o outro sobe) |
| perto de **-1** | relação linear negativa forte (quando um sobe, o outro desce) |
| perto de **0** | pouca ou nenhuma relação **linear** (mas pode haver relação não linear — ver Datasaurus Dozen: `r≈0` não significa ausência de padrão!) |

### Interpretação (modelo)

> "O diagrama de dispersão mostra uma relação linear [positiva/negativa] entre [var1] e [var2], confirmada pelo coeficiente de Pearson de [valor], que indica uma associação de intensidade [fraca/moderada/forte]. [Se houver atípico:] Ao removermos o valor atípico de [observação], o coeficiente [aumenta/diminui] para [valor], mostrando que o outlier estava [atenuando/inflando] a relação."

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
