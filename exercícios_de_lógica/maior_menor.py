array = [3, 7, 2, 8, 1, 9, 4, 6, 5, 10]

for i in range((len(array)) - 1):
    if array[i] > array[i+1]:
        aux = array[i]
        array[i] = array[i+1]
        array[i+1] = aux
    else:
        continue

maior = array[(len(array)) - 1]

print(f"O maior número da lista {array} é o número: {maior}\n")


for i in range((len(array)) - 1):
    if array[i] < array[i+1]:
        aux = array[i]
        array[i] = array[i+1]
        array[i+1] = aux
    else:
        continue

menor = array[(len(array)) - 1]

print(f"O menor número da lista {array} é o número: {menor}")