from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import os
import sys

# 1. Configuração de Caminhos
# Obtém o diretório ONDE O SCRIPT ESTÁ
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define os nomes dos arquivos
input_filename = "arquivo.txt"
output_foldername = "qtd_spark.csv" # Note que o Spark sempre cria uma pasta

# Cria os caminhos absolutos
input_file_path = os.path.join(script_dir, input_filename)
output_folder_path = os.path.join(script_dir, output_foldername)


# 2. Inicia uma sessão Spark
spark = SparkSession.builder.appName("WordCountSpark").getOrCreate()

# 3. Carrega o arquivo de texto (usando o caminho absoluto para evitar erros)
# Se o arquivo não for encontrado, ele dará o erro correto de caminho
try:
    df = spark.read.text(input_file_path)
except Exception as e:
    print(f"ERRO: Não foi possível ler o arquivo. Verifique se ele existe em: {input_file_path}")
    spark.stop()
    sys.exit(1)


# 4. Mapeamento e Redução (Seu código de contagem de palavras)
words_df = df.select(
    F.explode(F.split(F.col("value"), r"[\s.]+")).alias("word")
).filter(F.col("word") != "")

word_counts_df = words_df.groupBy(F.lower(F.col("word")).alias("word")).count().sort(F.col("count").desc())

# 5. Salva o resultado
# Usa o caminho absoluto para salvar NO MESMO DIRETÓRIO DO SCRIPT
print(f"Salvando resultados no diretório: {output_folder_path}")
word_counts_df.write.mode("overwrite").csv(output_folder_path)

# 6. Para a sessão Spark
spark.stop()
print("Processamento Spark concluído.")

# Seu resultado estará na pasta 'qtd_spark.csv' dentro do diretório do script!