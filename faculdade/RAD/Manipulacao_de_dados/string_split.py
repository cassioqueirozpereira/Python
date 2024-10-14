# exemplo 1, onde o split irá separar as palavras pelo espaço' '
frase_1 = "Eu amo comer amoras no café da manhã"

lista_1 = frase_1.split()
print("\nExemplo 1\n")
print(lista_1)

# exemplo 2, para deixar claro que o split separa as palavras com espaço ' ', independente de quantos espaços tiver entre uma palavra e outra.
frase_2 = "Amora abacaxi     abacate       banana"

lista_2 = frase_2.split()
print("\nExemplo 2\n")
print(lista_2)

# exemplo 3, por padão o split usa os espaços para separar, mas caso não houver espaço, mas outra coisa separando as palavras, você só precisa colocar dentro do parenteses() o que irá definir a separação do argumento.
frase_3 = "Carro-moto-avião"

lista_3 = frase_3.split("-")
print("\nExemplo 3\n")
print(lista_3)

# exemplo 4, contador de palavras em uma frase
print("\nExemplo 4\n")
# resultado obtido utilizando o método count diretamente, desse modo ele conta toda vez que aparece amo, mesmo que esteja dentro de outra palavra, neste caso ele conta o amo dentro da palavra amoras tbm.
print("Contagem direta: ", frase_1.count("amo"))

# resultado obtido utilizando a quebra da frase em palavras
contador = 0
for linha in lista_1:
    if linha == "amo":
        contador += 1
print("\nContagem correta: ", contador)

# texte meu que deu certo, sem precisar utilizar o for para contar na lista, método mais agil.
print("\ncontagem texte: ", lista_1.count("amo"))