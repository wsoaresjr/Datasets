
import numpy as np
import pandas as pd

# Definindo o tamanho do dataset
n_vendas = 550

# Gerando variáveis numéricas (discretas e contínuas)
np.random.seed(42)
id_venda = np.arange(1, n_vendas + 1)  # ID da venda (discreta)
preco_produto = np.round(np.random.uniform(10, 1000, size=n_vendas), 2)  # Preço do produto entre 10 e 1000 (contínua)
quantidade_vendida = np.random.randint(1, 10, size=n_vendas)  # Quantidade vendida entre 1 e 10 unidades (discreta)
desconto_aplicado = np.round(np.random.uniform(0, 0.3, size=n_vendas), 2)  # Desconto aplicado, entre 0 e 30% (contínua)
avaliacao_produto = np.random.randint(1, 6, size=n_vendas)  # Avaliação do produto de 1 a 5 (discreta)

# Gerando variáveis categóricas (nominais e ordinais)
categoria_produto = np.random.choice(['Eletrônicos', 'Roupas', 'Livros', 'Beleza', 'Casa', 'Esportes'], size=n_vendas)  # Nominal
meio_pagamento = np.random.choice(['Cartão de Crédito', 'Boleto', 'Pix', 'Transferência Bancária'], size=n_vendas)  # Nominal
cod_loja = np.random.choice(['Matriz', 'Filial A', 'Filial B', 'Filial C', 'Loja Virtual'], size=n_vendas)  # Nominal
satisfacao_loja = np.random.choice(['Excelente', 'Boa', 'Neutro', 'Ruim'], size=n_vendas)  # Nominal
regiao_compra = np.random.choice(['Sudeste', 'Sul', 'Centro-Oeste', 'Nordeste', 'Norte'], size=n_vendas)  # Nominal
status_entrega = np.random.choice(['Entregue', 'Em Trânsito', 'Aguardando Pagamento', 'Cancelado'], size=n_vendas)  # Nominal
frete_gratis = np.random.choice(['Sim', 'Não'], size=n_vendas, p=[0.3, 0.7])  # Nominal

# Criando o DataFrame
df_vendas = pd.DataFrame({
    'ID Venda': id_venda,
    'Preço Produto (R$)': preco_produto,
    'Quantidade Vendida': quantidade_vendida,
    'Desconto Aplicado (%)': desconto_aplicado,
    'Avaliação do Produto': avaliacao_produto,
    'Categoria do Produto': categoria_produto,
    'Meio de Pagamento': meio_pagamento,
    'Identificação da Loja': cod_loja,
    'Satisfação com Atendimento': satisfacao_loja,
    'Região de Compra': regiao_compra,
    'Status da Entrega': status_entrega,
    'Frete Grátis': frete_gratis
})

# Exibindo o dataframe ao usuário
#tools.display_dataframe_to_user(name="Base de Dados de Vendas do Marketplace", dataframe=df_vendas)

# Salvando o arquivo em formato CSV para download
csv_path_vendas = 'C:/Users/Walter/Documents/BaseDados/base_dados_vendas_marketplace.csv'
df_vendas.to_csv(csv_path_vendas, index=False)

#csv_path_vendas
