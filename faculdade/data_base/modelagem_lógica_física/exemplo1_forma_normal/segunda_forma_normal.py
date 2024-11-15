import psycopg2 as conector
from datetime import date
from primeira_forma_normal import exportando_projeto

def connection_base():
    try:
        connection = conector.connect(
            database = "TABLE_NORMALIZATION",
            user = "postgres",
            password = "V0ucomerfruta",
            host = "127.0.0.1",
            port = "5432"
        )
        return connection
    
    except Exception as erro:
        print(f"Não foi possível se conectar ao banco. Erro: {erro}")

def create_tables():
    try:
        connection = connection_base()
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS PROJETO_2FN (
                       cod_proj VARCHAR(10),
                       tipo VARCHAR(25),
                       descricao VARCHAR(30),
                       PRIMARY KEY (cod_proj))''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS EMPREGADO_2FN (
                       cod_emp INTEGER,
                       nome VARCHAR(10) NOT NULL,
                       categoria VARCHAR(3) NOT NULL,
                       salario REAL NOT NULL,
                       PRIMARY KEY (cod_emp))''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS PROJETO_EMPREGADO_2FN (
                       cod_proj VARCHAR(10),
                       cod_emp INTEGER,
                       data_inicio DATE NOT NULL,
                       tempo_alocado SMALLINT NOT NULL,
                       PRIMARY KEY (cod_proj, cod_emp),
                       FOREIGN KEY (cod_proj) REFERENCES PROJETO_2FN (cod_proj),
                       FOREIGN KEY (cod_emp) REFERENCES EMPREGADO_2FN (cod_emp))''')
        
        connection.commit()
        print(f"Tabelas criadas com sucesso!")

    except Exception as erro:
        print(f"Nâo foi possível criar as tabelas. Erro: {erro}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def exportando_projeto_empregado():
    try:
        projeto_empregado = [
                ("LSC001", 2146, date(1991, 11, 1), 24),
                ("LSC001", 3145, date(1991, 10, 2), 24),
                ("LSC001", 6126, date(1992, 10, 3), 18),
                ("LSC001", 1214, date(1992, 10, 4), 18),
                ("LSC001", 8191, date(1992, 11, 1), 12),
                ("PAG02", 8191, date(1993, 5, 1), 12),
                ("PAG02", 4112, date(1991, 1, 4), 24),
                ("PAG02", 6126, date(1992, 12, 1), 12)
            ]
        return projeto_empregado
    
    except Exception as erro:
        print(f"Não foi possível exportar projeto_empregado. Erro: {erro}")

def enter_data():
    try:
        connection = connection_base()
        cursor = connection.cursor()
        
        projeto = exportando_projeto()

        empregado = [
            (2146, "João", "A1", 400.00),
            (3145, "Silvio", "A2", 400.00),
            (6126, "José", "B1", 900.00),
            (1214, "Carlos", "A2", 400.00),
            (8191, "Mario", "A1", 400.00),
            (4112, "Gumercindo", "A2", 400.00)
        ]

        projeto_empregado = exportando_projeto_empregado()

        cursor.executemany('''INSERT INTO PROJETO_2FN (cod_proj, tipo, descricao) VALUES (%s, %s, %s)''', projeto)

        cursor.executemany('''INSERT INTO EMPREGADO_2FN (cod_emp, nome, categoria, salario) VALUES (%s, %s, %s, %s)''', empregado)

        cursor.executemany('''INSERT INTO PROJETO_EMPREGADO_2FN (cod_proj, cod_emp, data_inicio, tempo_alocado) VALUES (%s, %s, %s, %s)''', projeto_empregado)

        connection.commit()
        print("Dados inseridos com sucesso!")
    
    except Exception as erro:
        print(f"Não foi possível inserir dados na tabela. Erro: {erro}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    create_tables()
    enter_data()