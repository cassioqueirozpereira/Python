# atribuição multipla

a, b = 1, 2
print(f"Antes da troca\nO valor das variáveis: a = {a}, b = {b}");

# primeira troca
auxiliar = a;
a = b;
b = auxiliar;
print(f"Primeira troca\nO valor das variáveis: a = {a}, b = {b}");

# segunda troca
a, b = b, a;
print(f"Segunda troca\nO valor das variáveis: a = {a}, b = {b}");