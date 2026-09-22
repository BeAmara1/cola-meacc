# Catálogo das bases da matéria (tudo verificado rodando)

Todas as bases do repositório da professora foram abertas e perfiladas: nomes **exatos** de coluna, tipos, tamanho, armadilhas e respostas conferidas. Nada aqui é de memória — foi tudo computado.

---

## ⚠️ O ALERTA MAIS IMPORTANTE DESTE REPOSITÓRIO

**As bases das aulas e as bases da lista de revisão NÃO são as mesmas** — mesmo quando tratam do mesmo assunto. Elas têm **nomes de coluna diferentes** (inglês vs português) e, pior, **valores diferentes**.

Copiar a resposta da aula para a questão da revisão **dá resposta errada**:

| Assunto | Base da AULA | Base da REVISÃO | Consequência |
|---|---|---|---|
| Tempo de viagem CN | `eg02-01nctravel.xls`, coluna `Minutes`, máx **70** | `TEMPOVIAGEMCN.xls`, coluna `Minutos`, máx **60** | Na aula, 70 **é** valor atípico. Na revisão, **não há** nenhum atípico |
| Tempo de viagem NY | `eg02-03nytravel.xls`, coluna `Minutes`, máx **75** | `TEMPOVIAGEMNY.xls`, coluna `Minutos`, máx **85** | Na aula, **não há** atípico. Na revisão, **85 é** atípico |
| Emissão de CO2 | `ex02-05co2emiss.xls`, 203 países, maior = **Qatar (43,86)** | `EMISSAOCO2.xls`, 39 países (pop ≥ 30 mi), maior = **Estados Unidos (18,91)** | Responder "Qatar" na revisão está **errado** — Qatar nem está na base |
| Áreas de estudo | `eg01-02majors.xls`, `Field of Study` / `Percent` | `HABILITA.xls`, `Disciplina` / `Percentual` | Código da aula referencia coluna que não existe → **gráfico vazio, sem erro** |
| Mídias sociais / rádio | `ex01-03socmedia.xls`, `Social Media Site` / `Percentage` | `FORMATORADIO.xls`, `Formato` / `NivelAudiencia` | Idem |

**Regra de ouro:** ao abrir qualquer base, rode `list(df.columns)` **antes** de escrever qualquer gráfico. Nunca assuma o nome da coluna.

---

## O ambiente da matéria (do `requirements.txt` da professora)

```
altair==6.2.2      pandas==3.0.5      xlrd==2.0.2
openpyxl==3.1.5    vegafusion==2.0.3  vl-convert-python==1.9.0.post1
pyarrow==25.0.1    matplotlib==3.11.2
```

Duas consequências práticas:
- **pandas 3.0** → `resample('M')` **dá erro**; use `'ME'` (mês) e `'YE'` (ano). O gabarito de 2025 usa a escrita antiga.
- `xlrd` está na lista porque quase toda base é `.xls` (formato antigo). Se der `Missing optional dependency 'xlrd'`, rode `!pip install xlrd`.

---

## Bases das aulas práticas

