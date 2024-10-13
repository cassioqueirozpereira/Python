with open("dados.txt", encoding="utf-8") as arquivo:
    contador = 0
    print("\nTEXTO UTILIZADO\n")
    for linha in arquivo:
        print(repr(linha))
        if linha:
            contador += 1
    print("\nTotal de linhas = ", contador)

with open("dados.txt", encoding="utf-8") as arquivo:
    contador = 0
    print("\n\nTEXTO UTILIZADO APÓS STRIP\n")
    for linha in arquivo:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))
        if linha_limpa:
            contador += 1
    print("\nTotal de linhas = ", contador)

with open("dados.txt", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    print("\nTEXTO UTILIZADO\n")
    print(repr(texto))
    contador = texto.count("Olá")
    print("\nTotal de Olá = ", contador)