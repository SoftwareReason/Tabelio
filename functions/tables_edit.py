import pandas as pd

def config_tables(dfs, espacamento_colunas=3):
    """
    Empilha uma lista de DataFrames horizontalmente (lado a lado), 
    inserindo espaçadores de colunas vazias entre eles e repetindo o cabeçalho antes de cada bloco.

    Parâmetros:
    - dfs (list): Lista de DataFrames a serem organizados lado a lado.
    - espacamento_colunas (int): Número de colunas vazias entre cada tabela.

    Retorno:
    - DataFrame único, com todas as tabelas lado a lado e separadas por colunas em branco.
    """

    dfs_formatados = []

    for df in dfs:
        # Cria um DataFrame contendo o cabeçalho visível como primeira linha
        header_df = pd.DataFrame(columns=df.columns)

        # Concatena o cabeçalho com a tabela de dados
        tabela_completa = pd.concat([header_df, df], ignore_index=True)

        # Adiciona o bloco completo à lista de tabelas
        dfs_formatados.append(tabela_completa)

        # Cria espaçador de colunas vazias com mesmo número de linhas da tabela
        espacador = pd.DataFrame([[""] * espacamento_colunas] * tabela_completa.shape[0], columns=[""] * espacamento_colunas)
        dfs_formatados.append(espacador)

    # Concatena todos os blocos horizontalmente (lado a lado)
    return pd.concat(dfs_formatados, axis=1)
