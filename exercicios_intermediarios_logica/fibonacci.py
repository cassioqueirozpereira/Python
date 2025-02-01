num = -1

while (num <= 0):
    num = int(input("\nDigite a quantidade de números da sequência de fibonacci deseja ver: "))
    if (num <= 0):
        print("\nVocê digitou um número menor que 1.\nPor favor digite um número maior que zero!")

def f_fibonacci(num):
    fibonacci = [0, 1]
    if (num == 1):
        return print(fibonacci[0])
    elif (num > 1):
        for i in range(num - 2):
            fibonacci.append(fibonacci[i] + fibonacci[i + 1])
        return print(fibonacci)

f_fibonacci(num)

