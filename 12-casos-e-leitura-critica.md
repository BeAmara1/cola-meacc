# Os casos vistos em aula + leitura crítica de gráficos

As bases usadas nas aulas práticas (`00-1-shipman...`, `01-1-child-heart...`, `02-4-sexual-partners...`, `DatasaurusDozen.tsv`) são os casos do livro **"A Arte da Estatística", de David Spiegelhalter** — a numeração dos arquivos segue capítulo-figura do livro.

Isso importa por um motivo prático: **a prova tende a usar uma base nova, mas cobrar o mesmo tipo de raciocínio dos casos**. Se você entende o que cada caso ensina, reconhece o padrão na hora.

E tem o ângulo que é a cara de Comunicação Digital: não é só calcular certo, é perceber **como a escolha de visualização muda a mensagem**.

---

## Caso 1 — Harold Shipman (o médico assassino)

**O que é:** médico britânico condenado por assassinar pacientes. A base tem, para cada vítima confirmada, idade, ano da morte, gênero e local da morte.

**O que o caso ensina:** análise puramente descritiva, bem visualizada, **revela um padrão que denuncia**. Nenhum teste estatístico sofisticado — só histograma, gráfico de barras e dispersão.

**O que você faz com essa base (e apareceu nas aulas 4, 6 e 14):**
- Univariada qualitativa: distribuição de gênero das vítimas, local da morte
- Univariada quantitativa: histograma de idade, histograma por ano da morte
- Bivariada: dispersão de ano da morte × idade, colorida por gênero, **com histogramas nas margens** (o gráfico "completo" do caso)

**A leitura:** o padrão que salta é a concentração em um perfil específico de vítima (mulheres idosas, mortes em casa). É a concentração — não a quantidade bruta — que conta a história.

**Gancho de comunicação:** aqui o gráfico funciona como **evidência**. Vale notar na resposta que a visualização tornou visível um padrão que tabelas de números não tornavam.

---

## Caso 2 — Bebês de Bristol (cirurgia cardíaca infantil)

**O que é:** taxas de sobrevivência em 30 dias em cirurgias cardíacas infantis em hospitais britânicos. O hospital de Bristol tinha resultados muito piores, o que gerou um inquérito público.

**Esse é o caso mais rico para a prova**, porque ele é uma aula inteira de manipulação de visualização. Três decisões que mudam completamente a leitura do mesmo dado:

### (a) Enquadramento positivo vs. negativo
A mesma informação pode ser apresentada como:
- **"taxa de sobrevivência de 96%"** (enquadramento positivo — soa tranquilizador)
- **"taxa de mortalidade de 4%"** (enquadramento negativo — soa alarmante)

São o mesmo número. A escolha entre eles é **editorial**, não estatística.

> **Frase-modelo:** "A escolha por apresentar a taxa de sobrevivência em vez da taxa de mortalidade adota um enquadramento positivo: matematicamente equivalente, mas com efeito muito diferente sobre quem lê."

### (b) Manipulação da escala do eixo
Nas aulas, o gráfico de sobrevivência é feito duas vezes: com o eixo começando em 0 e com o eixo limitado a `domain=(86, 100)`.

- Eixo começando em **0**: todas as barras parecem quase iguais (todas acima de 86%) → mensagem: "os hospitais são parecidos"
- Eixo começando em **86**: as diferenças viram um abismo visual → mensagem: "há hospitais muito piores"

Nenhum dos dois é "mentira" — mas **truncar o eixo exagera diferenças**. Numa questão que peça análise crítica, aponte isso.

> **Frase-modelo:** "Ao truncar o eixo horizontal (começando em 86% em vez de 0%), as diferenças entre hospitais ficam visualmente amplificadas. É uma escolha legítima para destacar variação, mas que pode exagerar a percepção da diferença real."

### (c) Ordenação das barras
Ordenar por valor (`sort='-x'`) cria um **ranking** — e ranking implica julgamento ("o pior hospital"). Manter a ordem original (alfabética, por exemplo) é uma apresentação mais neutra. É uma escolha de comunicação.

