# fazer uma função que encontra o menor valor de uma lista
print("\nMenor valor da lista")

def menor_valor(lista):
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    return menor

lista_teste = [2, 10, 3, 1, 4, 5]
menor = menor_valor(lista_teste)

print(f"O menor número da lista é o {menor}")

# fazer uma função que retorne a soma de todos os elementos da lista
print("\nSoma dos números pares")

def soma(lista):
    soma = 0
    for numero in lista:
        if (numero % 2 == 0):
            soma += numero
    return soma
lista_teste = [2, 10, 3, 1, 4, 5]
par = soma(lista_teste)

print(f"A soma dos números pares da lista é {par}")

# fazer uma função que retorne o fatorial de um número
print("\nFatorial de um número")
# MINHA IDEIA
# def fatorial(num):
#     if (num > 1):
#         fator = num
#         while (num > 1):
#             fator *= (num -1)
#             num -= 1
#     else:
#         fator = 1
#     return fator

# FATORIAL ITERATIVO
# def fatorial(num):
#     f = 1
#     for i in range(1, num + 1):
#         f *= i
#     return f

# FATORIAL RECURSIVO
def fatorial(num):
    if (num <= 1):
        return 1
    return num * fatorial(num - 1)

numero = 5
fatorando = fatorial(numero)

print(f"O fatorial de {numero}! é {fatorando}")

# fazer uma função que retorna se o número é primo ou não
print("\nÉ primo ou não?")

# def primo(num):
#     pri = "é primo"
#     if (num < 2):
#         pri = "não é primo"
        
#     i = num // 2
#     while (i > 1):
#         if (num % i == 0):
#             pri = "não é primo"
#         i -= 1
#     return pri

# numero = eval(input("Digite um número: "))
# resultado = primo(numero)
# print(f"O número {numero} {resultado}")


def primo(num):
    if (num < 2):
        return False
    i = num // 2
    while (i > 1):
        if (num % i == 0):
            return False
        i -= 1
    return True

def imprimir_resultado(num, resultado):
    mensagem = f"O número {num} não é primo"
    if (resultado):
        mensagem = f"O número {num} é primo"
    return mensagem

numero = eval(input("Digite um número: "))
resultado = primo(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)