# programa que transforma os textos recebidos com letras minúsculas e maiúsculas, em letras todas maiúsculas.

def main():
    print("Digite seu texto. Para terminar e salvar o arquivo, em uma nova linha digite somente a palavra 'sair': ")
    # cria a variável frases que irá caber tudo.
    frases = []

    # looping infinito, para 'frases' receber todo o texto
    while True:
        # entrada recebe o texto todo até o enter.
        entrada = input("> ")
        # se a frase for somente a palabra sair
        if entrada.lower() == "sair":
            # encerre o looping
            break
        # se não a variável frases adiciona mais esse texto.
        frases.append(entrada)

    # abre o arquivo "meu_arquivo.txt", como arquivo
    with open("meu_arquivo.txt", "w") as arquivo:
        # para cada parágrafo armazenado na variável 'frases'
        for frase in frases:
            # separe como parágrafo (assim deixando igual o texto digitado pelo usuário, cada parágrafo com seu enter)
            arquivo.write(frase + "\n")

    print("Arquivo original criado. Agora vamos manipular os dados.")

    # cria uma nova variável, para armazenar o texto na variável frases, só que em maiúsculo.
    dados_modificados = []

    # abre o "meu_arquivo.txt", no modo leitura, como arquivo
    with open("meu_arquivo.txt", "r") as arquivo:
        # para cada linha no arquivo
        for linha in arquivo:
            # exemplo de manipulação, tira os espaços extras no final da frase 'strip()'(exemplo. cassio '        '(espaço extra no final da frase que será removido))converter para maiúscula 'upper()'
            dados_modificados.append(linha.strip().upper())

    # abre o "meu_arquivo.txt", no modo escrita, em portugues(para ter acentos), como arquivo
    with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
        # para cada linha na variável dados_modificados
        for linha in dados_modificados:
            # escreva cada linha com enter(faça os parágrafos), no arquivo "meu_arquivo.txt"
            arquivo.write(linha + "\n")

    print("O arquivo foi sobrescrito com os dados modificados.")

if __name__ == "__main__":
    main()