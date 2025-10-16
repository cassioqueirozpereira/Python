# Importa a classe principal para interagir com o cluster Spark.
# O SparkContext é o ponto de entrada de baixo nível para a funcionalidade do Spark,
# usado tradicionalmente para trabalhar com RDDs (a estrutura de dados original do Spark).
from pyspark import SparkContext

# Importa a classe SparkSession, que é a interface de programação moderna e unificada.
# Ela combina o SparkContext (criação de conexão) e o SQLContext (funcionalidades SQL).
from pyspark.sql import SparkSession

# Importa o módulo 'os' (Operating System), uma biblioteca padrão do Python.
# Este módulo é crucial para interagir com o sistema operacional, neste caso,
# para manipulação e construção de caminhos de arquivo de forma segura.
import os

import pandas as pd

# ----------------------------------------------------------------------
# INICIALIZAÇÃO E CONEXÃO DE BAIXO NÍVEL (SparkContext)
# ----------------------------------------------------------------------

# Cria uma instância do SparkContext. Quando rodado localmente (como neste caso),
# o Spark inicia um "mini-cluster" em sua máquina.
# Esta linha estabelece a conexão fundamental com o motor do Spark.
spark_contexto = SparkContext()

# Imprime informações sobre a instância do SparkContext que foi criada.
# Isso confirma que a conexão está ativa.
print(spark_contexto)

# Imprime a versão do Spark que está sendo executada (exemplo: 4.0.1).
print(spark_contexto.version)

# ----------------------------------------------------------------------
# INICIALIZAÇÃO DE ALTO NÍVEL (SparkSession)
# ----------------------------------------------------------------------

# Cria ou recupera uma instância da SparkSession.
# .builder(): Inicia a construção da sessão.
# .getOrCreate(): Se já houver uma SparkSession ativa (conectada ao SparkContext),
#                 ele a retorna; caso contrário, cria uma nova.
# 'spark' é a variável principal que usaremos para todas as operações de DataFrame e SQL.
spark = SparkSession.builder.getOrCreate() # Create my_spark

# Imprime informações sobre a SparkSession (o objeto 'spark').
print(spark) # Print my_spark

# ----------------------------------------------------------------------
# CONFIGURAÇÃO DE CAMINHOS ROBUSTOS
# ----------------------------------------------------------------------

# Obtém o caminho absoluto do diretório onde o script Python atual está sendo executado.
# __file__: O caminho do script atual.
# os.path.abspath(): Converte o caminho para absoluto.
# os.path.dirname(): Retira o nome do arquivo, deixando apenas o diretório.
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define o nome do arquivo CSV de entrada que o Spark deve ler.
input_filename = "Test.csv"

# Define o nome da pasta de saída que o Spark criará para armazenar os resultados.
# O PySpark não salva em um único arquivo, mas sim em um diretório de partições.
output_foldername = "spark.csv" # Note que o Spark sempre cria uma pasta

# Combina o caminho do diretório do script com o nome do arquivo de entrada.
# Isso cria um caminho absoluto e compatível com todos os sistemas operacionais.
input_file_path = os.path.join(script_dir, input_filename)

# Combina o caminho do diretório do script com o nome da pasta de saída.
output_folder_path = os.path.join(script_dir, output_foldername)

# ----------------------------------------------------------------------
# LEITURA DE DADOS E OPERAÇÕES DE DATAFRAME
# ----------------------------------------------------------------------

# Lê o arquivo CSV a partir do caminho absoluto definido.
# .inferSchema=True: Pede ao Spark para analisar o arquivo e tentar adivinhar
#                    o tipo de dado correto para cada coluna (inteiro, string, float, etc.).
# .header=True: Informa ao Spark que a primeira linha do CSV contém os nomes das colunas (cabeçalhos).
dataset = spark.read.csv(input_file_path, inferSchema=True, header=True)

# Executa uma AÇÃO do Spark para buscar o primeiro registro (Row) do DataFrame.
# Como o resultado é um objeto Python (Row), usamos print() para exibir seu conteúdo no terminal.
print(dataset.head())

# Executa uma AÇÃO do Spark para contar o número total de registros (linhas de dados)
# no DataFrame (excluindo a linha de cabeçalho).
print(dataset.count())

# ----------------------------------------------------------------------
# SPARK SQL (Consultas e Estruturas)
# ----------------------------------------------------------------------

# Cria uma "tabela virtual" em memória com base nos dados do DataFrame 'dataset'.
# Isso permite que você execute consultas SQL diretamente contra o DataFrame usando a sintaxe SQL.
# 'tabela_temporaria' é o nome que a tabela SQL terá.
dataset.createOrReplaceTempView("tabela_temporaria")

# Imprime a lista de tabelas temporárias (e permanentes) disponíveis no catálogo do Spark.
# Isso confirma que 'tabela_temporaria' foi registrada com sucesso.
print(spark.catalog.listTables())

# Define a consulta SQL a ser executada na tabela temporária.
# A consulta seleciona as colunas 'longitude' e 'latitude' e limita o resultado a 3 registros.
query = "SELECT longitude, latitude FROM tabela_temporaria LIMIT 3"

# Executa a consulta SQL definida acima usando a SparkSession.
# O resultado da consulta é armazenado em um novo DataFrame, chamado 'saida'.
saida = spark.sql(query)

# Executa a AÇÃO final para exibir o conteúdo do DataFrame 'saida' no terminal,
# formatado como uma tabela.
saida.show()

query1 = "SELECT MAX(total_rooms) as maximo_quartos FROM tabela_temporaria"
maximo_quartos = spark.sql(query1)
pd_maximo_quartos = maximo_quartos.toPandas()
print("A quantidade máxima de quartos é: {}".format(pd_maximo_quartos["maximo_quartos"]))
qtd_maximo_quartos = int(pd_maximo_quartos.loc[0, "maximo_quartos"])

query2 = 'SELECT longitude, latitude FROM tabela_temporaria WHERE total_rooms = ' + str(qtd_maximo_quartos)
localizacao_maximo_quartos = spark.sql(query2)
pd_localizacao_maximo_quartos = localizacao_maximo_quartos.toPandas()
print(pd_localizacao_maximo_quartos.head())

import numpy as np
media = 0
desvio_padrao=0.1 
pd_temporario = pd.DataFrame(np.random.normal(media,desvio_padrao,100))
spark_temporario = spark.createDataFrame(pd_temporario)

print(spark.catalog.listTables())
spark_temporario.createOrReplaceTempView('nova_tabela_temporaria')

print(spark.catalog.listTables())

spark.stop()