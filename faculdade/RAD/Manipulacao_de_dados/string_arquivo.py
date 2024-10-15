# arquivo.read() lê tudo que tem no arquivo
arquivo = open("dados.txt", "r", encoding="utf-8")

conteudo = arquivo.read()

print("Tipo de conteúdo: ", type(conteudo))

print("Conteúdo retornado pelo read: ", repr(conteudo))

print("fim do arquivo.read()\n")

arquivo.close()

# arquivo.readline() lê somente a primeira linha, se chamado novamente lê a próxima linha e assim sucessivamente.
arquivo = open("dados.txt", "r", encoding="utf-8")

conteudo = arquivo.readline()

print("Tipo de conteúdo: ", type(conteudo))

print("Conteúdo retornado pelo readline: ", repr(conteudo))

proximo_conteudo = arquivo.readline()

print("Próximo conteúdo retornado pelo readline: ", repr(proximo_conteudo))

proximo_conteudo = arquivo.readline()

print("Próximo conteúdo retornado pelo readline: ", repr(proximo_conteudo))

print("fim do arquivo.readline()\n")

arquivo.close()

# arquivo.readlines() lê todas as linhas, porém já não é mais do tipo string "str", agora será do tipo lista "list"
arquivo = open("dados.txt", "r", encoding="utf-8")

conteudo = arquivo.readlines()

print("Tipo de conteúdo: ", type(conteudo))

print("Conteúdo retornado pelo readlines: ", repr(conteudo))

print("fim do arquivo.readlines()\n")

arquivo.close()