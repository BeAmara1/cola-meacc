# Lista de revisão (Aula 15) — com o roteiro de ataque de cada questão

As 14 questões da aula de revisão da professora (`aulas_praticas/15-revisao/Revisão.ipynb`), cada uma com **o que a questão está cobrando** e **o caminho para responder**. Como a lista de revisão costuma antecipar o formato da prova, vale usar isso como mapa de estudo.

Os arquivos de dados de cada questão estão na pasta `15-revisao/` do repositório da matéria.

> 🔴 **Antes de usar este arquivo, leia o alerta do `15-catalogo-das-bases.md`:** as bases da revisão **não são as mesmas** das aulas, mesmo tratando do mesmo assunto — têm outros nomes de coluna e **outros valores**. Copiar a resposta da aula para a revisão dá resposta errada. Todos os números abaixo foram conferidos rodando as bases **da revisão**.

---

### Q1 — Classificar variáveis
> Homicídios no Brasil; time de futebol; taxa de desemprego; satisfação com o governo; denominação religiosa; renda per capita.

**Cobra:** vocabulário de tipos de variável.
**Respostas:** quantitativa discreta · qualitativa nominal · quantitativa contínua · qualitativa **ordinal** (tem ordem!) · qualitativa nominal · quantitativa contínua.
**Ver:** `01-tipos-de-variaveis.md`

---

### Q2 — "Qual área de estudo?" (HABILITA.xls)
> (a) Quem eram as observações originais? (b) Verifique a consistência. (c) Gráficos + interpretação.

**Cobra:** unidade de análise + checagem de consistência de percentuais + gráfico de qualitativa.
**Colunas reais:** `Disciplina`, `Percentual` (10 linhas).
**Roteiro:**
- (a) **Os estudantes** — a tabela está agregada por área, mas quem gerou o dado foi cada calouro. (Ver `11-conceitos-fundamentais.md` §1.)
- (b) Conferido: a soma dá **99,9**, não 100 → é **erro de arredondamento** (a categoria "Outra" já existe na base, então não é caso de categoria faltante).
- (c) Barras ordenadas (`sort='-y'`). Setores só se somar 100% e houver poucas categorias.

**Ver:** `02-analise-univariada-qualitativa.md`

---

### Q3 — "Você ouve rádio?" (FORMATORADIO.xls)
> (a) Soma dos níveis de audiência; qual % ouve outros formatos. (b) Seria correto usar gráfico de setores? (c) Barras incluindo "Outro formato".

**Cobra:** exatamente a pegadinha do gráfico de setores.
**Colunas reais:** `Formato`, `NivelAudiencia` (12 linhas).
**Roteiro:**
- (a) Conferido: a soma dá **67,3** → **32,7%** da audiência ouve outros formatos.
- (b) **Não, não do jeito que está** — setores exige partes de um todo (soma 100%). Como a tabela só traz os formatos mais populares, falta a fatia "Outros". *Depois* de acrescentar "Outro formato", aí sim somaria 100% e o setor seria defensável (ainda assim, barras comunicam melhor com muitas categorias).
- (c) Acrescente a linha "Outras" e plote barras.

**Ver:** `02-analise-univariada-qualitativa.md`

---

### Q4 — Nascidos fora (NASCIDOSFORA.xls)
> (a) Histograma com classes de 5% começando em 0. (b) Resumo dos 5 números. (c) Califórnia é atípico ou só o maior valor? Regra 1,5×AIQ.

**Cobra:** histograma com bin controlado + resumo dos 5 números + regra do atípico.
**Roteiro:**
- (a) `bin=alt.Bin(step=5, extent=[0, 30])`
- (b) Resumo dos 5 números conferido: **mín 1,2 · Q1 3,8 · mediana 6,3 · Q3 12,5 · máx 27,2**
- (c) AIQ = 12,5 − 3,8 = **8,7** → limite superior = 12,5 + 1,5×8,7 = **25,55**. Como Califórnia = **27,2 > 25,55**, ela **é** um valor atípico (não é apenas a maior observação). Mostre essa conta na resposta.

**Ver:** `03-histogramas-e-series-temporais.md` e `04-medidas-descritivas.md`

---

### Q5 — Custo da faculdade (FACCUSTO.xls)
> (a) Gráfico temporal. (b) Padrão geral. (c) Desvios do padrão (atípicos, quedas, aumentos rápidos). (d) Série das taxas ou do % de aumento?

**Cobra:** série temporal + leitura de tendência + variação percentual.
**Roteiro:**
- (a) `mark_line()` com ano no x
- (b) Tendência **de alta** ao longo de todo o período
- (c) Procure os trechos de inclinação mais forte — no caso visto em aula, ~2002-2004 (e picos em 1983 e 2009 no gráfico de variação)
- (d) **As duas coisas**, mas o gráfico de `pct_change()` é melhor para achar *quando* o aumento fugiu do padrão, porque tendência de alta constante esconde a aceleração

