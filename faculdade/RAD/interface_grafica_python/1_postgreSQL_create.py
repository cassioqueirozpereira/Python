import psycopg2 as conector

connection = conector.connect(database = "postgres", user = "postgres", password = "senha123", host = "127.0.0.1", port = "5432")

print("Database connection successfully opened!")

cursor = connection.cursor()

cursor.execute('''CREATE TABLE Agenda (
               ID INT PRIMARY KEY NOT NULL,
               Nome TEXT NOT NULL,
               Telefone CHAR(12));''')
print("table created successfully")
connection.commit()

connection.close()
cursor.close()
