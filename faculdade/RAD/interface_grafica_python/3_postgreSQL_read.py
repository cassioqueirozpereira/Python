import psycopg2

connection = psycopg2.connect(database = "postgres", user = "postgres", password = "senha123", host = "127.0.0.1", port = "5432")

print("Database connection successfully opened!")

cursor = connection.cursor()

cursor.execute('''select * from public."AGENDA" where "id" = 1''')

registro = cursor.fetchone()

print(registro)
connection.commit()
print("Selection performed successfully")

connection.close()
cursor.close()