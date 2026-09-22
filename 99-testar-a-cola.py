# =====================================================================
# TESTAR A COLA — roda todo o código do repositório contra uma base
# sintética e avisa o que quebrou.
# ---------------------------------------------------------------------
# POR QUE ISSO EXISTE: as versões de pandas e Altair do Colab mudam sem
# aviso, e código que funcionava ano passado pode dar erro hoje (foi
# exatamente o que aconteceu com resample('M') → resample('ME')).
# Rode isso ANTES da prova (na véspera e/ou no começo da prova) pra
# saber se algum snippet da cola quebrou na versão do dia.
#
# Como usar no Colab:
#   !git clone https://github.com/BeAmara1/cola-meacc.git
#   %cd cola-meacc
#   !python 99-testar-a-cola.py
#
# Ou, se estiver rodando localmente, só: python 99-testar-a-cola.py
# =====================================================================

import contextlib
import glob
import io
import os
import re
import sys

import pandas as pd
import altair as alt

PASTA = os.path.dirname(os.path.abspath(__file__))

# Arquivos que NÃO devem ser testados automaticamente:
# - 07: documenta a prova real, então referencia bases reais (enem, censo...) que não existem aqui
# - 10-como-usar: os exemplos chamam funções definidas no outro arquivo
IGNORAR = ('07-prova-2025-resolvida.md', '10-como-usar-o-corretor.md')

# Trechos que indicam código que só faz sentido dentro do Colab, ou que
# referencia arquivo de exemplo inexistente — são pulados, não são falha.
MARCAS_SO_COLAB = (
    'google.colab', 'drive.mount', "'arquivo.", '"arquivo.',
    '{PASTA}', 'caminho/da/pasta', 'MyDrive',
)


def so_roda_no_colab(bloco):
    if any(marca in bloco for marca in MARCAS_SO_COLAB):
        return True
    # comandos de shell/magics do notebook (!pip install, %cd ...)
    return any(l.strip().startswith(('!', '%')) for l in bloco.split('\n'))


def base_generica(n=40):
    """Base sintética cujas colunas têm os mesmos nomes-placeholder dos exemplos."""
    import numpy as np
    rng = np.random.default_rng(0)
    return pd.DataFrame({
        'coluna': rng.normal(50, 15, n).round(1),
        'categoria': rng.choice(['A', 'B', 'C'], n),
        'valor': rng.integers(1, 100, n),
        'var1': rng.normal(10, 3, n).round(2),
        'var2': rng.normal(20, 5, n).round(2),
        'data': pd.date_range('2023-01-01', periods=n, freq='D'),
        'id': [f'obs{i}' for i in range(n)],
        'grupo_A': rng.normal(5, 1, n).round(2),
        'grupo_B': rng.normal(6, 2, n).round(2),
        'idade': rng.integers(1, 90, n),
        'origem': rng.choice(['X', 'Y'], n),
        'grupo': rng.choice(['g1', 'g2'], n),
        'ano': rng.choice([2021, 2022, 2023], n),
        'mes_dia': pd.date_range('2023-01-01', periods=n, freq='D').strftime('%m-%d'),
    })


def base_percentuais():
    """Base de 2 colunas tipo tabela de frequência do livro (para os exemplos de % )."""
    return pd.DataFrame({
        'Field of Study': ['Artes', 'Bio', 'Negócios', 'Educação', 'Engenharia'],
        'Percent': [10.5, 15.0, 20.2, 8.3, 40.0],
    })


def ambiente(df):
    return {
        'pd': pd, 'alt': alt, 'df': df,
        'df1': df.copy(), 'df2': df.copy(), 'df_long': df.copy(), 'df_junto': df.copy(),
        'df_idx': df.set_index('data') if 'data' in df.columns else df,
        'i': 0, 'indice_do_atipico': 0,
        'lista': [1, 2, 3, 4, 5],
        'bins': [0, 18, 30, 55, 100],
        'labels': ['a', 'b', 'c', 'd'],
        'var1': 'var1', 'var2': 'var2',
    }


def testar_markdowns():
    """
    Cada arquivo .md é tratado como um notebook: os blocos rodam em sequência
    no MESMO namespace, então um bloco pode usar variáveis criadas no anterior
    (é assim que você vai usar na prova mesmo).
    """
    falhas, total, pulados = [], 0, 0
    for md in sorted(glob.glob(os.path.join(PASTA, '*.md'))):
        if os.path.basename(md) in IGNORAR:
            continue
        blocos = re.findall(r'```python\n(.*?)```', open(md, encoding='utf-8').read(), re.S)
        amb_generico = ambiente(base_generica())
        amb_percentual = ambiente(base_percentuais())
        for i, bloco in enumerate(blocos):
            uteis = [l for l in bloco.split('\n') if l.strip() and not l.strip().startswith('#')]
            if not uteis:
                continue
            if so_roda_no_colab(bloco):
                pulados += 1
                continue
            total += 1
            erro_final = None
            # tenta na base genérica; se falhar, tenta na base de percentuais
            # (o stdout dos blocos é engolido pra não poluir o relatório)
            for amb in (amb_generico, amb_percentual):
                try:
                    with contextlib.redirect_stdout(io.StringIO()):
                        exec(compile(bloco, f'{os.path.basename(md)}#{i}', 'exec'), amb)
                    erro_final = None
                    break
                except Exception as e:
                    erro_final = e
            if erro_final is not None:
                falhas.append((os.path.basename(md), i, type(erro_final).__name__, str(erro_final)[:180], bloco.strip()[:200]))
    return total, falhas, pulados


