# Fluxograma rápido — o que fazer em cada questão

## Passo 1 — Que tipo de variável(is) a questão envolve?

- **1 variável qualitativa** → vá para `02-analise-univariada-qualitativa.md`
- **1 variável quantitativa** → vá para `03-histogramas-e-series-temporais.md` (distribuição) e `04-medidas-descritivas.md` (resumo numérico)
- **1 variável quantitativa ao longo do tempo** (datas) → série temporal, `03-histogramas-e-series-temporais.md`
- **2 variáveis qualitativas** → tabela de dupla entrada + gráfico de barras segmentadas, `05-analise-bivariada.md`
- **2 variáveis quantitativas** → diagrama de dispersão + correlação de Pearson, `05-analise-bivariada.md`
- **1 quantitativa comparada entre grupos** (ex: renda por gênero) → boxplots lado a lado, `05-analise-bivariada.md`

## Passo 2 — Checklist do que a professora sempre cobra

- [ ] Fiz o gráfico certo pro tipo de variável (nunca gráfico de setores para >5-6 categorias ou quando não soma 100%)
- [ ] Rodei `describe()` / medidas de centro e dispersão quando é quantitativa
- [ ] Chequei valores atípicos pela regra **1.5×AIQ** quando fez sentido
- [ ] **Interpretei por escrito** o resultado (nunca deixar só o código/gráfico sem texto)
- [ ] Se comparei grupos ou fiz bivariada, disse a direção e a força da relação/diferença

## Qual gráfico usar (variável quantitativa, 1 variável)

| Situação | Gráfico |
|---|---|
| Distribuição de frequência | Histograma (`mark_bar` + `bin`) |
| Evolução no tempo | Gráfico de linha (`mark_line`) com data no eixo x |
| Comparar dispersão/atípicos entre grupos | Boxplot (`mark_boxplot`) |

## Qual gráfico usar (variável qualitativa)

| Situação | Gráfico |
|---|---|
| Poucas categorias (até ~5-6), soma = 100% | Gráfico de setores (pizza) — mas **barras quase sempre é mais seguro e didático** |
| Muitas categorias, comparação de magnitude | Gráfico de barras (ordenado do maior pro menor, `sort='-y'`) |
| Categoria explicada por outra qualitativa | Barras segmentadas (empilhadas), em contagem ou em % (`stack="normalize"`) |

## Regra do valor atípico (1.5×AIQ)

```
AIQ = Q3 - Q1
Limite inferior = Q1 - 1.5*AIQ
Limite superior = Q3 + 1.5*AIQ
```
Valor fora de `[limite inferior, limite superior]` → potencial valor atípico.

## Média vs. Mediana — o que a diferença entre elas indica

- **Média > Mediana** → distribuição assimétrica à **direita** (poucos valores altos puxam a média pra cima). Ex: renda.
- **Média < Mediana** → distribuição assimétrica à **esquerda**.
- **Média ≈ Mediana** → distribuição aproximadamente **simétrica**.
- A **mediana é resistente** a valores atípicos; a **média não é**.
