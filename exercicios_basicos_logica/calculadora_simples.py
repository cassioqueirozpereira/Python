num1 = float(input("Digite o primeiro número: "))

calculo = input("\nDigite + para soma(+).\nDigite X para multiplicação(X).\nDigite - para subtração(-).\nDigite / para divisão(/): ")

operacao = calculo.upper()

num2 = float(input("\nDigite o segundo número: "))

def soma(num1, num2):
    return num1 + num2

def multiplica(num1, num2):
    return num1 * num2

def subtrai(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

if (operacao == '+'):
    resultado = soma(num1, num2)
    print(f"\nO resultado é {resultado}")

if (operacao == 'X'):
    resultado = multiplica(num1, num2)
    print(f"\nO resultado é {resultado}")

if (operacao == '-'):
    resultado = subtrai(num1, num2)
    print(f"\nO resultado é {resultado}")

if (operacao == '/'):
    resultado = divide(num1, num2)
    print(f"\nO resultado é {resultado}")