from datetime import datetime

frutas = ["Jabuticaba", "Laranja", "Uva", "Banana"]

# for para percorrer cada argumento da lista
for fruta in frutas:
    # depois de {fruta:} o que é colocado depois dos : é a quantidade de espaço que será reservado, caso a palavra seja maior que o espaço, será escrito tudo, caso a palavra seja menor, será acrescentado com espaço vazio até preencher todos os espaços reservados.
    minha_fruta = f"Nome: {fruta:10} - Número de letras: {len(fruta): 3}"
    print(minha_fruta)

    print()

pi = 3.1415
meu_numero = f"O número PI é: {pi:.1f}"
# o 6.1f, significa que será dado 6 casas de espaço para então aprensentar o número e o .1 é quantas casas depois da virgula ou ponto serão acrescentadas, nesse caso 1
meu_numero_deslocado = f"O número PI deslocado é: {pi:6.1f}"
# nesse caso .4, será acrescentado 4 casas depois da virgula
meu_numero_preciso = f"O número PI mais preciso é: {pi:.4f}"
print(meu_numero)
print(meu_numero_deslocado)
print(meu_numero_preciso)

print()

data = datetime.now()
# nesse caso aparece a data no padão inglês
minha_data = f"A data de hoje é {data}"
# aqui com a formatação %d/%m%Y, obrigamos a aparecer primeiro o dia, depois o mês e por fim o ano.
minha_data_formatada = f"A data de hoje formatada é {data:%d/%m/%Y}"
print(minha_data)
print(minha_data_formatada)