import sqlite3 as conector

# função para conectar ao banco
def conectar_banco(nome_banco):
    conexao = conector.connect(nome_banco)
    return conexao

# função para inserir os dados na tabela
def inserir_dados(conexao):
    # ativando o cursor
    cursor = conexao.cursor()

    # armazendo os dados a serem inseridos na tabela em uma variável
    veiculo = [
        ("AAA0001", 2001, "Prata", 1.0, 10000000099, 1),
        ("BAA0002", 2002, "Preto", 1.4, 20000000099, 1),
        ("CAA0003", 2003, "Branco", 2.0, 30000000099, 2),
        ("DAA0004", 2004, "Azul", 2.2, 40000000099, 2)
    ]

    marca = [
        ("Marca A", "MA"),
        ("Marca B", "MB")
    ]

    # executemany (executa o processo quantas vezes forem necessarias, nesse caso 4 vezes, pois são 4 linhas adicionadas na tabela.) INSERT INTO Veiculo (inserir em Veiculo) VALUES (valores)
    cursor.executemany('INSERT INTO Veiculo(placa, ano, cor, motor, proprietario, marca) VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca)', veiculo)

    cursor.executemany('INSERT INTO Marca(nome, sigla) VALUES (:nome, :sigla)', marca)

    # salvando as ações no banco de dados
    conexao.commit()
    #fechando o cursor
    cursor.close()

# se nome main
if __name__ == "__main__":
    # conexão recebe a função conectar_banco, que envia como parâmetro o nome_banco("./meu_banco.db")
    conexao = conectar_banco("./meu_banco.db")
    # a função inserir dados é acionada, enviando como parâmetro a função conectar_banco
    inserir_dados(conexao)
    # fechando conexao
    conexao.close()