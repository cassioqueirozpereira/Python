num = int(input("Digite um número inteiro!: "))

def primo(num):
    aux = 0
    for i in range(num - 2):
        if ((num % (i + 2)) == 0):
            aux = 1
    if (aux == 1):
        return print(f"\nO número {num} não é primo!")
    else:
        return print(f"\nO número {num} é primo!")
        
primo(num)