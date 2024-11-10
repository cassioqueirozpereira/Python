from segunda_forma_normal import connection_base, exportando_projeto, exportando_projeto_empregado

def create_tables():
    try:
        connection = connection_base()
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS PROJETO_3FN (
                    cod_proj VARCHAR(10),
                    tipo VARCHAR(25) NOT NULL,
                    descricao VARCHAR(30) NOT NULL,
                    PRIMARY KEY (cod_proj))''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS CATEGORIA_3FN (
                    categoria VARCHAR(3),
                    salario REAL NOT NULL,
                    PRIMARY KEY (categoria))''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS EMPREGADO_3FN (
                    cod_emp INTEGER,
                    nome VARCHAR(10) NOT NULL,
                    categoria VARCHAR(3),
                    PRIMARY KEY (cod_emp),
                    FOREIGN KEY (categoria) REFERENCES CATEGORIA_3FN (categoria)
                    )''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS PROJETO_EMPREGADO_3FN (
                    cod_proj VARCHAR(10),
                    cod_emp INTEGER,
                    data_inicio DATE NOT NULL,
                    tempo_alocado SMALLINT NOT NULL,
                    PRIMARY KEY (cod_proj, cod_emp),
                    FOREIGN KEY (cod_proj) REFERENCES PROJETO_3FN (cod_proj),
                    FOREIGN KEY (cod_emp) REFERENCES EMPREGADO_3FN (cod_emp))''')
        
        connection.commit()
        print("Tabelas criadas com sucesso!")

    except Exception as erro:
        print(f"Não foi possível criar as tebelas. Erro: {erro}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def enter_data():
    try:
        connection = connection_base()
        cursor = connection.cursor()

        projeto = exportando_projeto()

        categoria = [
            ("A1", 400.00),
            ("A2", 400.00),
            ("B1", 900.00)
        ]

        empregado = [
            (2146, "João", "A1"),
            (3145, "Silvio", "A2"),
            (6126, "José", "B1"),
            (1214, "Carlos", "A2"),
            (8191, "Mario", "A1"),
            (4112, "Gumercindo", "A2")
        ]

        projeto_empregado = exportando_projeto_empregado()

        cursor.executemany('''INSERT INTO PROJETO_3FN (cod_proj, tipo, descricao) VALUES (%s, %s, %s)''', projeto)

        cursor.executemany('''INSERT INTO CATEGORIA_3FN (categoria, salario) VALUES (%s, %s)''', categoria)

        cursor.executemany('''INSERT INTO EMPREGADO_3FN (cod_emp, nome, categoria) VALUES (%s, %s, %s)''', empregado)

        cursor.executemany('''INSERT INTO PROJETO_EMPREGADO_3FN (cod_proj, cod_emp, data_inicio, tempo_alocado) VALUES (%s, %s, %s, %s)''', projeto_empregado)

        connection.commit()
        print("Dados inseridos na tabela com sucesso!")
    
    except Exception as erro:
        print(f"Não foi possível inserir os dados na tabela. Erro: {erro}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    create_tables()
    enter_data()