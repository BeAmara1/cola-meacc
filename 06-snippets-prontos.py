# =====================================================================
# COLA MEACC — snippets prontos para copiar e colar
# Métodos Estatísticos Aplicados às Ciências Sociais (FGV — Profa. Polyana)
# =====================================================================

import pandas as pd
import altair as alt
alt.data_transformers.disable_max_rows()  # evita erro em bases > 5000 linhas

# =====================================================================
# 1) LEITURA DE DADOS
# =====================================================================
# df = pd.read_csv('arquivo.csv')
# df = pd.read_csv('arquivo.csv', sep=';')          # separador ;
# df = pd.read_excel('arquivo.xls')
# df = pd.read_csv('arquivo.tsv', sep='\t')

# =====================================================================
# 2) CHECAGEM DE CONSISTÊNCIA (dados percentuais devem somar 100)
# =====================================================================
# df.Percent.sum()
# df.loc[len(df)] = ['Outras', 100 - df.Percent.sum()]              # add categoria faltante
# df.loc[i, 'Percent'] += 100 - df.Percent.sum()                    # corrige arredondamento

# =====================================================================
# 3) UNIVARIADA QUALITATIVA
# =====================================================================
# df['coluna'].value_counts()
# df['coluna'].value_counts(normalize=True) * 100

# gráfico de barras (ordenado)
def grafico_barras(df, coluna_cat, coluna_valor=None):
    if coluna_valor:
        return alt.Chart(df).mark_bar().encode(
            x=alt.X(f'{coluna_cat}:N', sort='-y', axis=alt.Axis(labelAngle=-45)),
            y=f'{coluna_valor}:Q',
            tooltip=[coluna_cat, coluna_valor]
        )
    return alt.Chart(df).mark_bar().encode(
        x=alt.X(f'{coluna_cat}:N', sort='-y'),
        y='count()',
        tooltip=[coluna_cat, 'count()']
    )

# gráfico de setores (só qualitativa com poucas categorias, soma = 100%)
def grafico_pizza(df, coluna_cat, coluna_valor=None):
    theta = f'{coluna_valor}:Q' if coluna_valor else 'count()'
    return alt.Chart(df).mark_arc().encode(
        theta=theta,
        color=f'{coluna_cat}:N',
        tooltip=[coluna_cat, theta]
    )

# =====================================================================
# 4) HISTOGRAMA (univariada quantitativa)
# =====================================================================
def histograma(df, coluna, step=None, extent=None):
    bin_arg = alt.Bin(step=step, extent=extent) if step else True
    return alt.Chart(df).mark_bar().encode(
        alt.X(f'{coluna}:Q', bin=bin_arg),
        y='count()'
    )

# histograma em percentual (útil pra comparar bases de tamanhos diferentes)
def histograma_percentual(df, coluna, step=1):
    return alt.Chart(df).transform_joinaggregate(
        total='count(*)'
    ).transform_calculate(
        pct='1 / datum.total'
    ).mark_bar().encode(
        alt.X(f'{coluna}:Q', bin=alt.Bin(step=step)),
        alt.Y('sum(pct):Q', axis=alt.Axis(format='%'))
    )

# =====================================================================
# 5) MEDIDAS DESCRITIVAS
# =====================================================================
# df['coluna'].describe()          # tudo de uma vez
# df['coluna'].mean()
# df['coluna'].median()
# df['coluna'].mode()
# df['coluna'].std()
# df['coluna'].var()

def limites_atipicos(df, coluna):
    """Retorna (limite_inferior, limite_superior, aiq) pela regra 1.5xAIQ."""
    q1 = df[coluna].quantile(0.25)
    q3 = df[coluna].quantile(0.75)
    aiq = q3 - q1
    return q1 - 1.5 * aiq, q3 + 1.5 * aiq, aiq

def encontrar_atipicos(df, coluna):
    lim_inf, lim_sup, aiq = limites_atipicos(df, coluna)
    return df[(df[coluna] < lim_inf) | (df[coluna] > lim_sup)]

