import sqlite3 as conector
from data_base_8 import Veiculo, Marca

def recuperar_veiculos(conexao, cpf):
    # aquisição de cursor
    cursor = conexao.cursor()

    comando = '''SELECT * FROM Veiculo JOIN Marca ON Marca.id = Veiculo.marca WHERE Veiculo.proprietario = :cpf;'''

    cursor.execute(comando, (cpf,))

    veiculos = []
    registros = cursor.fetchall()
    
    for registro in registros:
        print("****", registro)
        marca = Marca(*registro[6:])
        veiculo = Veiculo(*registro[:5], marca)
        veiculos.append(veiculo)

    cursor.close()
    return veiculos