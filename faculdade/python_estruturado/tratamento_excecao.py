# fazer o tratamento de exceção para verificar se a entrada é de fato um número
try:
    x = int (input("\nDigite um número: "))
except ValueError:
    print("Entre com um número válido")


# fazer o tratamento de excesão para verificar se a entrada é de fato um número, além disso, insista que o usuário digite um número válido
while True:
    try:
        x = int (input("\nDigite um número: "))
        break
    except ValueError:
        print("Entre com um número válido")


# fazer um tratamento para a exceção de divisão por zero
def dividir(x, y):
    try:
        resultado = x / y
        print(f"\nA resposta é: {resultado}")
    except ZeroDivisionError:
        print("\n\nVALOR INDETERMINADO")

dividir(3, 0)

dividir(3, 2)