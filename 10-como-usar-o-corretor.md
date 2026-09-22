# Como usar o corretor de código Altair (`10-corretor-de-codigo-altair.py`)

Ferramenta **sem IA** — é só código Python com regras (regex, `try/except`, comparação de strings). Roda 100% offline no Colab, então pode usar na prova.

## O que ela pega

- **Parênteses/colchetes/chaves desbalanceados** — e tenta fechar sozinha
- **Typos comuns** — `alt.Chat` → `alt.Chart`, `.encod(` → `.encode(`, `mark_bat(` → `mark_bar(`, etc. — e tenta corrigir sozinha
- **Nome de método que não existe no Altair** (ex: `alt.Bra` em vez de `alt.Bar`) — sugere o nome certo
- **Nome de coluna que não existe na sua base** — o Altair **não avisa isso sozinho** (só desenha um gráfico vazio!), então essa é a checagem mais importante da ferramenta
- Dicas genéricas pra `TypeError` e `ValueError` comuns em Altair

## O que ela **não** pega (limitação, sendo honesto)

- Erros de **lógica** (código roda, mas o gráfico não é o que você queria — ex: usar `mark_bar` quando devia ser `mark_line`)
- Typos em nomes de coluna que **coincidem** com outra coluna real (não tem como saber qual você queria)
- Problemas de **interpretação estatística** (isso não é um corretor de estatística, só de sintaxe/código)

## Como usar

1. Na célula do Colab, cole o conteúdo de `10-corretor-de-codigo-altair.py` inteiro (as funções).
2. Numa célula abaixo, chame `checar()` passando seu código **como string** (entre `'''` três aspas) e sua base de dados de verdade:

```python
meu_codigo = '''
alt.Chart(df).mark_bar().encode(
    x="TP_COR_RAC:N",
    y="count()"
'''

checar(meu_codigo, df=enem)   # troque "enem" pela sua base de verdade
```

**Importante:** dentro da string `meu_codigo`, a base sempre precisa se chamar `df` (é o nome que a função usa internamente) — mesmo que sua base real se chame `enem`, `censo_estados` etc. Só troque o nome pra `df` na hora de colar dentro da string, ou passe seu código já com esse nome desde o início.

3. Leia o diagnóstico. Se ela autocorrigiu algo (parêntese, typo), ela te mostra o código já corrigido pra você copiar de volta pro seu notebook de verdade.

## Exemplo completo

```python
minha_base = pd.read_excel('arquivo.xls')

codigo_com_erro = '''
alt.Chart(df).mark_bar().encode(
    x="Categoria:N",
    y="valor:Q"
'''  # esqueci de fechar o parêntese

checar(codigo_com_erro, df=minha_base)
```

Saída esperada: ela fecha o parêntese sozinha, roda, e ainda avisa se `"Categoria"` (com C maiúsculo) não bater com o nome real da coluna na sua base.
