import os

# abrindo o arquivo no modo escrita
arquivo = open('exemplo.txt', 'w', encoding='utf-8')

# exibindo os atributos do arquivo
print("Nome do arquivo: ", arquivo.name)
print("Modo de abertura: ", arquivo.mode)
print("O arquivo está fechado?: ", arquivo.closed)

# escrevendo no arquivo
arquivo.write("Olá mundo!")

# encerrando o programa
# exit()
# fechando o arquivo
arquivo.close()

# verificando se o arquivo está fechado
print("O arquivo está fechado agora?: ", arquivo.closed)

# encerrando o programa
# exit()

# exibindo caminho relativo e absoluto
relpath = os.path.realpath('exemplo.txt')
abspath = os.path.abspath('exemplo.txt')

print("Caminho relativo: ", relpath)
print("Caminho absoluto: ", abspath)