| Arquivo | Aula | Tamanho | Colunas (nomes exatos) | Observações |
|---|---|---|---|---|
| `00-1-shipman-confirmed-victims-x.csv` | 4, 6, 14 | 215 × 10 | `DateofDeath`, `Name`, `Age`, `PlaceofDeath`, `Decision`, `yearOfDeath`, `gender`, `fractionalDeathYear`, `ageBracket`, `gender2` | `gender` é 0/1 numérico; **`gender2`** é o rótulo ("Women"/"Men") — use esse nos gráficos. `DateofDeath` é texto ('17-Mar-75') |
| `01-1-child-heart-survival-x.csv` | 4 | 13 × 6 | `Hospital`, `Operations`, `Survivors`, `Deaths`, `ThirtyDaySurvival`, `PercentageDying` | É o dado de **2012-15** (mesmo conteúdo do `02-5-...-2012-x.csv`). `Hospital` tem espaço sobrando em alguns nomes |
| `eg01-02majors.xls` | 4 | 10 × 2 | `Field of Study`, `Percent` | Soma = 100 |
| `ex01-03socmedia.xls` | 4 | 5 × 2 | `Social Media Site`, `Percentage` | Soma = **90** → faltam 10% de "Outras" |
| `TESTEIOWA.xls` | 6 | 947 × 1 | `Escore` | Distribuição simétrica (exemplo do livro) |
| `NASCIDOSFORA.xls` | 6, 15 | 51 × 2 | `Estado`, `PctNascFora` | 51 = 50 estados + DC |
| `FACCUSTO.xls` | 6, 15 | 31 × 2 | `ano`, `mensalidade` | 1980 a 2010 |
| `NIVELAGUA.xls` | 6 | 3287 × 2 | `Data`, `AltMediaMedidor` | **50 valores ausentes**; `Data` vem como texto → `pd.to_datetime` |
| `Base RID - Evolução X.csv` | 6 | 613 × 5 | `Data`, `Count`, `Categoria`, `Análise`, `Relatório` | Granularidade **horária** → precisa de `resample`. Tema: Eleições EUA |
| `RID - Evolução Facebook.csv` | 6 | 52 × 5 | `Data`, `Count`, `Categoria`, `Análise`, `Relatório` | `Categoria` separa Lula / Bolsonaro |
| `02-4-sexual-partners-counts-x.csv` | 11 | 137 × 5 | `NumPartners`, `MenCount`, `MenPercent`, `WomenCount`, `WomenPercent` | Base **agregada**: cada linha é um nº de parceiros, não uma pessoa |
| `eg02-01nctravel.xls` | 11 | 15 × 1 | `Minutes` | ⚠️ diferente do `TEMPOVIAGEMCN.xls` |
| `eg02-03nytravel.xls` | 11 | 20 × 1 | `Minutes` | ⚠️ diferente do `TEMPOVIAGEMNY.xls` |
| `ex02-02health.xls` | 11 | 35 × 2 | `Country`, `Dollars` | EUA é o atípico alto |
| `ex02-05co2emiss.xls` | 11 | 203 × 2 | `Country`, `CO2 emissions` | ⚠️ note o **espaço** no nome da coluna |
| `02-5-child-heart-surgery-1991-x.csv` | 14 | 12 × 6 | `Hospital`, `Operations`, `Survivors`, `Deaths`, `ThirtyDaySurvival`, `PercentageDying` | **Bristol é a linha 0** (71,3% de sobrevivência) — é o `drop([0])` do notebook |
| `02-5-child-heart-surgery-2012-x.csv` | 14 | 13 × 6 | idem | Linha 0 = London - Harley Street |
| `DatasaurusDozen.tsv` | 14 | 1846 × 3 | `dataset`, `x`, `y` | **É TSV**: `pd.read_csv(..., sep='\t')`. 13 conjuntos na coluna `dataset` |

---

## Bases da lista de revisão (Aula 15) — com as respostas conferidas

### `HABILITA.xls` — 10 × 2 · `Disciplina`, `Percentual` (Q2)
Soma dos percentuais = **99,9** → não é 100 por **arredondamento** (não falta categoria; já existe "Outra").

### `FORMATORADIO.xls` — 12 × 2 · `Formato`, `NivelAudiencia` (Q3)
Soma = **67,3** → **32,7%** da audiência ouve "outros formatos".
Por isso gráfico de setores **não** seria correto sem acrescentar a fatia "Outro formato".

### `NASCIDOSFORA.xls` — 51 × 2 · `Estado`, `PctNascFora` (Q4)
Resumo dos 5 números: **mín 1,2 · Q1 3,8 · mediana 6,3 · Q3 12,5 · máx 27,2**
AIQ = 8,7 → limite superior = 12,5 + 1,5×8,7 = **25,55**
**Califórnia (27,2) está acima de 25,55 → É valor atípico**, não apenas a maior observação.

### `EMISSAOCO2.xls` — 39 × 2 · `País`, `CO2` (Q6)
média **4,61** > mediana **3,95** → assimétrica à direita.
AIQ = 7,20 → limite superior = **18,73**.
Único atípico: **Estados Unidos (18,91)**. Top 5: EUA 18,91 · Canadá 16,92 · Rússia 10,83 · Coreia do Sul 10,49 · Japão 9,85.
⚠️ **Qatar não está nesta base** (ele é o extremo da base *da aula*, que tem 203 países).

