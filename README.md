# cola-meacc

Repositório de consulta para **Métodos Estatísticos Aplicados às Ciências Sociais** (Comunicação Digital, FGV — Profa. Polyana Barboza), para copiar e colar durante a prova (consulta a materiais de aula é permitida; a materiais de colegas e a LLMs, não — por isso esse repositório é preparado *antes* da prova).

Baseado nas aulas práticas do [repositório oficial da matéria](https://github.com/PolyanaSRB/MetodosEstatisticos_26.2) e na prova A1 de 2025.2 (com gabarito).

## Como usar na prova

1. Identifique o **tipo de questão** (ver `00-fluxograma-o-que-fazer.md`).
2. Vá direto ao arquivo do tópico correspondente e copie o snippet.
3. Adapte nomes de coluna/base para o seu dado.
4. **Sempre interprete o resultado** — a professora cobra isso em toda questão. Use os modelos de frase em `08-frases-de-interpretacao.md`.

## Índice

| Arquivo | Conteúdo |
|---|---|
| `00-fluxograma-o-que-fazer.md` | Fluxograma rápido: qual técnica/gráfico usar para cada tipo de variável/pergunta |
| `01-tipos-de-variaveis.md` | Classificação de variáveis (qualitativa/quantitativa, nominal/ordinal, discreta/contínua) |
| `02-analise-univariada-qualitativa.md` | Tabela de frequência, gráfico de barras e de setores (quando cada um vale) |
| `03-histogramas-e-series-temporais.md` | Histograma (bins), interpretação de forma/centro/dispersão/atípicos, séries temporais, `resample`, facetamento, sobreposição |
| `04-medidas-descritivas.md` | Média, mediana, moda, desvio padrão, quartis, AIQ, regra 1.5×AIQ, boxplot, `describe()` |
| `05-analise-bivariada.md` | Tabela de dupla entrada, distribuição condicional, correlação de Pearson, diagrama de dispersão, gráficos segmentados |
| `06-snippets-prontos.py` | Todos os snippets acima em um único arquivo Python, prontos para copiar |
| `07-prova-2025-resolvida.md` | Prova A1 de 2025.2 com gabarito completo (questões 1 a 3) |
| `08-frases-de-interpretacao.md` | Banco de frases para interpretar resultados (a professora sempre pede interpretação) |
| `09-teoria-analise-bivariada.md` | **Teoria** por trás da análise bivariada — o que cada técnica realmente significa, armadilhas (causalidade, não-linearidade, atípicos), e como estruturar a resposta escrita. Leia esse **antes** da prova se bivariada é seu ponto fraco. |
| `10-corretor-de-codigo-altair.py` + `10-como-usar-o-corretor.md` | **Ferramenta sem IA** (só regras) pra rodar no Colab durante a prova: pega seu código Altair que não funciona, roda de verdade, e diagnostica o erro — parêntese faltando, typo, coluna que não existe na base — tentando autocorrigir os casos bobos. |

## Se a teoria (não só o código) é seu ponto fraco

`09-teoria-analise-bivariada.md` foi feito justamente pra isso: ele explica o "porquê" de cada técnica de bivariada (tabela de dupla entrada, correlação de Pearson, boxplots comparativos), lista as armadilhas mais cobradas (correlação ≠ causalidade, Pearson só pega relação linear, sensibilidade a atípicos) e dá um roteiro de como estruturar a resposta escrita — pra você não travar na hora de redigir a interpretação.

## Setup rápido (Colab)

```python
import pandas as pd
import altair as alt
alt.data_transformers.disable_max_rows()  # evita erro em bases > 5000 linhas

folder = '/content/drive/MyDrive/Academico/Métodos Estatísticos/2026/Prova'
```
