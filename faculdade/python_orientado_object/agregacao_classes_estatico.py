# Agregação

# classe Salário
class Salario:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def salario_anual(self):
        return (self.base * 12) + self.bonus
    
#classe Empregado
class Empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        # agregação
        self.salario_agregado = salario

    def salario_total(self):
        return self.salario_agregado.salario_anual()
    
salario = Salario(10000, 700)
emp = Empregado("musashi", 46, salario)
print(emp.nome, emp.idade, emp.salario_total())


# Método de Classes e Método Estático
from datetime import date

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # um método de classe para criar um objeto Pessoa através do ano de nascimento
    @classmethod
    def apartirAnoNascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)
    
    # Método Estático: Verificar se é maior de idade
    @staticmethod
    def maiorIdade(idade):
        return idade >= 18