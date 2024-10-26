import sqlite3 as conector
from data_base_8 import Veiculo, Marca

# conexao com o banco
conexao = conector.connect("./meu_banco.db")
# aquisição de cursor
cursor = conexao.cursor()

# esse select irá selecionar tudo da tabela Veículo + tudo da tabela Marca
comando = '''SELECT * FROM Veiculo JOIN Marca ON Marca.id = Veiculo.marca;'''

# executar comando
cursor.execute(comando)
#registros recebe todos os dados da tabela Veículo + todos os dados da tabela Marca
registros = cursor.fetchall()

# for para percorrer todos os registros
for registro in registros:
    # como puxou todos os registros, aqui é feito a separação, marca recebe somente a partir do 6º elemento (6:)
    marca = Marca(*registro[6:])
    # aqui veiculo recebe até o 5º elemento (:5)
    veiculo = Veiculo(*registro[:5], marca)
    print("Placa:", veiculo.placa, ", Marca:", veiculo.marca.nome)