import os

print("\nREMOVER ARQUIVO\n")

arquivo_a_remover = "arquivo_a_remover.txt"

try:
    os.remove(arquivo_a_remover)
    print(f"O arquivo {arquivo_a_remover} foi removido com sucesso.")
except FileNotFoundError as erro:
    print(f"O arquivo {arquivo_a_remover} não foi encontrado.")
    print("Descrição:", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print("Descrição:", erro)
except IsADirectoryError as erro:
    print("Remove serve apenas para arquivos")
    print("Descrição:", erro)
except Exception as erro:
    print(f"Ocorreu um erro ao remover o arquivo: {erro}")

print("\n RENOMEAR ARQUIVO\n")

nome_antigo = "arquivo_novo.txt"
nome_novo = "dados.txt"

try:
    os.rename(nome_antigo, nome_novo)
    print(f"O arquivo {nome_antigo} foi renomeado para {nome_novo}.")
except FileNotFoundError:
    print(f"O arquivo {nome_antigo} não foi encontrado")
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print("Descrição:", erro)
except FileExistsError as erro:
    print("Já existe um arquivo com esse nome")
    print("descrição:", erro)
except Exception as e:
    print(f"Ocorreu um erro ao renomear o arquivo: {e}")

print("\nFIM DO PROGRAMA\n")

