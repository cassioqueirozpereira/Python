num = -1

while (num < 0):
    num = int(input("\nDigite um número inteiro positivo: "))
    if (num < 0):
        print("Você digitou um número negativo!")

def f_fibonacci(num):
    fibonacci = [1, 1]
    print(fibonacci, num)
    for i in range(num):
        fibonacci.append(1)
    return print(fibonacci)

f_fibonacci(num)

