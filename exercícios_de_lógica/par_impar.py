num = int(input("Digite um número: "))

def par_ou_impar(num):
    if (num % 2) == 0:
        return print(f"O número {num} é par")
    else:
        return print(f"O número {num} é ímpar")
    
par_ou_impar(num)