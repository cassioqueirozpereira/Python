import sqlite3 as conector
from data_base_8 import Pessoa

# conexão com um detector de types
conexao = conector.connect("./meu_banco.db", detect_types = conector.PARSE_DECLTYPES)
cursor = conexao.cursor()

# função para converter números bytes em booleano
def converter_booleano(dado):
    # verifica se o dado é do type bytes
    if isinstance (dado, bytes):
        # converte para string
        dado = dado.decode()
        return True if dado == '1' else False
    return True if dado == 1 else False

conector.register_converter("BOOLEAN", converter_booleano)

comando = '''SELECT * FROM Pessoa WHERE oculos = :usa_oculos;'''

cursor.execute(comando, {"usa_oculos": True})

registros = cursor.fetchall()
for registro in registros:
    pessoa = Pessoa(*registro)
    print("cpf:", type(pessoa.cpf), pessoa.cpf)
    print("nome:", type(pessoa.nome), pessoa.nome)
    print("nascimento", type(pessoa.data_nascimento), pessoa.data_nascimento)
    print("oculos:", type(pessoa.usa_oculos), pessoa.usa_oculos)

cursor.close()
conexao.close()