# main.py
import pandas as pd
import json
from functions.table_shape_y import table_shape_y
from functions.table_shape_xy import table_shape_x_y
from functions.table_shape_xyz import table_shape_x_y_z
from functions.tables_edit import config_tables


try:

    #--------------
    # 1. Caminhos
    #--------------
    # Caminho local do BD
    CAMINHO_DADOS = 'dados/[220.00]_vale_peat_2025_momento_2_aplicação_vale_peat_2025_15-04-2025_20-14-31.xlsx'
    # Caminho cfg
    CAMINHO_CONFIG = 'config/colunas_para_analise.json'
    #Local para salvar arquivo de saída
    CAMINHO_SAIDA = 'saida/tabelas_geradas.xlsx'


    #--------------
    # 2. Leitura: Banco de Dados e Configurações
    #--------------
    df = pd.read_excel(CAMINHO_DADOS)
    with open(CAMINHO_CONFIG, 'r', encoding='utf-8') as f:
        config = json.load(f)

    tabelas_y = []
    tabelas_xy = []
    tabelas_xyz = []

    #--------------
    # 3. AVISOS!
    #--------------
    if 'y' not in config:
        raise KeyError("⚠️ A chave 'y' não está presente no arquivo de configuração.")
    if 'x_y' not in config:
        raise KeyError("⚠️ A chave 'y_x' não está presente no arquivo de configuração.")
    if 'x_y_z' not in config:
        raise KeyError("⚠️ A chave 'x_y_z' não está presente no arquivo de configuração.")

    #--------------
    # 4. Análises
    #--------------
    for coluna in config.get('y', []):
        print(f'Gerando tabela de análise para: {coluna}.')
        tabela_y = table_shape_y(df, column=coluna)
        tabelas_y.append(tabela_y)

    for par in config.get('x_y', []):
        y = par['y']
        x = par['x']
        print(f'Gerando tabela de análise cruzada entre: {y} x {x}.')
        tabela_xy = table_shape_x_y(df, ycolumn=y, xcolumn=x)
        tabelas_xy.append(tabela_xy)

    for triple in config.get('x_y_z', []):
        y = triple['y']
        x = triple['x']
        z = triple['z']
        print(f'Gerando tabela cruzada entre: {y} x {x}, com filtro {z}.')
        tabela_xyz = table_shape_x_y_z(df, ycolumn=y, xcolumn=x, filtro_dict=z)
        tabelas_xyz.append(tabela_xyz)

    #--------------
    # 5. Saída
    #--------------
    print("Quase lá!")
    print("Estou gerando seu arquivo '.xlsx' com os dados.")
    saida = pd.ExcelWriter(CAMINHO_SAIDA, engine='openpyxl')

    if tabelas_y:
        print("Organizando as tabelas de análise simples lado a lado...")
        resultado_y = config_tables(tabelas_y)
        resultado_y.to_excel(saida, index=False, sheet_name="Tabelas de análise simples")

    if tabelas_xy:
        print("Organizando as tabelas de análise composta lado a lado...")
        resultado_xy = config_tables(tabelas_xy)
        resultado_xy.to_excel(saida, index=False, sheet_name="Tabelas de análise composta")

    if tabelas_xyz:
        print("Organizando as tabelas de análise complexa lado a lado...")
        resultado_xyz = config_tables(tabelas_xyz)
        resultado_xyz.to_excel(saida, index=False, sheet_name="Tabelas de análise complexa")

    print(f'Só mais um pouquinho...')
    saida.close()
    print(f"✅ Arquivo com todas as análises gerado com sucesso em: {CAMINHO_SAIDA}")

except Exception as e:
    print(f"❌ Ocorreu um erro durante a execução: {e}")
    print(f"DICA: O arquivo READ.me contém todo conteúdo necessário para a utilização desta ferramenta!")
    print(f"Estarei aqui quando estiver pronto, novamente!")

print(f"Obrigado!")
print(f"By: Caio Basile.")