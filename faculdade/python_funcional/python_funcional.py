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
print("\nTerceiro exemplo. Operator, soma somente dois números\n")

# operator tem a função add, sub, mul, truediv
import operator

print(operator.add(10, 20))

# quarto exemplo
print("\nQuarto exemplo. Reduce soma todos os elementos da lista\n")

from functools import reduce

print(reduce(operator.add, (numero)))

print(reduce(operator.concat, ["\nAprendendo reduce"]))