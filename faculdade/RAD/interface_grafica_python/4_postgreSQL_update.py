import psycopg2

connection = psycopg2.connect(database = "postgres", user = "postgres", password = "V0ucomerfruta", host = "127.0.0.1", port = "5432")

cursor = connection.cursor()

cursor.execute('''UPDATE AGENDA SET telefone = '02188888888' where id = 1''')

connection.commit()

print("Record successfully updated")

connection.close()
cursor.close()