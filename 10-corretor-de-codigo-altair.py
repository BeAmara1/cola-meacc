# =====================================================================
# CORRETOR DE CÓDIGO ALTAIR — sem IA, só regras (roda no Colab)
# -----------------------------------------------------------------------
# Pra que serve: você escreveu um gráfico em Altair na prova, deu erro,
# e você não sabe o que está errado. Cole seu código (como string) na
# função `checar()` e ela roda de verdade, pega o erro do Python, e
# tenta te dizer EXATAMENTE o que consertar — parêntese faltando, nome
# errado de método do Altair, coluna que não existe na base, etc.
# Também tenta autocorrigir os erros mais bobos sozinha (parêntese
# faltando, typos comuns) e te mostra o código corrigido.
#
# Como usar (cole isso tudo numa célula do Colab, depois numa célula
# abaixo rode):
#
#   meu_codigo = '''
#   alt.Chart(df).mark_bar().encode(
#       x="categoria:N",
#       y="valor:Q"
#   '''
#   checar(meu_codigo, df=minha_base)
#
# Se sua base já se chama diferente de "df" no código, passe ela em
# `df=` mesmo assim — a função substitui o nome da variável do seu
# código pela base real na hora de testar.
# =====================================================================

import ast
import re
import difflib
import pandas as pd
import altair as alt

# --- vocabulário válido do Altair, pra sugerir correções de nome ---
_MARKS_VALIDOS = [m for m in dir(alt.Chart) if m.startswith('mark_')]
_TOPO_ALTAIR = [n for n in dir(alt) if not n.startswith('_')]
_CANAIS_VALIDOS = [
    'x', 'y', 'x2', 'y2', 'xError', 'yError', 'color', 'opacity', 'size',
    'shape', 'tooltip', 'theta', 'theta2', 'radius', 'radius2', 'text',
    'column', 'row', 'facet', 'order', 'detail', 'href', 'key',
    'latitude', 'longitude', 'stroke', 'strokeWidth', 'strokeDash'
]

# typos mais comuns vistos em prova -> correção
_TYPOS_COMUNS = {
    'alt.Chat(': 'alt.Chart(',
    'alt.chart(': 'alt.Chart(',
    'markbar(': 'mark_bar(',
    'mark_bat(': 'mark_bar(',
    'mark_line(': 'mark_line(',
    'marker_bar(': 'mark_bar(',
    '.encod(': '.encode(',
    '.enconde(': '.encode(',
    '.emcode(': '.encode(',
    'improt pandas': 'import pandas',
    'imoprt altair': 'import altair',
    'improt altair': 'import altair',
    'pandas as pandas': 'pandas as pd',
    'value_count(': 'value_counts(',
    'describ(': 'describe(',
    'grupby(': 'groupby(',
    'groupby(': 'groupby(',
    'read_excell(': 'read_excel(',
    'read_csv(': 'read_csv(',
}


def _contagem_delimitadores(codigo):
    """Retorna dict com o saldo (abre - fecha) de cada tipo de delimitador."""
    return {
        '(': codigo.count('(') - codigo.count(')'),
        '[': codigo.count('[') - codigo.count(']'),
        '{': codigo.count('{') - codigo.count('}'),
    }


def _diagnosticar_syntax_error(erro, codigo):
    dicas = []
    saldo = _contagem_delimitadores(codigo)
    fechamentos = {'(': ')', '[': ']', '{': '}'}
    for abre, diff in saldo.items():
        if diff > 0:
            dicas.append(
                f"Faltam {diff} '{fechamentos[abre]}' pra fechar todos os '{abre}' abertos."
            )
        elif diff < 0:
            dicas.append(
                f"Tem {-diff} '{fechamentos[abre]}' a mais do que '{abre}' — sobrou fechamento."
            )
    if not dicas:
        linha = codigo.split('\n')[erro.lineno - 1] if erro.lineno and erro.lineno <= len(codigo.split('\n')) else ''
        dicas.append(
            "Os parênteses/colchetes estão balanceados, então o problema é outra coisa: "
            "vírgula faltando entre argumentos, ':' onde devia ter '=' (ou o contrário), "
            "ou aspas não fechadas. Olhe com atenção a linha:\n    " + linha.strip()
        )
    return dicas


