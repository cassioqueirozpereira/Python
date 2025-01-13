numero = int(input("Faremos uma tabuada do 1 até o seu número escolhido. Digite um número: "))

def Tabuada(num):
    for i in range(num):
        for j in range(num + 1):   
            tabuada = (i+1) * (j)
            print(f"{i+1} X {j} = {tabuada}")

Tabuada(numero)