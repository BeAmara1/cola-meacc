# Lista de revisão (Aula 15) — com o roteiro de ataque de cada questão

As 14 questões da aula de revisão da professora (`aulas_praticas/15-revisao/Revisão.ipynb`), cada uma com **o que a questão está cobrando** e **o caminho para responder**. Como a lista de revisão costuma antecipar o formato da prova, vale usar isso como mapa de estudo.

Os arquivos de dados de cada questão estão na pasta `15-revisao/` do repositório da matéria.

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
**Roteiro:**
- (a) **Os estudantes** — a tabela está agregada por área, mas quem gerou o dado foi cada calouro. (Ver `11-conceitos-fundamentais.md` §1.)
- (b) `df.Percent.sum()` → tem que dar 100. Se não der, é arredondamento ou falta a categoria "Outras".
- (c) Barras ordenadas (`sort='-y'`). Setores só se somar 100% e houver poucas categorias.

**Ver:** `02-analise-univariada-qualitativa.md`

---

### Q3 — "Você ouve rádio?" (FORMATORADIO.xls)
> (a) Soma dos níveis de audiência; qual % ouve outros formatos. (b) Seria correto usar gráfico de setores? (c) Barras incluindo "Outro formato".

**Cobra:** exatamente a pegadinha do gráfico de setores.
**Roteiro:**
- (a) `df.Percentage.sum()` e depois `100 - soma` = o que sobra para "Outros".
- (b) **Não, não do jeito que está** — setores exige partes de um todo (soma 100%). Como a tabela só traz os formatos mais populares, falta a fatia "Outros". *Depois* de acrescentar "Outro formato", aí sim somaria 100% e o setor seria defensável (ainda assim, barras comunicam melhor com muitas categorias).
- (c) Acrescente a linha "Outras" e plote barras.

**Ver:** `02-analise-univariada-qualitativa.md`

---

### Q4 — Nascidos fora (NASCIDOSFORA.xls)
> (a) Histograma com classes de 5% começando em 0. (b) Resumo dos 5 números. (c) Califórnia é atípico ou só o maior valor? Regra 1,5×AIQ.

**Cobra:** histograma com bin controlado + resumo dos 5 números + regra do atípico.
**Roteiro:**
- (a) `bin=alt.Bin(step=5, extent=[0, 30])`
- (b) Resumo dos 5 números = **mín, Q1, mediana, Q3, máx** → sai do `describe()`
- (c) Calcule `AIQ = Q3 - Q1`, depois `Q3 + 1.5*AIQ`. Se 27,2 (Califórnia) estiver acima desse limite → atípico; se não, é **só a maior observação**. Escreva a conta na resposta.

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
**Roteiro:**
- (a) Porque **total confunde tamanho populacional com intensidade de emissão** — China e Índia emitem muito no total por terem muita gente. Per capita permite comparar países de tamanhos diferentes (mesma lógica de usar percentual em vez de contagem).
- (b) Assimétrica à direita, unimodal
- (c) Qatar é o caso extremo clássico dessa base — confirme pela regra 1,5×AIQ
- (d) Média > mediana **porque** a cauda à direita (poucos países com emissão altíssima) puxa a média, e a média não é resistente

---

### Q7 — Tempo de viagem CN × NY (TEMPOVIAGEMCN.xls, TEMPOVIAGEMNY.xls)
> Análise completa: média, moda, mediana, quartis, boxplot, atípicos + comparação entre as duas bases.

**Cobra:** a questão "kitchen sink" de medidas descritivas + comparação de grupos.
**Roteiro:**
1. `describe()` nas duas
2. Moda via `value_counts()` (atenção: pode ser **plurimodal**)
3. AIQ e regra 1,5×AIQ em cada uma
4. **Junte as duas bases** (`concat` com uma coluna de origem) e faça **boxplots lado a lado** — é isso que permite a comparação
5. Interprete: quem tem mediana maior, quem tem mais dispersão, quem tem atípico

**Ver:** `04-medidas-descritivas.md` (seção de boxplots lado a lado)

---

### Q8 — Estados felizes (FELICIDADE.xls)
> (a) Dispersão de BRFSS (resposta) contra posto (explicativa). (b) Associação positiva ou negativa? (c) Concordância entre medida subjetiva e objetiva? (d) Atípicos?

