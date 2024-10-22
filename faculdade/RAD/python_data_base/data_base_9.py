import sqlite3 as conector
from data_base_8 import Pessoa

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

pessoa = Pessoa(10000000099, 'Maria', '1990-01-31', False)

comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?);'''

cursor.execute(comando, (pessoa.cpf,
                         pessoa.nome,
                         pessoa.data_nascimento,
                         pessoa.usa_oculos))

conexao.commit()

cursor.close()
conexao.close()