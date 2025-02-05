num = int(input("Digite quantos números terá o vetor: "))

vetor = []

for i in range(num):
    n = float(input(f"Digite o {i + 1}º número: "))
    vetor.append(n)

print(f"Os números que vc digitou são: {vetor}")

for i in range(num - 1):
    for i in range(num - 1):
        if (vetor[i] > vetor[i + 1]):
            aux = vetor[i]
            vetor[i] = vetor[i + 1]
            vetor[i + 1] = aux
    
print(f"\nOs números em ordem crescente ficam: {vetor}")