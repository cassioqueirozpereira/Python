import psycopg2

connection = psycopg2.connect(database = "postgres", user = "postgres", password = "senha123", host = "127.0.0.1", port = "5432")

cursor = connection.cursor()

cursor.execute('''Delete from public."AGENDA" where "id" = 1''')

print("Delete performed successfully")

connection.close()
cursor.close()