**Ver:** `03-histogramas-e-series-temporais.md`

---

### Q6 — Emissão de CO2 (EMISSAOCO2.xls)
> (a) Por que medir por pessoa e não total? (b) Histograma: forma, centro, dispersão. (c) Atípicos. (d) Média e mediana — por que diferem?

**Cobra:** normalização de indicador + descrição completa de distribuição.
**Colunas reais:** `País`, `CO2` — **39 países** (só os com população ≥ 30 milhões).
**Roteiro:**
- (a) Porque **total confunde tamanho populacional com intensidade de emissão** — China e Índia emitem muito no total por terem muita gente. Per capita permite comparar países de tamanhos diferentes (mesma lógica de usar percentual em vez de contagem).
- (b) Assimétrica à direita, unimodal. Conferido: média **4,61** · mediana **3,95** · mín 0,03 · máx 18,91
- (c) AIQ = 7,20 → limite superior **18,73**. Único atípico: **Estados Unidos (18,91)**. Top 5: EUA · Canadá (16,92) · Rússia (10,83) · Coreia do Sul (10,49) · Japão (9,85).
  > ⚠️ **Não responda "Qatar".** Qatar é o extremo da base *da aula* (`ex02-05co2emiss.xls`, 203 países) — ele nem aparece nesta base da revisão.
- (d) Média > mediana **porque** a cauda à direita (poucos países com emissão alta) puxa a média, e a média não é resistente

---

### Q7 — Tempo de viagem CN × NY (TEMPOVIAGEMCN.xls, TEMPOVIAGEMNY.xls)
> Análise completa: média, moda, mediana, quartis, boxplot, atípicos + comparação entre as duas bases.

**Cobra:** a questão "kitchen sink" de medidas descritivas + comparação de grupos.
**Coluna real nas duas bases:** `Minutos` (em português — nas bases da aula é `Minutes`).
**Roteiro:**
1. `describe()` nas duas
2. Moda via `value_counts()` (atenção: pode ser **plurimodal**)
3. AIQ e regra 1,5×AIQ em cada uma
4. **Junte as duas bases** (`concat` com uma coluna de origem) e faça **boxplots lado a lado** — é isso que permite a comparação
5. Interprete: quem tem mediana maior, quem tem mais dispersão, quem tem atípico

**Valores conferidos nas bases da revisão:**

| | Carolina do Norte (n=15) | Nova York (n=20) |
|---|---|---|
| média | 22,47 | 31,25 |
| mediana | 20,0 | 22,5 |
| moda | 10 | 15 |
| desvio padrão | 15,23 | 21,88 |
| Q1 / Q3 | 10 / 30 | 15 / 41,25 |
| AIQ | 20,0 | 26,25 |
| mín / máx | 5 / 60 | 5 / 85 |
| atípicos | **nenhum** | **85** |

> ⚠️ Na base **da aula**, Carolina do Norte tem o 70 como atípico — o notebook inteiro gira em torno disso. Na base **da revisão** não há atípico em CN, e quem tem atípico é NY. Não reaproveite a conclusão da aula.

**Ver:** `04-medidas-descritivas.md` (seção de boxplots lado a lado)

---

### Q8 — Estados felizes (FELICIDADE.xls)
> (a) Dispersão de BRFSS (resposta) contra posto (explicativa). (b) Associação positiva ou negativa? (c) Concordância entre medida subjetiva e objetiva? (d) Atípicos?

**Cobra:** bivariada quantitativa + **atenção à direção da escala**.
**Colunas reais:** `Estado`, `BRFSS`, `CompDif` (50 linhas).
**Roteiro:**
- (a) Explicativa (`CompDif`, o posto) no **x**, resposta (`BRFSS`) no **y** — a questão diz explicitamente
- (b) Conferido: **r = −0,565** → relação linear **negativa**, intensidade **moderada**
- (c) ⚠️ **Aqui está a pegadinha da lista.** No enunciado, *menor* BRFSS = mais feliz, e posto 1 = mais feliz. Então **concordância** entre as medidas produziria correlação **positiva**. Como deu **negativa**, as medidas **discordam**.
  Confirmando nos extremos: os 10 estados de melhor posto objetivo têm BRFSS médio de **−0,009**, enquanto os 10 de pior posto têm **−0,065** — ou seja, os pior colocados objetivamente são os que **se declaram mais felizes**. (Postos 1-3: Wyoming, Dakota do Sul, Arkansas. Postos 48-50: Nova York, Michigan, Illinois.)
  **Escreva a direção de cada escala antes de concluir** — sem isso, o mesmo sinal pode ser lido dos dois jeitos.
