# atributos estáticos
print("\nAtributo estático\n")

class Pessoa:
    # atributo estático, pois todas as pessoas da classe Pessoa, vão compartilhar o mesmo contador
    _contador = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa._contador +=1

    def imprimir(self):
        print(self.nome, " tem ", self.idade, " ano(s)")

    # propriedade
    @property

    # definindo um método do objeto
    def contador(self):
        # type(self) é mesma coisa que escrever Pessoa, pois refere-se a própria classe
        return type(self)._contador
    
p1 = Pessoa("Carlos", 18)
p1.imprimir()
print(f"\nMostrando o contador através da propriedade: {p1.contador}")
print(f"\nMostrando o contador direto pela classe: {Pessoa._contador}")


# método da classe
print("\n\nMétodo da classe")
class NomeCompleto:
    
    # self, é para chamar a própria classe (NomeCompleto), para o objeto
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    # método da classe
    @classmethod

    # cls, é para chamar a própria classe (NomeCompleto), para o classe. STANDARD FACTORY (padão fábrica)
    def fromString(cls, texto):
        # nome vai receber tudo antes do espaço e sobrenome tudo depois do espaço
        nome, sobrenome = map(str, texto.split(" "))
        objeto = cls(nome, sobrenome)
        return objeto

registro1 = NomeCompleto.fromString("Luiz Braga")
print(f"\nMostrando o valor antes do espaço: {registro1.nome}")
print(f"\nMostrando o valor depois do espaço: {registro1.sobrenome}")


# método estático
print("\n\nMétodo estático")
class Nome:
    
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    @classmethod

    def fromString(cls, texto):
        nome, sobrenome = map(str, texto.split(" "))
        objeto = cls(nome, sobrenome)
        return objeto
    
    @staticmethod

    def isValid(texto):
        nomes = texto.split(" ")
        return len(nomes) > 1
    
registro2 = Nome.isValid("Dilnara de Almeida")
registro3 = Nome.fromString("Cássio Queiroz")
print(f"\nVerifica se o nome tem 1 ou mais espaços e retorna um booleano True se sim e False se não: {registro2}")
print(f"\nMostrando o valor antes do espaço: {registro3.nome}")
print(f"\nMostrando o valor depois do espaço: {registro3.sobrenome}")


# agregação independente/assossiativa, ou seja, uma classe não depende da outra, se excluir uma a outra ainda continua funcionando
print("\n\nAgregação independente/assossiativa")
class Conta:

    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
        
class Cliente:
    
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

cliente1 = Cliente("123456789-10", "Ana", "Rua dos bobos")

cliente2 = Cliente("987654321-10", "Carlos", "Rua zero")

conta = Conta([cliente1, cliente2], 12000000, 2500.00)

conta.depositar(1000)

conta.sacar(500)

print(f"\nO primeiro cliente se chama: {cliente1.nome} e tem o endereço: {cliente1.endereco}")
print(f"\nO segundo cliente se chama: {cliente2.nome} e tem o endereço: {cliente2.endereco}")
print(f"\nO número da conta é: {conta.numero} e o saldo é:{conta.saldo}")


# composição dependente/estruturada, ou seja, uma classe depende da outra, se excluir uma, a outra para de funcionar
print("\n\nAgregação dependente/estruturada")
class Extrato:

    def __init__(self):
        self.transacoes = []

    def imprimir(self):
        for p in self.transacoes:
            print(p[0], p[1])

class Cont:

    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor])
            return True
        
c1 = Cliente("111111111-11", "Dilnara", "Rua Centro")

c2 = Cliente("222222222-22", "VictorLanna", "Rua Centro")

conta = Cont([c1, c2], 12345678, 3000.00)

conta.depositar(1000)

conta.sacar(500)

print("\nAs transações e seus respectivos valores:\n")
conta.extrato.imprimir()

print(f"\nO número da conta dos clientes é: {conta.numero} e o saldo final: {conta.saldo}")