def _diagnosticar_erro_execucao(erro, ambiente):
    tipo = type(erro).__name__
    msg = str(erro)
    dicas = [f"Erro do tipo {tipo}: {msg}"]

    if isinstance(erro, NameError):
        m = re.search(r"name '(\w+)' is not defined", msg)
        if m:
            nome = m.group(1)
            candidatos = difflib.get_close_matches(nome, list(ambiente.keys()) + _TOPO_ALTAIR, n=3, cutoff=0.6)
            if nome in ('alt', 'pd'):
                dicas.append("Faltou importar? (`import altair as alt` / `import pandas as pd`)")
            elif candidatos:
                dicas.append(f"'{nome}' não existe. Você quis dizer: {', '.join(candidatos)}?")
            else:
                dicas.append(f"'{nome}' não foi definido em nenhuma célula anterior — rode a célula que cria essa variável antes.")

    elif isinstance(erro, AttributeError):
        m = re.search(r"module 'altair' has no attribute '(\w+)'", msg)
        m2 = re.search(r"object has no attribute '(\w+)'", msg)
        alvo = (m or m2)
        if alvo:
            nome = alvo.group(1)
            candidatos = difflib.get_close_matches(nome, _TOPO_ALTAIR + _MARKS_VALIDOS, n=3, cutoff=0.5)
            if candidatos:
                dicas.append(f"'{nome}' não existe (erro de digitação?). Você quis dizer: {', '.join(candidatos)}?")

    elif isinstance(erro, KeyError):
        col = msg.strip("'\"")
        df = ambiente.get('df')
        if isinstance(df, pd.DataFrame):
            candidatos = difflib.get_close_matches(col, list(map(str, df.columns)), n=3, cutoff=0.4)
            if candidatos:
                dicas.append(f"Coluna '{col}' não existe na base. Colunas parecidas: {candidatos}")
            else:
                dicas.append(f"Coluna '{col}' não existe. Colunas disponíveis na base: {list(df.columns)}")

    elif isinstance(erro, TypeError):
        dicas.append(
            "Erros de TypeError em Altair geralmente são: argumento errado dentro de encode() "
            "(ex: passar uma lista onde precisa de um alt.X(...)), ou parêntese fechado no lugar errado, "
            "encerrando a chamada antes da hora. Confira o encadeamento de .mark_...().encode()."
        )

    elif isinstance(erro, ValueError):
        dicas.append(
            "ValueError em Altair costuma ser o formato do canal errado — confira se está usando "
            "':Q' (quantitativa), ':N' (nominal), ':O' (ordinal) ou ':T' (temporal/data) no lugar certo."
        )

    return dicas


def _autocorrigir_typos(codigo):
    """Aplica substituições de typos comuns. Retorna (codigo_corrigido, lista_de_mudancas)."""
    mudou = []
    for errado, certo in _TYPOS_COMUNS.items():
        if errado in codigo:
            codigo = codigo.replace(errado, certo)
            mudou.append(f"'{errado}' → '{certo}'")
    return codigo, mudou


def _autocorrigir_delimitadores(codigo):
    """Se faltar fechamento de (), [] ou {}, adiciona no final. Retorna (codigo, mudou_algo)."""
    saldo = _contagem_delimitadores(codigo)
    fechamentos = {'(': ')', '[': ']', '{': '}'}
    add = ''
    mudou = []
    # fecha na ordem inversa de abertura mais comum: () por último costuma ser o de fora
    for abre in ['{', '[', '(']:
        diff = saldo[abre]
        if diff > 0:
            add += fechamentos[abre] * diff
            mudou.append(f"adicionado {diff}x '{fechamentos[abre]}' no final")
    return codigo + add, mudou


_PADRAO_CAMPO = re.compile(
    r'(?:^|[\(,]\s*)(?:x|y|x2|y2|color|opacity|size|shape|tooltip|theta|theta2|'
    r'radius|radius2|text|column|row|facet|order|detail|href|key|latitude|longitude)'
    r'\s*=\s*(?:alt\.\w+\(\s*)?[\'"]([^\'"]+)[\'"]'
)


