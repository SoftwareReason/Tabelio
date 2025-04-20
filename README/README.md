# AutoTab (ou Tabélio) — Geração Automatizada de Tabelas Tabulares

AutoTab é uma ferramenta Python que automatiza a criação de tabelas estatísticas a partir de bases de dados tabulares.
Ideal para relatórios recorrentes, dashboards no Excel e análise de entrevistas, a ferramenta permite gerar contagens absolutas e percentuais de variáveis com base em regras de configuração simples.

## 🔧 O que ela faz
- Gera tabelas de frequência simples (1 variável)
- Gera tabelas cruzadas (ex: Sexo por Estado)
- Aplica filtros avançados para gerar visões por recortes
- Exporta tudo em um único arquivo Excel pronto para criar gráficos

## 🧠 Como funciona
1. O usuário fornece:
   - Um **arquivo de dados Excel** com as respostas (em `/dados`)
   - Um **arquivo de configuração JSON** com as regras de análise (em `/config`)

2. O script `main.py`:
   - Lê os dados e as regras
   - Executa automaticamente as análises
   - Empilha todas as tabelas
   - Exporta em `/saida/tabelas_geradas.xlsx`

## 📂 Estrutura do projeto
```
tabela_auto/
├── main.py
├── funcoes/
│   ├── table_shape_y.py
│   ├── table_shape_xy.py
│   ├── table_shape_xyz.py
│   └── tables_edit.py
├── config/
│   └── colunas_para_analise.json
├── dados/
│   └── banco_de_dados.xlsx
├── saida/
│   └── tabelas_geradas.xlsx
└── README.md
```

## ⚙️ Exemplo de configuração (`colunas_para_analise.json`)
```json
{
  "y": ["Sexo", "Faixa Etária"],
  "y_x": [
    {"y": "Estado", "x": "Sexo"},
    {"y": "Estado", "x": "Escolaridade"}
  ],
  "x_y_z": [
    {
      "y": "Estado",
      "x": "Sexo",
      "z": {"Faixa Etária": "18 a 29"}
    }
  ]
}
```

## ▶️ Como rodar
Certifique-se de ter o Python e o `pandas` instalados. Depois:

```bash
python main.py
```
## ⚠️ Importante: cuidado com sobrescrita de arquivos

Por padrão, o Tabélio salva o resultado das análises no seguinte caminho:

O arquivo `tabelas_geradas.xlsx` será criado automaticamente na pasta `/saida`.

Se você executar o script mais de uma vez, o arquivo será **sobrescrito automaticamente**, e o conteúdo anterior será perdido.

### 🔄 O que você pode fazer:

- Mova ou renomeie o arquivo de saída após cada execução do script
- Crie uma cópia manual com outro nome, se quiser comparar relatórios

## ✨ Contribuindo
Esse projeto pode ser adaptado, expandido e personalizado conforme as necessidades de qualquer análise. A estrutura modular facilita a inclusão de novos formatos, gráficos ou relatórios.

---

Feito com foco em automação e clareza. Perfeito para transformar análises repetitivas em processos rápidos e replicáveis.

> Desenvolvido por Caio Basile.

