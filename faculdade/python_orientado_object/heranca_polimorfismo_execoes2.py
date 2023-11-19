from agregacao_classes_estatico2 import Cont
from agregacao_classes_estatico2 import c2
from agregacao_classes_estatico2 import c1
import datetime


# herança
print("\nHerança")
class ContaEspecial(Cont):
    def __init__(self, clientes, numero, saldo, limite):
        Cont.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor])
            return True

fatura = ContaEspecial([c1, c2], 33333333, 4000, 1000)
fatura.sacar(4500)
print("\nAs transações foram\n")
fatura.extrato.imprimir()
print(f"\nO saldo final é: {fatura.saldo}")

# herança multipla
print("\n\nHerança multipla\n")

# Classe que será herdada
class Poupanca:
    
    def __init__(self, taxaremuneracao):
        self.taxaremuneracao = taxaremuneracao
        self.data_abertura = datetime.datetime.today()
    
    def remuneraConta(self, saldo):
        self.saldo += saldo * self.taxaremuneracao

# aqui a classe ContaRemuneradaPoupanca está recebendo a herança multipla
class ContaRemuneradaPoupanca(Cont, Poupanca):
    
    def __init__(self, clientes, numero, saldo, taxa_remuneracao):
        Cont.__init__(self, clientes, numero, saldo)
        Poupanca.__init__(self, taxa_remuneracao)
        self.taxa_remuneracao = taxa_remuneracao

    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxa_remuneracao / 30)

cx = ContaRemuneradaPoupanca([c1, c2], 98939123, 1500.00, 0.03)
print(f"\nO número da conta é: {cx.taxa_remuneracao}, o saldo é de: {cx.saldo}, a taxa de remuneração é: {cx.taxa_remuneracao}")
cx.sacar(500)
cx.remuneraConta()
print(f"\nO saldo final é de: {cx.saldo}")


# polimorfismo
print("\n\nPolimorfismo")
class ContaCliente:

    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valor_investido = valor_investido
        self.taxa_rendimento = taxa_rendimento
    
    def calculoRendimento(self):
        pass

class ContaComum(ContaCliente):

    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendimento)
    
    def calculoRendimento(self):
        self.valor_investido += (self.valor_investido * self.taxa_rendimento)

class ContaRemunerada(ContaCliente):

    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendimento)

    def calculoRendimento(self):
        self.valor_investido += (self.valor_investido * self.taxa_rendimento)
        self.valor_investido -= self.valor_investido * self.IOF

try:
    print(x)
except:
    print("Variável indefinida")

class ExcecaoCustomizada(Exception):
    pass


# y = "hello"

# if not type(y) is int:
#     raise TypeError("Use apenas inteiros")


x = -1
if x < 0:
    raise Exception("Valor negativo!!!")
print("Cássio")