### `TEMPOVIAGEMCN.xls` (15 × 1) e `TEMPOVIAGEMNY.xls` (20 × 1) · coluna `Minutos` (Q7)

| | Carolina do Norte | Nova York |
|---|---|---|
| média | 22,47 | 31,25 |
| mediana | 20,0 | 22,5 |
| moda | 10 | 15 |
| desvio padrão | 15,23 | 21,88 |
| Q1 / Q3 | 10 / 30 | 15 / 41,25 |
| AIQ | 20,0 | 26,25 |
| mín / máx | 5 / 60 | 5 / 85 |
| atípicos (1,5×AIQ) | **nenhum** | **85** |

Leitura: NY tem mediana maior (viagens tipicamente mais longas), AIQ maior (mais dispersão) e um atípico; CN é mais concentrada.

### `FELICIDADE.xls` — 50 × 3 · `Estado`, `BRFSS`, `CompDif` (Q8)
**r(BRFSS, CompDif) = −0,565** → relação linear **negativa**, de intensidade **moderada**.

Como interpretar (essa é a parte que exige cuidado — releia as escalas no enunciado):
- `BRFSS` **menor** = mais feliz (medida subjetiva)
- `CompDif` **posto 1** = mais feliz (medida objetiva)
- Logo, **concordância** entre as duas medidas produziria correlação **positiva** (feliz = BRFSS baixo *e* posto baixo).

Os dados mostram o contrário. Conferindo os extremos:
- Postos 1-3 (mais felizes **objetivamente**): Wyoming (BRFSS −0,046), Dakota do Sul (−0,014), Arkansas (−0,017)
- Postos 48-50 (menos felizes objetivamente): Nova York (−0,088), Michigan (−0,079), Illinois (−0,072)
- BRFSS médio dos 10 melhores postos: **−0,009** · dos 10 piores postos: **−0,065**

Ou seja: os estados **pior** colocados na medida objetiva têm BRFSS **mais baixo** — que, pela regra do enunciado, significa **mais felizes subjetivamente**. As duas medidas, portanto, **discordam**.

> Na resposta, **cite explicitamente a direção de cada escala** antes de concluir. Sem isso, o mesmo sinal de correlação pode ser lido como concordância ou discordância.

### `CESSAFUMO.xls` — 6 × 3 · `Fumou`, `Tratamento`, `Contagem` (Q9)
⚠️ **Esta base já vem em formato LONG com uma coluna de contagem** — não é uma lista de pessoas. Então `groupby(...).size()` **não** serve (contaria 6 linhas). Use `pivot`:

```python
cf = pd.read_excel('CESSAFUMO.xls')
tab = cf.pivot(index='Tratamento', columns='Fumou', values='Contagem')
tab['total'] = tab.sum(axis=1)
tab['% parou'] = (tab['Não'] / tab['total'] * 100).round(1)
```

Resultado conferido (% que **parou** de fumar, ou seja `Fumou = Não`):

| Tratamento | parou | continuou | total | **% que parou** |
|---|---|---|---|---|
| Chantix | 155 | 197 | 352 | **44,0%** |
| Bupropiona | 97 | 232 | 329 | **29,5%** |
| Placebo | 61 | 283 | 344 | **17,7%** |

Como os três grupos têm tamanhos diferentes (352, 329, 344), a comparação **tem que ser em percentual**. Chantix > bupropiona > placebo, com diferença grande.

Para o gráfico, o `Count` já pronto entra como peso:
```python
alt.Chart(cf).mark_bar().encode(
    x=alt.X('sum(Contagem):Q', stack='normalize'),
    y='Tratamento:N', color='Fumou:N')
```

### `SATMAT.xls` — 51 × 3 · `Estado`, `PctSAT`, `SAT-Mat` (Q10)
**r(PctSAT, SAT-Mat) = −0,866** → negativa **forte**.
Quanto maior o percentual de alunos que faz o SAT no estado, **menor** a média estadual — o que se explica por **viés de seleção** (onde poucos fazem, só os mais preparados fazem), não por qualidade de ensino.
⚠️ A coluna se chama `SAT-Mat`, com hífen — use `df['SAT-Mat']`, não `df.SAT-Mat`.

