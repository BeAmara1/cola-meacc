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

## As três medidas de dispersão baseadas na média

A professora cobra as três com "definição, exemplos, interpretação e **propriedades**" — então não basta calcular.

Todas partem do mesmo lugar: **o quanto cada observação se afasta da média** (o "desvio" de cada ponto, `xᵢ − x̄`). A diferença é o que se faz com esses desvios — e a razão de existirem três é que a soma simples dos desvios **sempre dá zero** (os positivos cancelam os negativos), então é preciso eliminar o sinal de algum jeito.

| Medida | Como elimina o sinal | Unidade | Fórmula |
|---|---|---|---|
| **Desvio médio** | valor absoluto | mesma dos dados | média de \|xᵢ − x̄\| |
| **Variância** (s²) | elevando ao quadrado | **ao quadrado** (ex: reais²) | soma de (xᵢ − x̄)² ÷ (n−1) |
| **Desvio padrão** (s) | raiz da variância | mesma dos dados | √s² |

```python
s = df['coluna']

desvio_medio = (s - s.mean()).abs().mean()   # ⚠️ .mad() NÃO existe mais no pandas
variancia = s.var()                          # padrão: divide por (n-1)
variancia_pop = s.var(ddof=0)                # se quiser dividir por n
desvio_padrao = s.std()                      # = raiz quadrada de s.var()
```

**Por que o desvio padrão é o mais usado**, se o desvio médio é mais intuitivo? Porque ele volta à **unidade original** dos dados (diferente da variância, que fica em unidade ao quadrado e por isso é difícil de interpretar sozinha) e tem propriedades matemáticas melhores que o desvio médio.

### Propriedades do desvio padrão (isso cai)

1. **s ≥ 0 sempre.** Nunca é negativo.
2. **s = 0 apenas quando todos os valores são iguais** (não há dispersão nenhuma).
3. **Tem a mesma unidade dos dados** — se a renda está em reais, s está em reais. (A variância está em reais², por isso não se interpreta diretamente.)
4. **Não é resistente**: como é calculado a partir da média, um único valor atípico infla bastante s.
5. **Somar uma constante a todos os valores não muda s** (a dispersão é a mesma, tudo só "andou" junto). Já a **média muda**.
6. **Multiplicar todos os valores por uma constante multiplica s pela mesma constante** (mudar de reais para centavos multiplica o desvio padrão por 100).
7. Faz sentido como resumo principalmente em distribuições **aproximadamente simétricas** — em distribuição assimétrica ou com atípico, prefira **mediana + AIQ**.

### Qual par de medidas usar

| Distribuição | Centro | Dispersão |
|---|---|---|
| Aproximadamente simétrica, sem atípicos | **média** | **desvio padrão** |
| Assimétrica ou com valores atípicos | **mediana** | **AIQ** (resumo dos 5 números) |

> **Frase-modelo:** "Como a distribuição é assimétrica à direita e apresenta valor atípico, a mediana ([valor]) e a amplitude interquartil ([valor]) descrevem melhor o centro e a dispersão do que média e desvio padrão, que não são resistentes a valores extremos."

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
# CUIDADO: var_name e value_name NÃO podem ter o mesmo nome de uma coluna
# que já existe no df, senão dá erro ("cannot match an element in the
# DataFrame columns"). Se der, é só trocar por nomes inventados.
df_long = df.melt(
    id_vars=['id'],
    value_vars=['grupo_A', 'grupo_B'],
    var_name='Category',
    value_name='Value'
)

# 2) plotar
alt.Chart(df_long).mark_boxplot(extent=1.5, size=40).encode(
    alt.X('Value:Q'),
    alt.Y('Category:N')
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
