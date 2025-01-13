# num = -1
# while (num < 0):
#     num = int(input("Digite um número inteiro positivo: "))

# def fatorial(num):
#     if num == 0 or  num == 1:
#         return print(f"O fatorial de {num} é 1")
#     else:
#         return num * fatorial(num - 1)
    
# resultado = fatorial(num)

# print(f"O fatorial de {num} é: {resultado}")


def fatorial(num):
    """Calcula o fatorial de um número inteiro não negativo."""
    if num < 0:
        return "Não existe fatorial de número negativo."
    elif num == 0 or num == 1:  # Caso base unificado para 0 e 1
        return 1
    else:
        return num * fatorial(num - 1)

while True:
    try:
        num = int(input("Digite um número inteiro não negativo: "))
        if num < 0:
            raise ValueError("Por favor, digite um número não negativo.")
        break # Sai do loop se a entrada for válida
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

resultado = fatorial(num)

print(f"O fatorial de {num} é: {resultado}")