# Erros que travam a prova (e a solução de cada um)

Todos os casos abaixo foram **testados de verdade**, não são chute. Procure pela mensagem de erro que apareceu na sua tela.

---

## 🔴 Os 3 erros SILENCIOSOS (não dão mensagem — e são os piores)

Esses não quebram nada: o código roda, mas o resultado está errado. Se algo parecer estranho, cheque esses três primeiro.

### 1. Coluna com PONTO no nome → gráfico sai vazio

Se a coluna se chama `P.a.p.` (é o caso do arquivo `InfoFamiliasEntrevistadas.csv`), o Altair interpreta o ponto como "campo aninhado" e **desenha um gráfico vazio, sem reclamar**.

```python
# ❌ gráfico vazio, sem erro nenhum
alt.Chart(df).mark_bar().encode(x='P.a.p.:N', y='count()')

# ✅ solução mais simples: renomeie a coluna
df = df.rename(columns={'P.a.p.': 'Pap'})
alt.Chart(df).mark_bar().encode(x='Pap:N', y='count()')

# ✅ alternativa: escapar os pontos com \.  (note o r'' antes da string)
alt.Chart(df).mark_bar().encode(x=alt.X(r'P\.a\.p\.:N'), y='count()')
```

**Regra geral:** se o nome da coluna tem `.` ou `[`, renomeie antes de plotar. Espaço e acento são ok.

### 2. Número que virou texto (por causa da vírgula decimal)

CSV brasileiro costuma usar vírgula como decimal (`1,5`). Sem avisar o pandas, a coluna vira **texto** e os cálculos ficam errados ou impossíveis.

**Como detectar:** rode `df.describe()`. Se aparecer `unique / top / freq` em vez de `mean / std / min / max`, sua coluna é texto, não número.

```python
df.dtypes            # 'object' ou 'str' = texto; 'int64'/'float64' = número

# ✅ solução na leitura:
df = pd.read_csv('arquivo.csv', sep=';', decimal=',')

# ✅ ou consertando depois:
df['coluna'] = df['coluna'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)
```

### 3. Coluna referenciada que não existe → gráfico vazio

O Altair **não dá erro** se você errar o nome da coluna — só desenha nada. Cheque com `df.columns` ou use o corretor (`10-corretor-de-codigo-altair.py`), que foi feito exatamente pra pegar isso.

---

## 🟠 Erros na hora de LER o arquivo

### `FileNotFoundError: No such file or directory`

```python
import os
os.listdir('/content/drive/MyDrive/caminho/da/pasta')   # veja o nome EXATO
```
- No Colab (Linux), **maiúscula/minúscula importa**: `Censo.csv` ≠ `censo.csv`
- Acento e espaço no nome também contam
- Montou o Drive?
```python
from google.colab import drive
drive.mount('/content/drive')
```

### Tudo veio numa coluna só (`df.shape` mostra 1 coluna)

Separador errado. CSV brasileiro/europeu usa `;`:
```python
df = pd.read_csv('arquivo.csv', sep=';')
```
Os arquivos da prova de 2025 (ENEM e INMET) **usavam `sep=';'`**.

### `Missing optional dependency 'xlrd'` (ao abrir .xls)

Os arquivos do livro são `.xls` (formato antigo), que precisa da biblioteca `xlrd`:
```python
!pip install xlrd
```
Já `.xlsx` usa `openpyxl` (normalmente já vem instalado no Colab).

### `UnicodeDecodeError` (acentos quebrados ou erro na leitura)

Arquivo salvo no padrão do Windows:
```python
df = pd.read_csv('arquivo.csv', sep=';', encoding='latin-1')   # ou encoding='cp1252'
```

### Combo completo para arquivo brasileiro problemático

```python
df = pd.read_csv('arquivo.csv', sep=';', decimal=',', thousands='.', encoding='latin-1')
```

---

## 🟠 Erros do Altair

### `MaxRowsError: The number of rows in your dataset (X) is greater than the maximum allowed (5000)`

Clássico com base grande (microdados do ENEM, por exemplo). Uma linha resolve:
```python
alt.data_transformers.disable_max_rows()
```
Coloque isso **na primeira célula**, junto dos imports, e nunca mais pense nisso.

### `SchemaValidationError: 'None' is an invalid value for 'extent'`

Você passou um parâmetro como `None`. Em vez de `alt.Bin(step=5, extent=None)`, passe só `alt.Bin(step=5)`.

### O gráfico não aparece (célula roda e não mostra nada)

O objeto do gráfico precisa ser a **última linha** da célula (sem `print`). Se estiver no meio do código, use `.display()`:
```python
grafico = alt.Chart(df).mark_bar().encode(x='cat:N', y='count()')
grafico.display()
```

---

## 🟠 Erros do pandas

### `ValueError: 'M' is no longer supported for offsets. Please use 'ME' instead.`

Mudança de versão do pandas. No `resample`: mês virou `'ME'`, ano virou `'YE'`, trimestre `'QE'`. O gabarito de 2025 usa a escrita antiga.
```python
df.set_index('data').resample('ME').valor.mean()
```

### `ValueError: value_name (X) cannot match an element in the DataFrame columns`

No `melt`, o `value_name`/`var_name` não pode ser igual a uma coluna que já existe. Use nomes diferentes (`'Value'`, `'Category'`).

### `ValueError: cannot set a row with mismatched columns`

Você fez `df.loc[len(df)] = ['Outras', 12.3]` mas o df tem mais de 2 colunas. Use a versão com `pd.concat` (está em `02-analise-univariada-qualitativa.md`).

### `KeyError: 'nome da coluna'` mesmo o nome parecendo certo

Provavelmente tem **espaço invisível** no fim do nome:
```python
list(df.columns)                       # olhe com atenção: 'Renda ' tem espaço no fim
df.columns = df.columns.str.strip()    # remove espaços das pontas de todos os nomes
```

### `SettingWithCopyWarning`

É **aviso**, não erro — pode ignorar na prova. Se quiser resolver, use `.copy()` ao criar um recorte:
```python
recorte = df[df.valor > 10].copy()
```

---

## 🩺 Célula de diagnóstico rápido

Quando algo estiver estranho e você não souber o quê, rode isso na base:

```python
print('formato (linhas, colunas):', df.shape)
print()
print('colunas:', list(df.columns))
print()
print('tipos:')
print(df.dtypes)
print()
print('valores ausentes por coluna:')
print(df.isna().sum())
print()
df.head()
```

Isso responde de uma vez: o separador estava certo? os nomes das colunas são esses mesmo? os números são números ou texto? tem dado faltando?
