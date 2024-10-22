import sqlite3 as conector
from data_base_8 import Pessoa

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

pessoa = Pessoa(20000000099, 'José', '1990-02-28', False)

comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (:cpf, :nome, :data_nascimento, :usa_oculos);'''

cursor.execute(comando, {
    "cpf": pessoa.cpf,
    "nome": pessoa.nome,
    "data_nascimento": pessoa.data_nascimento,
    "usa_oculos": pessoa.usa_oculos
})

conexao.commit()

cursor.close()
conexao.close()