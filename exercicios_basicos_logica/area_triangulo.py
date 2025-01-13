base = float(input("Digite o valor da base do triângulo: "))

altura = float(input("Digite o valor da altura do triângulo: "))

def area(num1, num2):
    return (base * altura) / 2

resultado = area(base, altura)

print(f"A área do triângulo é: {resultado}")