import sqlite3 as conector

# abertura de conexão
conexao = conector.connect("URL SQLITE")

# aquisição de um cursor
cursor = conexao.cursor()

# execução de comandos: SELECT...CREATE...
cursor.execute("...")
cursor.fetchall()

# salvar os comandos no data base
conexao.commit()

# fechamento das conexões, ou finalização
cursor.close()
conexao.close()


import psycopg2 as conector

# abertura de conexão
conexao = conector.connect("URL PostgreSQL")

# aquisição de um cursor
cursor = conexao.cursor()

# execução de comandos: SELECT...CREATE...
cursor.execute("...")
cursor.fetchall()

# salvar os comandos no data base
conexao.commit()

# fechamento das conexões, ou finalização
cursor.close()
conexao.close()


import mysql.connector as conector

# abertura de conexão
conexao = conector.connect("URL MySQL")

# aquisição de um cursor
cursor = conexao.cursor()

# execução de comandos: SELECT...CREATE...
cursor.execute("...")
cursor.fetchall()

# salvar os comandos no data base
conexao.commit()

# fechamento das conexões, ou finalização
cursor.close()
conexao.close()