import sqlite3 as conector

conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

comando1 = '''UPDATE Pessoa SET oculos = 1;'''
cursor.execute(comando1)

comando2 = '''UPDATE Pessoa SET oculos = ? WHERE cpf = 20000000099;'''
cursor.execute(comando2, (False,))

comando3 = '''UPDATE Pessoa SET nome = :nome WHERE cpf = :cpf;'''
cursor.execute(comando3, {"nome": 'João', "cpf": 12345678900})

conexao.commit()

cursor.close()
conexao.close()