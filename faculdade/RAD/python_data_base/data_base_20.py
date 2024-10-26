import sqlite3 as conector
from data_base_8 import Pessoa
from data_base_19 import recuperar_veiculos

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

comando = '''SELECT * FROM Pessoa;'''
cursor.execute(comando)

pessoas = []
reg_pessoas = cursor.fetchall()

for reg_pessoa in reg_pessoas:
    pessoa = Pessoa(*reg_pessoa)
    pessoa.veiculos = recuperar_veiculos(conexao, pessoa.cpf)
    pessoas.append(pessoa)

for pessoa in pessoas:
    print(pessoa.nome)
    if pessoa.veiculos:
        for veiculo in pessoa.veiculos:
            print(f"\t PLACA: {veiculo.placa} MARCA: {veiculo.marca.nome}")
    else:
        print(f"\t {pessoa.nome} não tem veículo.")

cursor.close()
conexao.close()