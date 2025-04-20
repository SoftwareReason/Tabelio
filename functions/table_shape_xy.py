# table_shape_x.py
import pandas as pd

# table_shape_x_y.py
def table_shape_x_y(df: pd.DataFrame, ycolumn: str, xcolumn: str, modo_percentual: bool = False) -> pd.DataFrame:
    """
    Gera uma tabela cruzada contendo frequências absolutas e relativas (percentuais),
    a partir de duas variáveis categóricas: uma para as linhas (ycolumn) e outra para as colunas (xcolumn).
    Preserva todas as categorias da variável de linha, mesmo que não estejam presentes após o cruzamento.

    Parâmetros:
    - df: DataFrame original contendo os dados.
    - ycolumn: Nome da coluna que será utilizada como variável nas linhas.
    - xcolumn: Nome da coluna que será utilizada como variável nas colunas.
    - modo_percentual: Define se o percentual será baseado na soma da respectiva coluna (True) ou no total geral (False).

    Retorna:
    - DataFrame com as categorias de ycolumn nas linhas, cruzadas com os valores de xcolumn nas colunas,
      incluindo contagem absoluta e percentual.
    """

    # Criar cópia de segurança do DataFrame
    df_copy = df.copy()

    # Gerar tabela cruzada (crosstab) com contagem absoluta entre as variáveis
    result_table = pd.crosstab(df_copy[ycolumn], df_copy[xcolumn])

    # Preservar todas as categorias da variável de linha
    categorias_y = (
        df[ycolumn]
        .dropna()
        .unique()
        .tolist()
    )
    result_table = result_table.reindex(categorias_y, fill_value=0)

    # Armazenar os nomes das colunas (xcolumn) da tabela
    base_columns = result_table.columns.tolist()
    columns_organized_list = []

    # Calcular os percentuais e organizar as colunas
    for column in base_columns:
        result_table[column] = result_table[column].astype(int)

        if modo_percentual:
            divisor = result_table[column].sum()
        else:
            divisor = result_table[base_columns].sum().sum()

        result_table[f'Percentual {column}'] = result_table[column].apply(
            lambda num: f'{(num / divisor) * 100:.1f}%'
        )

        columns_organized_list.append(column)
        columns_organized_list.append(f'Percentual {column}')
    # Reorganizar colunas e ajustar índice
    result_table = result_table[columns_organized_list]
    result_table = result_table.sort_values(by=column, ascending=False).reset_index()
    result_table.columns.name = None
    result_table = result_table
    return result_table