### `InfoFamiliasEntrevistadas.csv` — 120 × 6 (Q12)
Colunas: `Nº`, `Local`, `P.a.p.`, `Instr.`, `Tam.`, `Renda`
⚠️ **Três nomes com ponto** (`P.a.p.`, `Instr.`, `Tam.`) e um com caractere especial (`Nº`). Ponto no nome faz o **Altair desenhar gráfico vazio sem dar erro**. Renomeie logo na leitura:

```python
inf = pd.read_csv('InfoFamiliasEntrevistadas.csv')
inf = inf.rename(columns={'P.a.p.': 'Pap', 'Instr.': 'Instr', 'Tam.': 'Tam', 'Nº': 'N'})
```

Resposta conferida (renda ≤ 5 salários = baixa; > 5 = alta):

| Faixa de renda | não usa programa | **usa programa** | total |
|---|---|---|---|
| renda baixa | 15 (27,3%) | 40 (**72,7%**) | 55 |
| renda alta | 27 (41,5%) | 38 (**58,5%**) | 65 |

Há associação: entre as famílias de renda baixa, 72,7% usam o programa, contra 58,5% entre as de renda alta — diferença de ~14 pontos percentuais no sentido esperado.

### `OECD_IDH_data.csv` — 23 × 9 (Q13)
Colunas: `nation`, `GDP`, `Unemploy`, `Inequal`, `Health`, `Phys`, `C02`, `Parlia`, `FemEcon`
⚠️ **Armadilha séria:** a coluna `Inequal` vem como **texto**, porque usa a letra `'I'` como marcador de valor ausente. Consequência: `df.corr()` **exclui essa coluna silenciosamente** e `describe()` mostra `unique/top/freq`. Se escolher `Inequal` para a análise, converta primeiro:

```python
oc['Inequal'] = pd.to_numeric(oc['Inequal'], errors='coerce')   # 'I' vira NaN
```

⚠️ Note também que a coluna de CO2 se chama **`C02`** (com o número zero, não a letra O) — provável erro de digitação da base, mas é o nome real.
Maior PIB (o atípico do histograma da parte b): **Luxemburgo (69.961)**.

### `Censo_estados.xlsx` — 28 × 5 (Q14)
Colunas: `Territorialidades`, `Esperança de vida ao nascer 2000`, `Mortalidade infantil 2000`, `Taxa de analfabetismo - 18 anos ou mais de idade 2000`, `Renda per capita 2000`
⚠️ **São 28 linhas, não 27: a primeira linha é "Brasil"**, o agregado do país inteiro — não é um estado. Misturar o agregado com as unidades é erro de unidade de análise. Remova:

```python
ce = pd.read_excel('Censo_estados.xlsx')
ce = ce[ce.Territorialidades != 'Brasil']
```
(Neste caso o efeito numérico é pequeno — r vai de −0,8325 para −0,8314 —, mas o argumento conceitual vale ponto.)

Matriz de correlação conferida (sem a linha Brasil):

| | Esp. vida | Mort. infantil | Analfabetismo | Renda |
|---|---|---|---|---|
| **Esperança de vida** | 1,000 | −0,886 | −0,856 | 0,852 |
| **Mortalidade infantil** | −0,886 | 1,000 | **0,931** | −0,823 |
| **Analfabetismo** | −0,856 | 0,931 | 1,000 | −0,831 |
| **Renda per capita** | 0,852 | −0,823 | −0,831 | 1,000 |

Todos os pares têm correlação forte. O par mais forte é **mortalidade infantil × analfabetismo (0,931)**.
⚠️ Esta base é do Censo de **2000**. A prova de 2025 usou uma base de **2010** — os nomes das colunas mudam junto com o ano.

---

## Checklist de 30 segundos ao abrir qualquer base

```python
print(df.shape)
print(list(df.columns))     # nomes EXATOS — tem ponto? espaço? hífen? maiúscula?
print(df.dtypes)            # algum número veio como texto?
print(df.isna().sum())      # ausentes
df.head()                   # tem linha de agregado ("Brasil", "Total")?
```
