# Checklist de conceitos — a lista da própria professora

Este é o conteúdo do arquivo **`Revisão Conceitos.docx`**, que a professora publicou junto com a Aula 15 e **deletou do repositório no mesmo dia (17/09/2026)**. Recuperado do histórico do git (commit `b1b38d0`).

Vale mais que qualquer resumo meu: **é o escopo da prova, escrito por quem faz a prova.** Use como checklist final de estudo — se você consegue explicar cada linha, está pronto.

Abaixo está a lista original, com a indicação de onde cada item está coberto neste repositório.

---

## Dados
- [ ] **Do conceito à variável** — como uma ideia abstrata ("felicidade", "desenvolvimento") vira uma variável medível → `11-conceitos-fundamentais.md`
- [ ] **Indivíduos** — as unidades sobre as quais os dados são coletados (é o termo do livro para unidade de análise) → `11-conceitos-fundamentais.md` §1
- [ ] **Tipos de variáveis** → `01-tipos-de-variaveis.md`

## Variáveis qualitativas
- [ ] **Distribuição de frequências** → `11-conceitos-fundamentais.md` §4
- [ ] **Gráfico de barras** → `02-analise-univariada-qualitativa.md`
- [ ] **Gráfico de setores** (e quando NÃO usar) → `02-analise-univariada-qualitativa.md`

## Variáveis quantitativas
- [ ] **Distribuição de frequências**
- [ ] **Histograma** → `03-histogramas-e-series-temporais.md`
- [ ] **Interpretação a partir do padrão geral (centro, variabilidade e forma) e desvio** → `03` e `11` §8

> 📌 Note a fórmula da professora: **padrão geral + desvio**. "Padrão geral" = centro, variabilidade e forma. "Desvio" = o que foge disso (valores atípicos). Use esse vocabulário na resposta.

## Séries temporais
- [ ] **Interpretação a partir do padrão geral (ciclos ou tendências) e desvio (picos)** → `03-histogramas-e-series-temporais.md`

> 📌 Aqui o "padrão geral" são **ciclos ou tendências**, e o "desvio" são os **picos**.

## Medidas centrais de resumo
*(para cada uma: definição, exemplos, interpretação e propriedades)*
- [ ] **Média** → `04-medidas-descritivas.md`
- [ ] **Moda** → `04`
- [ ] **Mediana** → `04`
- [ ] **Comparação entre média e mediana** → `00-fluxograma` e `11` §9
- [ ] **Medida ideal para cada tipo de distribuição** → `04` e `11` §7

## Variabilidade
- [ ] **Quartis, valores atípicos e boxplot** → `04-medidas-descritivas.md`
- [ ] **Q1, Q3, AIQ** → `04`
- [ ] **Resumo dos cinco números** → `04`
- [ ] **Simetria e assimetria** → `11` §9
- [ ] **Boxplot** → `04`
- [ ] **Regra 1,5×AIQ** → `04`
- [ ] **Desvio médio, variância e desvio padrão** (definição, exemplos, interpretação e **propriedades**) → `04` (seção "As três medidas de dispersão")
- [ ] **Escolha de medidas de centro e de variabilidade** → `04` e `11` §7

## Indicadores
- [ ] **Indicadores** → `11-conceitos-fundamentais.md` §10

## Análise bivariada (gráficos e busca de padrões e desvios)
- [ ] **Variável resposta e explicativa** → `11` §5
- [ ] **Uma variável quantitativa e uma qualitativa** → `05-analise-bivariada.md` (boxplots comparativos)
- [ ] **Duas variáveis qualitativas**
  - [ ] Tabela de dupla entrada e gráfico de barras segmentadas → `05`
  - [ ] **Distribuição marginal e condicional** → `05` (seção "Marginal vs condicional")
- [ ] **Duas variáveis quantitativas**
  - [ ] Diagrama de dispersão → `05`
  - [ ] **Interpretação a partir do padrão geral (direção, forma e intensidade) e desvio** → `05` e `09`
  - [ ] **Inclusão de variável qualitativa** (colorir os pontos por categoria) → `05`
- [ ] **Coeficiente de Pearson** (definição, exemplos, interpretação, propriedades, **cuidados**) → `09-teoria-analise-bivariada.md`

---

## O que essa lista revela

**1. "Padrão geral e desvio" é a estrutura de resposta que ela quer.** Aparece três vezes na lista (histograma, série temporal, dispersão). Em cada contexto:

| Análise | Padrão geral | Desvio |
|---|---|---|
| Histograma | centro, variabilidade, **forma** | valores atípicos |
| Série temporal | ciclos ou tendências | picos, quebras |
| Dispersão | direção, **forma**, intensidade | pontos fora da nuvem |

**2. Ela pede "propriedades", não só cálculo.** Aparece em medidas centrais, em desvio padrão e em Pearson. Saber calcular não basta — tem que saber o que a medida faz (é resistente? muda se eu somar 10 a todos os valores? pode ser negativa?).

**3. Note o que NÃO está na lista:** nada de inferência, teste de hipótese, p-valor, intervalo de confiança ou regressão. A prova é **100% estatística descritiva**. Não invente linguagem inferencial na resposta.

**4. "Forma" aparece na dispersão.** Muita gente descreve dispersão só com direção e força e esquece a forma (linear ou curva) — que é exatamente o que separa quem entendeu o Datasaurus de quem não entendeu.
