import psycopg2

connection = psycopg2.connect(database = "postgres", user = "postgres", password = "senha123", host = "127.0.0.1", port = "5432")

print("Database connection successfully opened")

cursor = connection.cursor()

cursor.execute('''INSERT INTO public."AGENDA" ("id", "nome", "telefone") VALUES (1, "Pessoa 1", "021999999999")''')

connection.commit()

print("insertion performed successfully!")

connection.close()
cursor.close()