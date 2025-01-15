num = -1
while (num < 0):
    num = int(input("Digite um número inteiro positivo: "))

def fatorial(num):
    if num == 0 or  num == 1:
        return 1
    else:
        return num * fatorial(num - 1)

    
resultado = fatorial(num)

print(f"O fatorial de {num} é: {resultado}")