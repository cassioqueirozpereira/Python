import psycopg2 as conector

try:
    connection = conector.connect(
        database="postgres",
        user="postgres",
        password="senha123",
        host="127.0.0.1",
        port="5432",
        options="-c client_encoding=UTF8"
    )

    cursor = connection.cursor()

    # Criar uma tabela simples para teste
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Teste (
            ID SERIAL PRIMARY KEY,
            Nome TEXT NOT NULL
        );
    ''')

    # Inserir um valor simples
    cursor.execute("INSERT INTO Teste (Nome) VALUES (%s)", ("Teste com acentuação é legal",))

    connection.commit()

    print("Dados inseridos com sucesso!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
