# table_shape_y.py
import pandas as pd

def table_shape_y(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Gera uma tabela com frequência absoluta e percentual de uma única variável categórica,
    preservando todas as categorias existentes no DataFrame, inclusive aquelas com zero ocorrências
    após possíveis filtragens.

    Parâmetros:
    - df: DataFrame original.
    - column: Nome da coluna a ser analisada.
    - modo_percentual: Define se o percentual será baseado no total da coluna (True) ou no total geral (False).

    Retorna:
    - DataFrame com valores únicos da coluna, suas contagens (ABS) e percentuais.
    """

    # Cria cópia de segurança do DataFrame original
    df_copy = df.copy()

    # Calcula a contagem absoluta dos valores únicos na coluna
    abs_counts = df_copy[column].value_counts().to_frame(name='ABS')

    # Recupera todas as categorias possíveis (inclusive as que não aparecem depois de filtros)
    todas_categorias = (
                        df[column] # DataFrame original na coluna especificada
                        .dropna() # Exclui valores vazios
                        .unique() # Apenas valores únicos de uma Series
                        .tolist() # Converte a operação em lista
                        )
    abs_counts = abs_counts.reindex(todas_categorias, fill_value=0)

    # Reset do índice (transforma o valor da coluna em coluna de fato)
    abs_counts = abs_counts.reset_index().rename(columns={'index': column})

    # Cálculo do divisor do percentual
    total_geral = (
        abs_counts['ABS'].sum()
    )

    # Gera coluna de percentual com base no total geral
    abs_counts['Percentual'] = abs_counts['ABS'].apply(
        lambda num: f'{(num / total_geral) * 100:.1f}%' if total_geral else '100.0%'
    )
    abs_counts = abs_counts.sort_values(by='ABS', ascending=False)
    return abs_counts

