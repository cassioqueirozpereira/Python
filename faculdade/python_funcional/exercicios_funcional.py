# utilizar programação funcional para transformar todos os nomes em maiúsculas
print("\nMaiúsculo funcional")

veiculos = ["avião", "carro", "navio", "ônibus"]

funcional_maiuscula = lambda x: str.upper(x)

veiculos_maiusculos = list(map(funcional_maiuscula, veiculos))

print(f"\nPalavras maiúsculas = {veiculos_maiusculos}")


# utilizar programa funcional para imprimir apenas os números pares
print("\n\nImprimir somente os pares da lista")

lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

funcional_par = lambda x: x % 2 == 0

print(f"\nteste de funcional_par(5) = {funcional_par(5)}")

pares = list(filter(funcional_par, lista))

print(f"\nlista de números pares = {pares}")


# utilizar programa funcional para arredondar os valores da lista de números na mesma ordem da lista de precisão
print("\n\nArredonda uma lista de números, com uma lista de precisão")

lista_num = [9.56783, 7.57568, 3.00914, 6.2321]

lista_precis = [2, 2, 3, 3]

arredondamento = lambda x, y: round(x, y)

resultado = list(map(arredondamento, lista_num, lista_precis))

print(f"\nOs números antes do arredondamento: {lista_num}. Aplicando a lista de precisão {lista_precis}, os números ficam: {resultado}")


# utilizar programação funcional para somar todos os números de uma lista
print("\n\nSomando todos os números de uma lista")

from functools import reduce

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = lambda x, y: x + y

total = reduce(soma, numero)

print(f"\nO total da soma da lista é: {total}")