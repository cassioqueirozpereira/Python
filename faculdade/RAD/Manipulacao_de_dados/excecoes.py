print("Abrindo um arquivo")

try:
    open("teste.txt", 'r')
    print("Arquivo aberto")
except FileNotFoundError as erro:
    print("\nArquivo inexistente")
    print("Descrição:", erro)

print("\nFIM DO PROGRAMA")

print("\nNOVO PROGRAMA\n\nAbrindo um arquivo\n")

try:
    open("C:\\Windows\\System32\\teste.pdf", 'w')
    print("Arquivo aberto")
except FileNotFoundError as erro:
    print("\nArquivo inexistente")
    print("Descrição: ", erro)
except PermissionError as erro:
    print("\nSem permissão para acessar o arquivo")
    print("Descrição:", erro)

print("\nFIM DO PROGRAMA")
