class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco


import sqlite3

def conectar_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao

def criar_tabelas(conexao):
    cursor = conexao.cursor()

    # reiniciando as tabelas, pois se não sempre vai repetindo os dados da tabela. Na dúvida, retire esses 3 DROP, para ver os pedidos se repetindo a cada execução do programa.
    cursor.execute('''DROP TABLE Pedidos;''')
    cursor.execute('''DROP TABLE Livros;''')
    cursor.execute('''DROP TABLE Clientes;''')

    # criando as tabelas
    cursor.execute('''CREATE TABLE IF NOT EXISTS Livros (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   autor TEXT NOT NULL,
                   preco REAL NOT NULL)''')
    
    # criando as tabelas
    cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL)''')
    
    # quando uma tabela faz referencia à outra tabela, ela precisa ser criada depois que as outras já estejam criadas
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pedidos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   cliente_id INTEGER NOT NULL,
                   livro_id INTEGER NOT NULL,
                   quantidade INTEGER NOT NULL,
                   data_pedido TEXT NOT NULL,
                   FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
                   FOREIGN KEY (livro_id) REFERENCES Livros(id))''')
    
    conexao.commit()
    cursor.close()

def inserir_dados(conexao):
    cursor = conexao.cursor()

    # populando ou preenchendo a tabela Livro
    livros = [Livro("Python para Iniciantes", "John Doe", 
                39.99),
                Livro("Algoritmos e Estruturas de Dados", "Jane Smith", 49.99),
                Livro("Inteligência Artificial", "Alan Turing", 59.99)]
    
    # populando ou preenchendo a tabela Cliente
    clientes = [("Alice", "alice@example.com"),
                ("Bob", "bob@example.com"),
                ("Charlie", "charlie@example.com")]
    
    # populando ou preenchendo a tabela Pedido
    pedidos = [(1, 1, 2, "2023-06-15"),
                (2, 2, 1, "2023-06-16"),
                (3, 3, 3, "2023-06-17")]
    
    # o for pode ser substituido pelo método executemany()
    for livro in livros:
        cursor.execute('''INSERT INTO Livros (titulo, autor, preco) VALUES (:titulo, :autor, :preco)''', vars(livro))

    # usando o método executemany(), a principio é melhor, por digitar menos.
    cursor.executemany('''INSERT INTO Clientes (nome, email) VALUES (:nome, :email)''', clientes)

    # usando o método executemany()
    cursor.executemany('''INSERT INTO Pedidos (cliente_id, livro_id, quantidade, data_pedido) VALUES (:cliente_id, :livro_id, :quantidade, :data_pedido)''', pedidos)

    conexao.commit()
    cursor.close()

def exibir_pedidos(conexao):
    cursor = conexao.cursor()

    query = '''SELECT * FROM Pedidos'''

    cursor.execute(query)
    pedidos = cursor.fetchall()

    print("Pedidos:")
    for pedido in pedidos:
        print(pedido)
        

    cursor.close()

if __name__ == '__main__':
    conexao = conectar_banco("livraria.db")
    criar_tabelas(conexao)
    inserir_dados(conexao)
    exibir_pedidos(conexao)
    conexao.close()