num1 = 2
num2 = 2
while (num1 == num2):
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    if (num1 == num2):
        print("Você digitou dois números iguais. Digite dois números diferentes!")

if (num1 > num2):
    print(f"O número {num1} é maior que o {num2}")
else:
    print(f"O número {num2} é maior que o {num1}")