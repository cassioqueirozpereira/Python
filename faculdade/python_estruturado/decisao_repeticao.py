# verificar qual número é o maior
print("\nMaior")
a = 10
b = 20
maior = a
if (b > maior):
    maior = b
print(f"O maior número é o {maior}")

# verificar se o número é par ou ímpar
print("\nPar ou ímpar")
a = 11
if (a % 2 == 0):
    print(f"O número {a} é par")
else:
    print(f"O número {a} é ímpar")

# verificar se o aluno está aprovado, em recuperação ou reprovado
print("\nAprovado, em recuperação ou reprovado?")
media = 5
if (media >= 7):
    print("O aluno está aprovado")
elif (media >= 5):
    print("O aluno está de recuperação")
else:
    print("O aluno está reprovado")

# verifica o valor de unidades e da desconto conforme a quantidade
print("\nDesconto")
preco_unitario = 10
desconto10 = 0.9
desconto20 = 0.8
quantidade = eval(input("Digite a quantidade que vai comprar: "))

if (quantidade <= 10):
    valor = preco_unitario * quantidade
elif (quantidade <= 20):
    valor = preco_unitario * quantidade * desconto10
else:
    valor = preco_unitario * quantidade * desconto20

print(f"{quantidade} item(s) comprados. O valor é de R${valor}")

# verifica os valores de uma lista, e soma somente os pares
print("\nSomar somente os pares da lista/vetor")
print("\nEstratégia 1")
lista = [10, 2, 5, 7, 6, 3]
soma = 0
for i in range(len(lista)):
    if (lista[i] % 2 == 0):
        soma += lista[i]
print(f"A soma dos elementos pares da lista é {soma}")

print("\nEstratégia 2")
lista = [10, 2, 5, 7, 6, 3]
soma = 0
for num in lista:
    if (num % 2 == 0):
        soma += num
print(f"A soma dos elementos pares da lista é {soma}")