- (d) Pontos fora da nuvem; nomeie o estado

**Ver:** `05-analise-bivariada.md` e `09-teoria-analise-bivariada.md`

---

### Q9 — Parar de fumar (CESSAFUMO.xls)
> Tabela de dupla entrada de tratamento (Chantix / bupropiona / placebo) × parou de fumar. "Como isso depende do tratamento recebido?"

**Cobra:** bivariada qualitativa × qualitativa com **distribuição condicional**.
**Colunas reais:** `Fumou`, `Tratamento`, `Contagem` — só **6 linhas**.
**⚠️ Atenção ao formato:** a base já vem **agregada em formato long**, com a contagem numa coluna. `groupby(...).size()` **não funciona** aqui (contaria 6 linhas). Use `pivot`:

```python
cf = pd.read_excel('CESSAFUMO.xls')
tab = cf.pivot(index='Tratamento', columns='Fumou', values='Contagem')
tab['total'] = tab.sum(axis=1)
tab['% parou'] = (tab['Não'] / tab['total'] * 100).round(1)
```

**Resultado conferido** (parar de fumar = `Fumou` é "Não"):

| Tratamento | parou | continuou | total | **% que parou** |
|---|---|---|---|---|
| Chantix | 155 | 197 | 352 | **44,0%** |
| Bupropiona | 97 | 232 | 329 | **29,5%** |
| Placebo | 61 | 283 | 344 | **17,7%** |

**Roteiro:**
- Os grupos têm **tamanhos diferentes** (352, 329, 344) → comparar contagem bruta é errado, **use percentual**
- A explicativa é o **tratamento** → condicione nele
- Gráfico: `alt.Chart(cf).mark_bar().encode(x=alt.X('sum(Contagem):Q', stack='normalize'), y='Tratamento:N', color='Fumou:N')`
- Conclusão: Chantix (44%) mais que dobra a taxa do placebo (17,7%); bupropiona fica no meio (29,5%)
- ⚠️ Aqui **é** um experimento aleatorizado, então falar em efeito do tratamento é mais defensável que em dado observacional — mas siga usando linguagem descritiva

**Ver:** `05-analise-bivariada.md`

---

### Q10 — Escores SAT estaduais (SATMAT.xls)
> (a) Análise unidimensional das duas variáveis (distribuição, média, dp, 5 números). (b) Análise bidimensional + interpretação.

**Cobra:** univariada + bivariada na mesma questão (formato muito provável de cair).
**Colunas reais:** `Estado`, `PctSAT`, `SAT-Mat` (⚠️ hífen no nome → use `df['SAT-Mat']`).
**Roteiro:** histograma + `describe()` de cada uma; depois dispersão + Pearson.
**Resultado conferido: r = −0,866** → negativa **forte**.
**A sacada interpretativa:** estados onde *mais* alunos fazem o SAT têm média *menor*. Não é que o SAT "piore"; é que quando poucos fazem, só os mais preparados fazem (**viés de seleção**). Esse raciocínio é o que a questão quer.

---

### Q11 — Ideb
> Identifique o Ideb do seu estado e a posição no ranking nacional.

**Cobra:** consulta a fonte oficial + leitura de indicador. Não tem código.
**Roteiro:** é questão de pesquisa (Inep/Poder360). Na prova com internet liberada, é ponto fácil — só não esqueça de **citar a fonte e o ano** do dado.

---

### Q12 — Análise de renda (InfoFamiliasEntrevistadas.csv)
> (a) Classificar renda ≤ 5 salários como "baixa" e > 5 como "alta". (b) Há associação entre renda familiar e uso de programa de alimentação popular?

**Cobra:** **criar variável qualitativa a partir de quantitativa** + tabela de dupla entrada.
**Colunas reais:** `Nº`, `Local`, `P.a.p.`, `Instr.`, `Tam.`, `Renda` (120 linhas).
**⚠️ Renomeie antes de plotar:** `P.a.p.`, `Instr.` e `Tam.` têm **ponto no nome** — o Altair interpreta ponto como campo aninhado e desenha **gráfico vazio sem dar erro**.

```python
inf = pd.read_csv('InfoFamiliasEntrevistadas.csv')
inf = inf.rename(columns={'P.a.p.': 'Pap', 'Instr.': 'Instr', 'Tam.': 'Tam', 'Nº': 'N'})
```

