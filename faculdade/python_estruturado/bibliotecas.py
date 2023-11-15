# fazer uma solução para a equação do segundo grau
print("\nEquação do segundo grau")

def dados():
    coeficiente = eval(input("Digite o valor do coeficiente: "))
    return coeficiente

def calc_delta(a, b, c):
    delta = b * b - 4 * a * c
    return delta

import numpy as np

def raizes(a, b, delta):
    if (delta < 0):
        resultado = "A equação não possui raízes nos números reais"
    elif (delta == 0):
        x = -b / 2 * a
        resultado = f"A equação possui apenas a raíz: {x}"
    else:
        x1 = (-b + np.sqrt(delta)) / (2 * a)
        x2 = (-b - np.sqrt(delta)) / (2 * a)
        resultado = f"A equação possui as raízes: {x1} e {x2}"
    return resultado

a = dados()
b = dados()
c = dados()

delta = calc_delta(a, b, c)

resultado = raizes(a, b, delta)

print(resultado)

# implementar uma solução em python para visualizar dados de vendas de um produto em gráfico de barras
import matplotlib.pyplot as plt

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)
plt.show()

# gerar 1000 pontos seguindo a atribuição Normal com média 20 e desvio-padrão 2. Exibir os dados em um histograma
import matplotlib.pyplot as plt

np.random.seed(1)
data = np.random.normal(loc = 20, scale = 2, size = 1000)
plt.hist(data, color = "black", ec = "green")
plt.show()