**Cobra:** bivariada quantitativa + **atenção à direção da escala**.
**Roteiro:**
- (a) Explicativa (posto) no **x**, resposta (BRFSS) no **y** — a questão diz explicitamente
- (b) Calcule Pearson e olhe o gráfico
- (c) ⚠️ **Pegadinha**: no enunciado, *menores* escores BRFSS indicam **maior** felicidade, e posto 1 é o **mais feliz**. Ou seja, as duas escalas são "invertidas" em relação à intuição. Uma associação **positiva** aqui significa **concordância** entre as medidas. Leia a direção das escalas antes de concluir.
- (d) Pontos fora da nuvem; nomeie o estado

**Ver:** `05-analise-bivariada.md` e `09-teoria-analise-bivariada.md`

---

### Q9 — Parar de fumar (CESSAFUMO.xls)
> Tabela de dupla entrada de tratamento (Chantix / bupropiona / placebo) × parou de fumar. "Como isso depende do tratamento recebido?"

**Cobra:** bivariada qualitativa × qualitativa com **distribuição condicional**.
**Roteiro:**
- Os grupos têm **tamanhos diferentes** (352, 329, 344) → comparar contagem bruta é errado, **use percentual**
- A variável explicativa é o **tratamento** → condicione nele: dentro de cada tratamento, qual % parou de fumar
- Gráfico: barras segmentadas com `stack="normalize"`
- Conclua comparando os percentuais entre os três grupos
- ⚠️ Aqui **é** um experimento aleatorizado, então falar em efeito do tratamento é mais defensável que em dado observacional — mas siga usando linguagem descritiva

**Ver:** `05-analise-bivariada.md`

---

### Q10 — Escores SAT estaduais (SATMAT.xls)
> (a) Análise unidimensional das duas variáveis (distribuição, média, dp, 5 números). (b) Análise bidimensional + interpretação.

**Cobra:** univariada + bivariada na mesma questão (formato muito provável de cair).
**Roteiro:** histograma + `describe()` de cada uma; depois dispersão + Pearson.
**A sacada interpretativa:** a relação costuma ser **negativa** — estados onde *mais* alunos fazem o SAT têm média *menor*. Não é que o SAT "piore"; é que quando poucos fazem, só os mais preparados fazem (**viés de seleção**). Esse raciocínio é o que a questão quer.

---

### Q11 — Ideb
> Identifique o Ideb do seu estado e a posição no ranking nacional.

**Cobra:** consulta a fonte oficial + leitura de indicador. Não tem código.
**Roteiro:** é questão de pesquisa (Inep/Poder360). Na prova com internet liberada, é ponto fácil — só não esqueça de **citar a fonte e o ano** do dado.

---

### Q12 — Análise de renda (InfoFamiliasEntrevistadas.csv)
> (a) Classificar renda ≤ 5 salários como "baixa" e > 5 como "alta". (b) Há associação entre renda familiar e uso de programa de alimentação popular?

**Cobra:** **criar variável qualitativa a partir de quantitativa** + tabela de dupla entrada.
**Roteiro:**
- (a) `pd.cut(df['Renda'], bins=[0, 5, float('inf')], labels=['renda baixa', 'renda alta'])`
- (b) Tabela de dupla entrada dessa nova variável × `P.a.p.`, com **distribuição condicional na renda** (dentro de cada faixa de renda, qual % usa o programa) + barras segmentadas normalizadas

**Ver:** `05-analise-bivariada.md` (seção `pd.cut`)

---

### Q13 — IDH OECD (OECD_IDH_data.csv)
> (a) Histograma do PIB. (b) Identifique o atípico. (c) Escolha 2 variáveis e faça univariada. (d) Bivariada dessas duas.

**Cobra:** o pacote completo, com **liberdade de escolha** das variáveis.
**Dica de prova:** escolha variáveis que provavelmente se relacionam (ex: gasto público em saúde × médicos por 100 mil; PIB × desigualdade) — assim você tem o que interpretar. Escolher duas variáveis sem relação nenhuma te deixa sem assunto na hora de escrever.

---

### Q14 — Censo dos estados (Censo_estados.xlsx)
> Análises bivariadas para cada par de variáveis.

**Cobra:** bivariada em escala.
**Roteiro:** `df.corr(numeric_only=True)` dá a **matriz de correlação** de todos os pares de uma vez. Use ela para escolher os pares mais fortes e só então faça os diagramas de dispersão desses. Interprete direção e força de cada um.

> Essa base é praticamente a mesma da **Questão 3 da prova de 2025** — vale conferir `07-prova-2025-resolvida.md`, que tem essa análise já resolvida com interpretação.

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