**Roteiro:**
- (a) `inf['faixa_renda'] = pd.cut(inf['Renda'], bins=[0, 5, float('inf')], labels=['renda baixa', 'renda alta'])`
- (b) Tabela de dupla entrada dessa nova variável × `Pap`, com **distribuição condicional na renda** + barras segmentadas normalizadas

**Resultado conferido:**

| Faixa de renda | não usa | **usa o programa** | total |
|---|---|---|---|
| renda baixa (≤ 5 SM) | 15 (27,3%) | 40 (**72,7%**) | 55 |
| renda alta (> 5 SM) | 27 (41,5%) | 38 (**58,5%**) | 65 |

**Sim, a amostra sugere associação:** entre as famílias de renda baixa, 72,7% usam o programa, contra 58,5% entre as de renda alta — 14 pontos percentuais de diferença, no sentido esperado.

**Ver:** `05-analise-bivariada.md` (seção `pd.cut`)

---

### Q13 — IDH OECD (OECD_IDH_data.csv)
> (a) Histograma do PIB. (b) Identifique o atípico. (c) Escolha 2 variáveis e faça univariada. (d) Bivariada dessas duas.

**Cobra:** o pacote completo, com **liberdade de escolha** das variáveis.
**Colunas reais:** `nation`, `GDP`, `Unemploy`, `Inequal`, `Health`, `Phys`, `C02`, `Parlia`, `FemEcon` (23 países).

**⚠️ Duas armadilhas conferidas nesta base:**
1. A coluna **`Inequal` vem como TEXTO**, porque usa a letra `'I'` como marcador de ausente. Resultado: `df.corr()` **exclui ela silenciosamente** e `describe()` mostra `unique/top/freq`. Converta antes: `oc['Inequal'] = pd.to_numeric(oc['Inequal'], errors='coerce')`
2. A coluna de CO2 se chama **`C02`** — com o número **zero**, não a letra O. É o nome real na base.

- (b) O atípico do histograma de PIB é **Luxemburgo (69.961)**.
- **Dica:** escolha variáveis que provavelmente se relacionam (ex: `Health` × `Phys`; `GDP` × `Inequal`) — assim você tem o que interpretar. Escolher duas variáveis sem relação te deixa sem assunto na hora de escrever.

---

### Q14 — Censo dos estados (Censo_estados.xlsx)
> Análises bivariadas para cada par de variáveis.

**Cobra:** bivariada em escala.
**Colunas reais:** `Territorialidades`, `Esperança de vida ao nascer 2000`, `Mortalidade infantil 2000`, `Taxa de analfabetismo - 18 anos ou mais de idade 2000`, `Renda per capita 2000`.

**⚠️ São 28 linhas, não 27 — a primeira é "Brasil"**, o agregado do país, não um estado. Misturar o agregado com as unidades é erro de unidade de análise:
```python
ce = ce[ce.Territorialidades != 'Brasil']
```

**Roteiro:** `df.corr(numeric_only=True)` dá a **matriz de correlação** de todos os pares de uma vez. Use ela para escolher os pares mais fortes e só então faça os diagramas de dispersão desses.

**Matriz conferida (sem a linha Brasil):**

| | Esp. vida | Mort. infantil | Analfabet. | Renda |
|---|---|---|---|---|
| **Esperança de vida** | 1,000 | −0,886 | −0,856 | 0,852 |
| **Mortalidade infantil** | −0,886 | 1,000 | **0,931** | −0,823 |
| **Analfabetismo** | −0,856 | 0,931 | 1,000 | −0,831 |
| **Renda per capita** | 0,852 | −0,823 | −0,831 | 1,000 |

Todos os pares são fortes; o mais forte é **mortalidade infantil × analfabetismo (0,931)**.

> Esta base é do Censo de **2000**; a prova de 2025 usou a de **2010** (e os nomes das colunas carregam o ano). A análise resolvida está em `07-prova-2025-resolvida.md`.

---

## O que essa lista revela sobre a prova

Olhando as 14 questões juntas, o padrão é claro:

| Tipo de tarefa | Quantas questões |
|---|---|
| Univariada quantitativa (histograma + medidas + atípicos) | Q4, Q6, Q7, Q10, Q13 |
| Univariada qualitativa (frequência + barras/setores) | Q2, Q3 |
| Bivariada quantitativa (dispersão + Pearson) | Q8, Q10, Q13, Q14 |
| Bivariada qualitativa (dupla entrada + condicional) | Q9, Q12 |
| Série temporal | Q5 |
| Conceitual puro (sem código) | Q1, Q2a, Q6a, Q11 |

**Conclusão prática:** domine o pacote "histograma + describe + AIQ + boxplot" e o pacote "dispersão + Pearson" — juntos eles cobrem a maioria das questões. E note que **quase toda questão termina pedindo interpretação escrita**.
