import os

nome = "diretorio_trabalho"

print("\nREMOVENDO UM DIRETÓRIO\n")

try:
    os.rmdir(nome)
    print("Diretório Removido!")
except PermissionError:
    print(f"Sem permissão para remover o diretório '{nome}'")
except FileNotFoundError:
    print(f"O diretório '{nome}' não existe")
except OSError as erro:
    print("Outro erro.")
    print(f"O diretório '{nome}' está vazio?")
    print("Descrição:", erro)

print("\nCRIANDO UM DIRETÓRIO\n")

try:
    os.mkdir(nome)
    print(f"Diretório '{nome}' criado!")
except PermissionError:
    print(f"Sem permissão para criar o diretório '{nome}'")
except FileExistsError:
    print(f"Já existe um diretório com o nome '{nome}'")