def boxplot(df, coluna, destacar_atipicos=True):
    extent = 1.5 if destacar_atipicos else 'min-max'
    return alt.Chart(df).mark_boxplot(extent=extent).encode(
        y=f'{coluna}:Q'
    ).properties(width=200)

def boxplot_comparativo(df, id_col, grupos, nome_categoria='categoria', nome_valor='valor'):
    """grupos: lista de nomes de colunas a comparar lado a lado (ex: ['renda_homem','renda_mulher'])."""
    df_long = df.melt(id_vars=[id_col], value_vars=grupos,
                       var_name=nome_categoria, value_name=nome_valor)
    return alt.Chart(df_long).mark_boxplot(extent=1.5, size=40).encode(
        alt.X(f'{nome_valor}:Q'),
        alt.Y(f'{nome_categoria}:N')
    ).properties(height=200, width=600)

# =====================================================================
# 6) SÉRIES TEMPORAIS
# =====================================================================
# df['data'] = pd.to_datetime(df['data'])

def grafico_linha(df, coluna_data, coluna_valor, dominio_y=None):
    y_enc = alt.Y(f'{coluna_valor}:Q', scale=alt.Scale(domain=dominio_y)) if dominio_y else f'{coluna_valor}:Q'
    return alt.Chart(df).mark_line().encode(
        x=f'{coluna_data}:T',
        y=y_enc,
        tooltip=[coluna_data, coluna_valor]
    )

def agregar_por_periodo(df, coluna_data, coluna_valor, periodo='M', agregacao='mean'):
    """periodo: 'D' dia, 'W' semana, 'M' mês, 'Y' ano."""
    df_idx = df.set_index(coluna_data)
    return getattr(df_idx.resample(periodo)[coluna_valor], agregacao)()

# variação percentual entre períodos
# df['variacao_pct'] = df['valor'].pct_change() * 100

# =====================================================================
# 7) BIVARIADA — DUAS QUALITATIVAS (tabela de dupla entrada)
# =====================================================================
def tabela_dupla_entrada(df, var1, var2):
    tabela = df.groupby([var1, var2]).size().unstack(1)
    tabela.loc['Total', :] = tabela.sum(axis=0)
    tabela.loc[:, 'Total'] = tabela.sum(axis=1)
    return tabela.fillna(0)

def distribuicao_condicional(df, var1, var2, condicional_em=0):
    """condicional_em=0 -> % de var2 dentro de cada var1; =1 -> % de var1 dentro de cada var2."""
    long = df.groupby([var1, var2]).size()
    return long / long.groupby(level=condicional_em).transform(sum) * 100

def barras_segmentadas(df, var1, var2, normalizar=False):
    long = df.groupby([var1, var2]).size().reset_index().rename(columns={0: 'contagem'})
    x_enc = alt.X('contagem:Q', stack='normalize') if normalizar else alt.X('contagem:Q')
    return alt.Chart(long).mark_bar().encode(
        x=x_enc,
        y=f'{var1}:N',
        color=f'{var2}:N'
    )

# =====================================================================
# 8) BIVARIADA — DUAS QUANTITATIVAS (dispersão + Pearson)
# =====================================================================
def dispersao(df, var1, var2, dominio_y=None):
    y_enc = alt.Y(f'{var2}:Q', scale=alt.Scale(domain=dominio_y)) if dominio_y else f'{var2}:Q'
    return alt.Chart(df).mark_circle().encode(
        x=f'{var1}:Q',
        y=y_enc,
        tooltip=[var1, var2]
    )

def pearson(df, var1, var2):
    return df[[var1, var2]].corr(numeric_only=True)

# =====================================================================
# 9) CRIAR CATEGORIA A PARTIR DE QUANTITATIVA
# =====================================================================
def criar_faixas(df, coluna, bins, labels, right=True):
    return pd.cut(df[coluna], bins=bins, labels=labels, right=right)
