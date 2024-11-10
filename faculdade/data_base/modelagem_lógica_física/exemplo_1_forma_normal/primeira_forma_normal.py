import psycopg2 as conector
from datetime import date

def conectar_banco():
    try:
        connection = conector.connect(
            database = "postgres",
            user="postgres",
            password="V0ucomerfruta",
            host="127.0.0.1",
            port="5432"
        )
        return connection

    except (Exception, conector.Error) as error:
        if connection:
            print(f"Falha ao se conectar ao banco: {error}")

def delete_tabela():
    connection = conectar_banco()
    cursor = connection.cursor()
    cursor.execute('''DROP TABLE PROJETO_EMPREGADO_1FN''')
    cursor.execute('''DROP TABLE PROJETO_1FN''')
    connection.commit()
    cursor.close()
    connection.close()
def create_tables():
    try:
        connection = conectar_banco()
        cursor = connection.cursor()
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS PROJETO_1FN (
                    cod_proj VARCHAR(10),
                    tipo VARCHAR(25) NOT NULL,
                    descricao VARCHAR(30) NOT NULL,
                    PRIMARY KEY (cod_proj))''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS PROJETO_EMPREGADO_1FN (
                    cod_proj VARCHAR(10),
                    cod_emp INT,
                    nome VARCHAR(20) NOT NULL,
                    categoria VARCHAR(3) NOT NULL,
                    salario REAL NOT NULL,
                    data_inicio DATE,
                    tempo_alocado SMALLINT NOT NULL,
                    PRIMARY KEY (cod_emp, cod_proj),
                    FOREIGN KEY (cod_proj) REFERENCES PROJETO_1FN (cod_proj)
                    )''')

        connection.commit()
        print("Tabelas criadas com sucesso")
    except Exception as erro:
        print(f"Não foi possível criar as tabelas. Erro: {erro}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def exportando_projeto():
    try:
        projeto = [
                ("LSC001", "Novo Desenvolvimento", "Sistema de Estoque"),
                ("PAG02", "Manutenção", "Sistema de RH")
            ]
        return projeto
    except Exception as erro:
        print("Nâo foi possível exportar a variável projeto!")

# função para inserir os dados na tabela
def inserir_dados():
    try:
        # conectando ao banco
        connection = conectar_banco()
        # ativando o cursor
        cursor = connection.cursor()

        # armazenando os dados a serem inseridos na tabela em uma variável
        projeto_empregado = [
            ("LSC001", 2146, "João", "A1", 400.00, date(1991, 11, 1), 24),
            ("LSC001", 3145, "Silvio", "A2", 400.00, date(1991, 10, 2), 24),
            ("LSC001", 6126, "José", "B1", 900.00, date(1992, 10, 3), 18),
            ("LSC001", 1214, "Carlos", "A2", 400.00, date(1992, 10, 4), 18),
            ("LSC001", 8191, "Mario", "A1", 400.00, date(1992, 11, 1), 12),
            ("PAG02", 8191, "Mario", "A1", 400.00, date(1993, 5, 1), 12),
            ("PAG02", 4112, "João", "A2", 400.00, date(1991, 1, 4), 24),
            ("PAG02", 6126, "Gumercindo", "B1", 900.00, date(1992, 12, 1), 12)
        ]

        # executemany executa o processo quantas vezes forem necessárias.
        cursor.executemany('''INSERT INTO PROJETO_1FN (cod_proj, tipo, descricao) VALUES (%s, %s, %s)''', exportando_projeto())

        cursor.executemany('INSERT INTO PROJETO_EMPREGADO_1FN (cod_proj, cod_emp, nome, categoria, salario, data_inicio, tempo_alocado) VALUES (%s, %s, %s, %s, %s, %s, %s)', projeto_empregado)

        # salvando as ações no banco de dados
        connection.commit()

        print("Dados inseridos com sucesso!")
    except Exception as erro:
        print(f"Não foi possível inserir os dados na tabela. Erro: {erro}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def mostrar_tabela():
    try:
        connection = conectar_banco()
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM PROJETO_EMPREGADO_1FN''')
        tabela = cursor.fetchall()
        for linha in tabela:
            print(linha)
        print("Tabela acessada com sucesso!")
    except Exception as erro:
        print(f"Não foi possível mostrar a tabela. Erro: {erro}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
# se nome main
if __name__ == "__main__":
    create_tables()
    inserir_dados()