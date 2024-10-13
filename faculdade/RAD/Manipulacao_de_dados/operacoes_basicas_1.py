import os

arquivo1 = open("dados1.txt", 'w', encoding='utf-8')
print(os.path.abspath(arquivo1.name))
# arquivo2 = open("d:/OneDrive/yduqs/python/" "manipulação de dados/exemplos/dados1.txt")
arquivo1.write("Olá mundo!!!")

print(os.path.relpath(arquivo1.name))
print(arquivo1)

arquivo1.close()