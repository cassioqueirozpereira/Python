import psycopg2

connection = psycopg2.connect(database = "postgres", user = "postgres", password = "V0ucomerfruta", host = "127.0.0.1", port = "5432")

cursor = connection.cursor()

cursor.execute('''DROP TABLE Teste;''')

connection.commit()

print("Delete performed successfully")

connection.close()
cursor.close()