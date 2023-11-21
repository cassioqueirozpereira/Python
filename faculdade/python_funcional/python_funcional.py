# exemplo imperativo
print("\nPrimeiro exemplo")
numero = [1, 2, 3, 4]

total = 0

for num in numero:
    total += num

print("\nO total é:", total)

# mesmo exemplo funcional
print("\n\nPrimeiro exemplo funcional")

print("\nO total é: ", sum(numero))


# segundo exemplo imperativo
print("\n\nSegundo exemplo")

if True:
    print("\nTudo certo")
else:
    print("\nops")

# segundo exemplo funcional
print("\nSegundo exemplo funcional")
print("\nTudo certo" if True else "\nops")


# exemplo de mutabilidade (onde a variável total muda seu valor)
print("\nExemplo de mutabilidade\n")
def sum(numero):
    total = 0
    for num in numero:
        total += num
    return total

print(sum(numero))

# mesmo exemplo funcional
print("\nMesmo exemplo funcional\n")
def sum(numero):
    if not numero:
        return 0
    primeiro = numero[0]
    resto = numero[1:]
    return primeiro + sum(resto)

print(sum(numero))


# segundo exemplo de mutabilidade
print("\n\nSegundo exemplo de mutabilidade\n")

lista = ["civic"]

lista.append("onix")

print(lista)

# segundo exemplo funcional
print("\nMesmo exemplo funcional\n")

lista = ["civic"]

nova_lista = lista + ["onix"]

print(nova_lista)


# terceiro exemplo
print("\n\nTerceiro exemplo. Operator, soma somente dois números\n")

# operator tem a função add, sub, mul, truediv
import operator

print(operator.add(10, 20))


# quarto exemplo
print("\n\nQuarto exemplo. Reduce e operator, soma todos os elementos da lista\n")

from functools import reduce

print(reduce(operator.add, (numero)))

print(reduce(operator.concat, ["\nAprendendo reduce"]))


# primeiro exemplo de partial
print("\n\nExemplo de uma função com partial, onde se soma 1 ao parâmetro passado")
from functools import partial

soma_1 = partial(operator.add, 1)
print(f"\nO parâmetro passado é 5, logo a resposta é: {soma_1(5)}")

# exemplo com dados passados pelo usuário que eu implementei
print("\nExemplo que eu implementei com dados injetados pelo usuário")
valor = (eval(input("\nDigite um número: ")))
somador = eval(input("Digite quanto será adicionado ao número: "))
soma_somador = partial(operator.add, somador)
print(f"\nO número que vc digitou é: {valor}, seu número {valor} + {somador} é: {soma_somador(valor)}")

# segundo exeplo, sem utilizar o partial, nesse exemplo criamos uma classe pessoa, onde é atribuido a ela os atributos nome e idade.
print("\nSegundo exemplo sem partial")
import collections
from operator import attrgetter

pessoa = collections.namedtuple("pessoa", "nome idade")
pessoas = [pessoa("Joâo", 40), pessoa("Ana", 20), pessoa("Renata", 25)]

print(sorted(pessoas, key=attrgetter("nome")))
print(sorted(pessoas, key=attrgetter("idade")))

# segundo exemplo com partial
print("\nSegundo exemplo com partial")
sort_nome = partial(sorted, key=attrgetter("nome"))
sort_idade = partial(sorted, key=attrgetter("idade"))

print(sort_nome(pessoas))
print(sort_idade(pessoas))