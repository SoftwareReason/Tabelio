import pandas as pd


# table_shape_x_y_z.py
def table_shape_x_y_z(df: pd.DataFrame, ycolumn: str, xcolumn: str, filtro_dict: dict, modo_percentual: bool = False) -> pd.DataFrame:
    """
    Gera uma tabela cruzada com contagens absolutas e percentuais, aplicando previamente
    um filtro condicional sobre o DataFrame de origem. Preserva todas as categorias da variável de linha
    mesmo que estejam ausentes após filtragem.

    Parâmetros:
    - df: DataFrame original contendo os dados.
    - ycolumn: Nome da coluna que será utilizada como variável nas linhas.
    - xcolumn: Nome da coluna que será utilizada como variável nas colunas.
    - filtro_dict: Dicionário com colunas como chaves e valores desejados como filtros.
    - modo_percentual: Define se o percentual será baseado na soma da respectiva coluna (True) ou no total geral (False).

    Retorna:
    - DataFrame com valores de ycolumn nas linhas, cruzados com os de xcolumn nas colunas,
      incluindo tanto contagem absoluta quanto percentual.
    """

    # Criar cópia de segurança do DataFrame original
    df_copy = df.copy()

    # Aplicar filtros de universo
    for key, value in filtro_dict.items():
        df_copy = df_copy[df_copy[key].isin([value])]

    # Gerar tabela cruzada com contagens absolutas
    result_table = pd.crosstab(df_copy[ycolumn], df_copy[xcolumn])

    # Preservar todas as categorias da variável de linha
    categorias_y = (
        df[ycolumn]
        .dropna()
        .unique()
        .tolist()
    )
    result_table = result_table.reindex(categorias_y, fill_value=0)

    # Armazenar colunas base e organizar saída
    base_columns = result_table.columns.tolist()
    columns_organized_list = []

    for column in base_columns:
        result_table[column] = result_table[column].astype(int)

        # Neste trecho, utilizo forma compacta (ternário) para revisão e aprendizado pessoal.
        # Nas outras funções, segue-se o padrão tradicional com if/else.
        divisor = (
            result_table[column].sum()
            if modo_percentual
            else result_table[base_columns].sum().sum()
        )

        result_table[f'Percentual {column}'] = result_table[column].apply(
            lambda num: f'{(num / divisor) * 100:.1f}%'
        )

        columns_organized_list.append(column)
        columns_organized_list.append(f'Percentual {column}')
        result_table.sort_values(by=column, ascending=False)

    # Reorganizar colunas e ajustar índice
    result_table = result_table[columns_organized_list]
    result_table = result_table.sort_values(by=column, ascending=False).reset_index()
    result_table.columns.name = None

    return result_table