def _checar_colunas_no_codigo(codigo, df):
    """Checagem PROATIVA de nomes de coluna: o Altair NÃO dá erro se você
    referenciar uma coluna que não existe — ele só desenha um gráfico vazio.
    Por isso isso aqui é checado no texto do código, não esperando exceção."""
    if not isinstance(df, pd.DataFrame):
        return []
    avisos = []
    colunas = list(map(str, df.columns))
    campos = set()
    for m in _PADRAO_CAMPO.finditer(codigo):
        nome = m.group(1).split(':')[0].strip()
        if nome and nome not in ('count()',) and not nome.endswith('()'):
            campos.add(nome)
    for campo in campos:
        if campo not in colunas:
            candidatos = difflib.get_close_matches(campo, colunas, n=3, cutoff=0.4)
            if candidatos:
                avisos.append(f"Campo '{campo}' usado no gráfico não bate com nenhuma coluna da base. Você quis dizer: {candidatos}?")
            else:
                avisos.append(f"Campo '{campo}' usado no gráfico não existe na base. Colunas disponíveis: {colunas}")
    return avisos


def checar(codigo, df=None, tentar_autocorrigir=True, max_tentativas=4):
    """
    Roda `codigo` (uma expressão Altair, como string) contra `df` (ou uma
    base de teste, se não passar nenhuma) e imprime diagnóstico do erro,
    com sugestão de correção. Se `tentar_autocorrigir=True`, tenta
    consertar sozinha erros bobos (parêntese faltando, typos comuns) e
    mostra o código corrigido que funcionou.
    """
    base_teste = df if isinstance(df, pd.DataFrame) else pd.DataFrame({
        'categoria': ['A', 'B', 'C'], 'valor': [10, 20, 30], 'data': pd.date_range('2024-01-01', periods=3)
    })
    codigo_atual = codigo
    historico_mudancas = []

    for tentativa in range(max_tentativas):
        ambiente = {'pd': pd, 'alt': alt, 'df': base_teste}
        try:
            resultado = eval(compile(codigo_atual, '<celula>', 'eval'), ambiente)
            avisos_coluna = _checar_colunas_no_codigo(codigo_atual, base_teste)
            if avisos_coluna:
                print("⚠️  O código rodou sem dar erro, mas o Altair NÃO avisa quando uma coluna não existe")
                print("   (ele só desenha um gráfico vazio) — então confira à mão:")
                for a in avisos_coluna:
                    print(f"  - {a}")
            else:
                print("✅ O código rodou sem erros!")
            if historico_mudancas:
                print("\nCorreções automáticas aplicadas até funcionar:")
                for m in historico_mudancas:
                    print(f"  - {m}")
                print("\nCódigo corrigido:\n")
                print(codigo_atual)
            return resultado

        except SyntaxError as e:
            dicas = _diagnosticar_syntax_error(e, codigo_atual)
            if tentar_autocorrigir:
                novo_codigo, mudou_typo = _autocorrigir_typos(codigo_atual)
                novo_codigo, mudou_delim = _autocorrigir_delimitadores(novo_codigo)
                if mudou_typo or mudou_delim:
                    historico_mudancas += mudou_typo + mudou_delim
                    codigo_atual = novo_codigo
                    continue  # tenta de novo com o código corrigido
            print("❌ Erro de sintaxe:")
            for d in dicas:
                print(f"  - {d}")
            return None

        except Exception as e:
            dicas = _diagnosticar_erro_execucao(e, ambiente)
            print(f"❌ {type(e).__name__}:")
            for d in dicas:
                print(f"  - {d}")
            if historico_mudancas:
                print("\n(Correções automáticas já aplicadas antes desse erro:")
                for m in historico_mudancas:
                    print(f"  - {m}")
                print(")")
            return None

    print("Não consegui corrigir automaticamente depois de várias tentativas. Revise manualmente com as dicas acima.")
    return None


# =====================================================================
# EXEMPLOS DE USO (rode pra testar que está tudo funcionando)
# =====================================================================
if __name__ == '__main__':
    print("--- Exemplo 1: parêntese faltando ---")
    checar('''
alt.Chart(df).mark_bar().encode(
    x="categoria:N",
    y="valor:Q"
''')

    print("\n--- Exemplo 2: typo em Chart ---")
    checar('alt.Chat(df).mark_bar().encode(x="categoria:N", y="valor:Q")')

    print("\n--- Exemplo 3: coluna que não existe ---")
    checar('alt.Chart(df).mark_bar().encode(x="categoriaa:N", y="valor:Q")')

    print("\n--- Exemplo 4: código correto ---")
    checar('alt.Chart(df).mark_bar().encode(x="categoria:N", y="valor:Q")')
