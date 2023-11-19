faturamento = 1500

custo = 500

lucro = faturamento - custo

# "_" significa que vai separar as unidades de milhar por underline.
# ".2f" significa que irá separar as casas decimais por "ponto" e mostrará duas casas
texto_lucro = (f"R${lucro:_.2f}").replace(".", ",").replace("_", ".")

print(f"\nO lucro foi de R${texto_lucro}")

margem_lucro = lucro / faturamento

# .2% diz que vai ter duas casas decimais e vai ser mostrado no padrão porcentagem
print(f"\nA margem foi de {margem_lucro:.2%}\n")