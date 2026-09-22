# cola-meacc

Material de consulta para **Métodos Estatísticos Aplicados às Ciências Sociais** (Comunicação Digital, FGV — Profa. Polyana Barboza).

Serve para duas coisas: **estudar antes** (a teoria que não está nos notebooks) e **consultar durante a prova** (código pronto para copiar e colar).

A prova permite consulta a materiais de aula, anotações e internet — e proíbe consulta a colegas e a modelos de linguagem. Por isso tudo aqui é preparado **antes**, e as ferramentas do repositório rodam offline, sem IA.

Baseado nas aulas práticas do [repositório oficial da matéria](https://github.com/PolyanaSRB/MetodosEstatisticos_26.2), na prova A1 de 2025.2 com gabarito e na lista de revisão da Aula 15.

---

## Começando

**Para estudar (na ordem):**

1. `11-conceitos-fundamentais.md` — o vocabulário que sustenta tudo (unidade de análise, amostra, resistência, assimetria)
2. `01-tipos-de-variaveis.md` — classificar variáveis, que é o primeiro passo de toda questão
3. `09-teoria-analise-bivariada.md` — a teoria de bivariada, com as armadilhas mais cobradas
4. `12-casos-e-leitura-critica.md` — os casos vistos em aula e o olhar crítico sobre gráficos
5. `13-lista-de-revisao-resolvida.md` — as 14 questões de revisão com o roteiro de cada uma
6. `07-prova-2025-resolvida.md` — a prova do ano passado, resolvida e comentada

**Para a prova (deixe aberto):**

- `prova-template.ipynb` — abra direto no Colab; tem uma célula pronta para cada tipo de análise
- `00-fluxograma-o-que-fazer.md` — para decidir rápido qual técnica usar
- `08-frases-de-interpretacao.md` — para escrever a interpretação sem travar
- `14-erros-e-travadas-no-colab.md` — quando algo der erro

---

## Índice completo

### Teoria (o "porquê")
| Arquivo | Conteúdo |
|---|---|
| `11-conceitos-fundamentais.md` | Unidade de análise, população vs amostra, representatividade e viés, distribuição de frequência, variável explicativa vs resposta, resistência de medidas, como descrever uma distribuição |
| `01-tipos-de-variaveis.md` | Qualitativa (nominal/ordinal) vs quantitativa (discreta/contínua) e por que isso define tudo |
| `09-teoria-analise-bivariada.md` | O que cada técnica de bivariada significa; correlação ≠ causalidade; Pearson só mede relação linear; sensibilidade a atípicos; como estruturar a resposta escrita |
| `12-casos-e-leitura-critica.md` | Shipman, bebês de Bristol, parceiros sexuais, Datasaurus — o que cada caso ensina + enquadramento positivo/negativo, manipulação de escala de eixo, checklist de leitura crítica |

### Código (o "como")
| Arquivo | Conteúdo |
|---|---|
| `00-fluxograma-o-que-fazer.md` | Decisão rápida: qual técnica e qual gráfico para cada tipo de questão |
| `02-analise-univariada-qualitativa.md` | Tabela de frequência, barras, setores, checagem de consistência de percentuais |
| `03-histogramas-e-series-temporais.md` | Histograma e bins, interpretação de forma/centro/dispersão/atípicos, séries temporais, `resample`, facetamento, sobreposição |
| `04-medidas-descritivas.md` | Média, mediana, moda, desvio padrão, quartis, AIQ, regra 1,5×AIQ, boxplot, boxplots comparativos |
| `05-analise-bivariada.md` | Tabela de dupla entrada, distribuição condicional, barras segmentadas, dispersão, Pearson, `pd.cut` |
| `06-snippets-prontos.py` | Tudo acima como funções prontas, num arquivo só |
| `prova-template.ipynb` | **Notebook do Colab** com uma célula pronta por tipo de análise (roda de cara, com dados de exemplo) |

### Prática
| Arquivo | Conteúdo |
|---|---|
| `07-prova-2025-resolvida.md` | Prova A1 de 2025.2 (ENEM, série do INMET, PNAD/Censo) com gabarito comentado |
| `13-lista-de-revisao-resolvida.md` | As 14 questões da Aula 15 com o roteiro de ataque de cada uma + o que elas revelam sobre o formato da prova |
| `08-frases-de-interpretacao.md` | Banco de frases prontas para interpretar cada tipo de resultado |

### Ferramentas (sem IA, rodam offline)
| Arquivo | Conteúdo |
|---|---|
| `10-corretor-de-codigo-altair.py` | Pega seu código Altair que não funciona, roda de verdade e diagnostica: parêntese faltando, typo, coluna inexistente, nome de arquivo errado. Autocorrige os casos bobos. Guia em `10-como-usar-o-corretor.md` |
| `14-erros-e-travadas-no-colab.md` | Catálogo de erros (`sep=';'`, `decimal=','`, `xlrd`, `MaxRowsError`, `resample('M')`) e os 3 erros **silenciosos** que não dão mensagem |
| `99-testar-a-cola.py` | Roda todo o código do repositório e avisa o que quebrou na versão de biblioteca do dia |

---

## Usar no Colab

```python
!git clone https://github.com/BeAmara1/cola-meacc.git
%cd cola-meacc
!python 99-testar-a-cola.py      # confirma que tudo funciona na versão de hoje
```

Depois é só abrir o `prova-template.ipynb` no Colab e trabalhar a partir dele.

Setup mínimo de qualquer notebook:

```python
import pandas as pd
import altair as alt
alt.data_transformers.disable_max_rows()   # sem isso, base grande dá MaxRowsError
```

---

## Os primeiros 5 minutos da prova

1. Rodar o setup e **montar o Drive**
2. Listar a pasta (`os.listdir(PASTA)`) para pegar o **nome exato** dos arquivos
3. Ler a base e rodar a **célula de diagnóstico** (`df.shape`, `df.columns`, `df.dtypes`, `df.isna().sum()`)
4. Conferir três coisas antes de qualquer análise:
   - Os números vieram como número mesmo? (se `describe()` mostra `unique/top/freq`, veio como texto → `decimal=','`)
   - Algum nome de coluna tem **ponto**? Renomeie, senão o gráfico sai vazio
   - Quantos valores ausentes existem?
5. Só então ler a primeira questão e ir para a seção correspondente

---

## As 6 coisas que mais custam ponto

1. **Não interpretar.** Toda questão pede análise escrita — gráfico sozinho não fecha a resposta.
2. Descrever distribuição sem os 4 itens: **forma → centro → dispersão → atípicos**.
3. Comparar grupos de tamanhos diferentes usando **contagem** em vez de **percentual**.
4. Afirmar **causalidade** a partir de correlação.
5. Confiar no coeficiente de Pearson **sem olhar o diagrama de dispersão** (lembre do Datasaurus).
6. Esquecer de checar **valores atípicos** pela regra 1,5×AIQ e o efeito deles nas medidas.