### (d) O "efeito de volume" (aula 14)
Dispersão de nº de operações × taxa de sobrevivência:
- Em **1991-95**: parece haver relação positiva (hospitais que operam mais têm melhor sobrevivência), e Bristol é o ponto discrepante claro. Retirando Bristol, a relação continua.
- Em **2012-15**: a relação praticamente some — e com poucos hospitais na base, remover **um único** ponto muda bastante o coeficiente.

**O que isso ensina:** correlação com amostra pequena é **frágil**; e relações mudam com o tempo (o que valia nos anos 90 não vale hoje).

---

## Caso 3 — Número de parceiros sexuais (dados de survey)

**O que é:** distribuição do número declarado de parceiros sexuais ao longo da vida, por gênero, a partir de pesquisa populacional.

**O que ensina — três coisas de uma vez:**

1. **Distribuição muito assimétrica à direita** → a média é péssima como resumo; a mediana descreve melhor o caso típico.
2. **Preferência por números redondos ("digit preference")**: aparecem picos em valores como 10, 20, 30, 50 no histograma. As pessoas não contam — **estimam e arredondam**. Isso é um artefato de coleta, não um fato sobre a realidade.
3. **Viés de resposta (social desirability bias)**: quando se compara a declaração de homens e mulheres, costuma haver discrepância. Como é dado **autodeclarado** sobre tema sensível, a diferença pode refletir tanto comportamento real quanto **disposição diferente a relatar**.

> **Frase-modelo:** "Os picos em números redondos sugerem que os respondentes estimaram em vez de contar, o que é uma característica do instrumento de coleta e não da população. Além disso, por ser dado autodeclarado sobre tema sensível, parte da diferença observada pode vir de viés de resposta."

**Detalhe técnico dessa base:** ela vem **agregada** (uma linha por número de parceiros, com a contagem de pessoas). Para calcular média/mediana você precisa "desagregar" repetindo cada linha pela contagem — foi o que o `reindex(...index.repeat(...))` fez na aula 11.

---

## Caso 4 — Datasaurus Dozen

**O que é:** 13 conjuntos de dados fictícios (um deles desenha um dinossauro) com **estatísticas-resumo praticamente idênticas** — mesma média, mesmo desvio padrão, mesma correlação — e formatos completamente diferentes.

**O que ensina — a lição mais importante do semestre em uma frase:**

> **Sempre plote os dados. Estatística-resumo não captura a forma.**

Serve como argumento pronto sempre que uma questão te der um coeficiente de correlação baixo: **r ≈ 0 não significa "não há relação"**, significa "não há relação **linear**".

> **Frase-modelo:** "Como mostra o exemplo do Datasaurus, conjuntos com a mesma média, desvio padrão e correlação podem ter formatos radicalmente diferentes. Por isso o coeficiente de Pearson precisa sempre ser lido junto com o diagrama de dispersão."

---

## Caso 5 — Séries de menções em redes sociais

Base de evolução temporal de menções a um tema no X e no Facebook, inclusive segmentada por categoria (menções associadas a Lula e a Bolsonaro).

**O que ensina:**
- Dados de redes vêm em granularidade fina (por hora) e quase sempre precisam de **agregação** (`resample`) para a série virar legível
- A escolha da agregação é interpretativa: **soma** por dia responde "volume total"; **média** responde "intensidade típica"
- Comparar séries: **sobreposição** (tudo no mesmo eixo, bom para comparar magnitude) vs **facetamento** (um painel por categoria, bom quando as escalas são muito diferentes)

---

## Checklist de leitura crítica (para qualquer gráfico da prova)

- [ ] O **eixo começa em zero**? Se não, as diferenças estão amplificadas — vale comentar
- [ ] É contagem ou percentual? Comparar grupos de tamanhos diferentes exige **percentual**
- [ ] O enquadramento é positivo ou negativo (sobrevivência vs mortalidade)? Existe o complementar?
- [ ] A ordenação cria um ranking/julgamento?
- [ ] O tamanho das classes (bins) do histograma muda a leitura? (bin muito pequeno vira ruído, muito grande esconde o padrão)
- [ ] Tem valor atípico puxando média/correlação?
- [ ] O dado é autodeclarado? Pode ter viés de resposta
- [ ] É amostra ou população? Dá pra generalizar?
