# Essa classe possui o método CRUD
import psycopg2

class AppBD:
    def __init__(self):
        print("Método Construtor")
    
    # iniciar conexão com o banco de dados
    def abrir_conexao(self):
        try:
            self.connection = psycopg2.connect(
                                    user = "postgres",
                                    password = "V0ucomerfruta",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "postgres")
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)
    
    # selecionar todos os produtos
    def selecionar_dados(self):
        try:
            self.abrir_conexao()
            cursor = self.connection.cursor()

            print("Selecionando todos os produtos")
            sql_select_query = '''SELECT * FROM public."PRODUTO"'''

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)
        
        except (Exception, psycopg2.Error) as error:
            print("Error in select operation", error)
        
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada")
        
        return registros
    
    # inserir produtos
    def inserir_dados(self, codigo, nome, preco):
        try:
            self.abrir_conexao()
            cursor = self.connection.cursor()
            postgres_insert_query = '''INSERT INTO public."PRODUTO" ("CODIGO", "NOME", "PRECO") VALUES (%s, %s, %s)'''
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "registro inserido com sucesso na tabela PRODUTO")

        except psycopg2.IntegrityError as integrity_error:
            # Desfaz a transação
            self.connection.rollback()
            print("Erro: Código do produto já existe.", integrity_error)
            # Levanta a exceção para que possa ser tratada na interface
            raise

        except (Exception, psycopg2.Error) as error:
            print("Falha ao inserir registro na tabela PRODUTO:", error)
            # Levanta a exceção para que possa ser tratada na interface
            raise

        finally:
            if cursor:
                # Fechamento do cursor
                cursor.close()
            if self.connection:
                # Fechamento da conexão
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")




    # atualizar produto
    def atualizar_dados(self, codigo, nome, preco):
        try:
            self.abrir_conexao()
            cursor = self.connection.cursor()

            print("Registro antes da atualização")
            sql_select_query = '''SELECT * FROM public."PRODUTO" where "CODIGO" = %s'''
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
            # atualizar registro
            sql_update_query = '''UPDATE public."PRODUTO" SET "NOME" = %s, "PRECO" = %s WHERE "CODIGO" = %s'''
            cursor.execute(sql_update_query, (nome, preco, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso!")
            print("Registro depois da atualização")
            cursor.execute(sql_select_query, (codigo,))
            print(record)
        
        except (Exception, psycopg2.Error) as error:
            print("Erro na atualização", error)
        
        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o postgreSQL foi fechada.")
    
    # excluir produto
    def excluir_dados(self, codigo):
        try:
            self.abrir_conexao()
            cursor = self.connection.cursor()
            # atualizar registro
            sql_delete_query = '''DELETE FROM public."PRODUTO" WHERE "CODIGO" = %s'''
            cursor.execute(sql_delete_query, (codigo,))

            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluido com sucesso!")

        except (Exception, psycopg2.Error) as error:
            print("Erro na exclusão", error)

        finally:
            # closing database connection
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o postgreSQL foi fechada")