def testar_funcoes_snippets():
    """Chama cada função do 06-snippets-prontos.py de verdade."""
    caminho = os.path.join(PASTA, '06-snippets-prontos.py')
    if not os.path.exists(caminho):
        return 0, [('06-snippets-prontos.py', '-', 'FileNotFound', 'arquivo não encontrado', '')]
    amb = {}
    exec(open(caminho, encoding='utf-8').read().split("if __name__")[0], amb)
    df = base_generica()
    chamadas = {
        'grafico_barras (contagem)': lambda: amb['grafico_barras'](df, 'categoria'),
        'grafico_barras (valor)': lambda: amb['grafico_barras'](df, 'categoria', 'valor'),
        'grafico_pizza': lambda: amb['grafico_pizza'](df, 'categoria'),
        'histograma (auto)': lambda: amb['histograma'](df, 'valor'),
        'histograma (step)': lambda: amb['histograma'](df, 'valor', step=10),
        'histograma (step+extent)': lambda: amb['histograma'](df, 'valor', step=10, extent=[0, 100]),
        'histograma_percentual': lambda: amb['histograma_percentual'](df, 'valor', step=10),
        'limites_atipicos': lambda: amb['limites_atipicos'](df, 'valor'),
        'encontrar_atipicos': lambda: amb['encontrar_atipicos'](df, 'valor'),
        'boxplot': lambda: amb['boxplot'](df, 'valor'),
        'boxplot_comparativo': lambda: amb['boxplot_comparativo'](df, 'id', ['grupo_A', 'grupo_B']),
        'grafico_linha': lambda: amb['grafico_linha'](df, 'data', 'valor'),
        "agregar_por_periodo ('ME')": lambda: amb['agregar_por_periodo'](df, 'data', 'valor', 'ME'),
        "agregar_por_periodo ('M' antigo)": lambda: amb['agregar_por_periodo'](df, 'data', 'valor', 'M'),
        'tabela_dupla_entrada': lambda: amb['tabela_dupla_entrada'](df, 'categoria', 'grupo'),
        'distribuicao_condicional': lambda: amb['distribuicao_condicional'](df, 'categoria', 'grupo'),
        'barras_segmentadas': lambda: amb['barras_segmentadas'](df, 'categoria', 'grupo', normalizar=True),
        'dispersao': lambda: amb['dispersao'](df, 'var1', 'var2'),
        'pearson': lambda: amb['pearson'](df, 'var1', 'var2'),
        'criar_faixas': lambda: amb['criar_faixas'](df, 'idade', [0, 18, 30, 55, 100], ['a', 'b', 'c', 'd']),
    }
    falhas = []
    for nome, fn in chamadas.items():
        try:
            fn()
        except Exception as e:
            falhas.append(('06-snippets-prontos.py', nome, type(e).__name__, str(e)[:180], ''))
    return len(chamadas), falhas


def testar_corretor():
    """Confere que o corretor de código continua diagnosticando certo."""
    caminho = os.path.join(PASTA, '10-corretor-de-codigo-altair.py')
    if not os.path.exists(caminho):
        return 0, [('10-corretor-de-codigo-altair.py', '-', 'FileNotFound', 'arquivo não encontrado', '')]
    amb = {}
    exec(open(caminho, encoding='utf-8').read().split("if __name__")[0], amb)
    checar = amb['checar']
    df = base_generica()
    falhas = []
    casos = {
        'código correto': 'alt.Chart(df).mark_bar().encode(x="categoria:N", y="valor:Q")',
        'parêntese faltando (deve autocorrigir)': 'alt.Chart(df).mark_bar().encode(x="categoria:N", y="valor:Q"',
        'várias linhas': 'base = df.copy()\nalt.Chart(base).mark_bar().encode(x="categoria:N", y="valor:Q")',
    }

    for nome, codigo in casos.items():
        try:
            saida = io.StringIO()
            with contextlib.redirect_stdout(saida):
                checar(codigo, df=df)
            texto = saida.getvalue()
            if '❌' in texto:
                falhas.append(('10-corretor', nome, 'DiagnosticoInesperado', texto.strip()[:180], ''))
        except Exception as e:
            falhas.append(('10-corretor', nome, type(e).__name__, str(e)[:180], ''))
    return len(casos), falhas


if __name__ == '__main__':
    print(f"pandas {pd.__version__} | altair {alt.__version__} | python {sys.version.split()[0]}\n")

    total_md, falhas_md, pulados = testar_markdowns()
    total_fn, falhas_fn = testar_funcoes_snippets()
    total_cor, falhas_cor = testar_corretor()

    todas = falhas_md + falhas_fn + falhas_cor
    total = total_md + total_fn + total_cor

    print(f"Blocos de código dos .md testados: {total_md}  ({pulados} pulados: só rodam no Colab)")
    print(f"Funções do 06 testadas:            {total_fn}")
    print(f"Casos do corretor testados:        {total_cor}")
    print(f"\n{'=' * 60}")
    if not todas:
        print(f"✅ TUDO CERTO — {total} testes passaram nesta versão das bibliotecas.")
    else:
        print(f"⚠️  {len(todas)} de {total} testes falharam:\n")
        for arq, ident, tipo, msg, trecho in todas:
            print(f"--- {arq} [{ident}]  {tipo}: {msg}")
            if trecho:
                print('    ' + trecho.replace('\n', '\n    '))
            print()
        print("Se a falha for de versão (ex: 'no longer supported'), ajuste o snippet")
        print("correspondente antes da prova — a mensagem de erro geralmente já diz a troca.")
