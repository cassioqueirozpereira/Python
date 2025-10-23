print("\n---------------------Variable and your types---------------------------\n")

example_string = "Cássio"
example_list = ["Cássio", "Dilnara", "Lanna", "Victor"]
example_tuple = ("Cássio", "Dilnara", "Lanna", "Victor")
example_conjunct = set(example_list)
example_int = 1
example_rational = 3.3
example_complexy = 1e10
example_bool = True

example_dictionary = {
    "string": example_string,
    "list": example_list,
    "tuple": example_tuple,
    "conjunct": example_conjunct,
    "int": example_int,
    "rational": example_rational,
    "complexy": example_complexy,
    "bool": example_bool
}

for k, v in example_dictionary.items():
    print(k,":", v, "-Type->", type(example_dictionary[k]))

print("Dictionary from type: ", type(example_dictionary))

print("\n---------------------------------Operators--------------------------------------\n")

print("Aritméticos: +, -, *, /, // (divisão inteira), % (módulo), ** (exponenciação).")
print("Relacionais: ==, !=, >, <, >=, <=.")
print("Lógicos: and, or, not.")
print("Membro: in, not in.")
print("Identidade: is, is not.")
print("Atribuição: =, +=, -=, *= etc.")

print("\nFOR\n")

for i in range(0, 5):
    print(i)

print("\nWHILE\n")

i = 0
while i < 5:
    print(i)
    i += 1

print("\n---------------------------------Functions--------------------------------------\n")

def soma(a, b):
    return a + b

print(soma(1, 2))

print("\n---------------------------------Class--------------------------------------\n")

class cachorro:
    def __init__(self, nome, raca, tutor):
        self.nome = nome
        self.raca = raca
        self.tutor = tutor

    def latir(self):
        print("Au Au Au !")

terry = cachorro("Terry", "Pastor Alemão", "Cássio")
print("Dados do cachorro:")
print("Nome:", terry.nome)
print("Raça:", terry.raca)
print("Tutor:", terry.tutor)
terry.latir()

print("\n---------------------------------Scope--------------------------------------\n")

with open("./query.sql") as file:
    sql_query = file.read()

print(sql_query)

print("\n---------------------------------Importing Modules--------------------------------------\n")

from datetime import date
import os
from pandas import *
import pandas as pd

print("\n---------------------------------Data Assets--------------------------------------\n")

dataset = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
columns = ["a", "b", "a or b"]
ordf = pd.DataFrame(dataset, columns = columns)

print(ordf)

ordf.to_csv("./ordf.csv")

read_the_Data_Assets = pd.read_csv("./ordf.csv")

print("\nRead the datas\n\n", read_the_Data_Assets)

print("\nRead the values\n\n", read_the_Data_Assets.values)

print("\nRead the collumns\n\n", read_the_Data_Assets.columns)