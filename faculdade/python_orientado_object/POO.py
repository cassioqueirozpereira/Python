# programação orientada a objeto
# as classes vao ter atributos e métodos, atributos são caracteristicas da classe e métodos são as ações da classe

# Propriedades da PPO
# 1º Abstração: Modelo reduzido, ou modelo simplificado;
# 2ª Encapsulamento: Restringe o acesso a métodos e atribustos em uma classe. Em python, isso é obtido com métodos ou atribustos privados usando sublinhado como prefixo, ou seja, "_" simples ou "__" duplo;
# 3ª Herança: Permite definir uma classe que herda todos os métodos e atributos de outra classe;
# 4ª Polimorfismo: Permite usar uma única interface com diferentes formas;

# PPO no python

# classe pessoa
class Pessoa:
    # "__init__" é o contrutor. É a maneira de inicializar o objeto
    # "self" é a referencia para acessar os atributos e os métodos da classe, ou seja, "self" é o ponteiro para o próprio objeto do python, outras linguagens utilizam o "this", ou o "me". No caso do python ele é essencial para definir atributos e métodos
    # "nome" é um parâmetro passado ao construtor
    # "ender" é outro parâmetro passado ao construtor
    def __init__(self, nome, ender):
        # criando uma função para o parâmetro nome
        self.set_nome(nome)
        # criando uma função para o parâmetro ender
        self.set_ender(ender)

    # acessando o parâmetro nome
    def set_nome(self, nome):
        # transformando o parâmetro nome em um atributo
        self.nome = nome

    # acessando o parâmetro ender
    def set_ender(self, ender):
        # transformando o parâmetro ender em um atributo
        self.ender = ender

    # função que retorna o atributo nome
    def get_nome(self):
        return self.nome
    
    # função que retorna o atributo ender
    def get_ender(self):
        return self.ender
    
# objeto pessoa
# pessoa1 é um objeto
# pessoa2 é outro objeto
# Pessoa é a classe
# maria é o parâmetro passado para o nome
# rua 01234 é o parâmetro passado para o ender
nome1 = "maria"
nome2 = input("\nDigite o seu nome: ")
endereco1 = "rua 01234"
endereco2 = input("\nDigite o seu endereço: ")

pessoa1 = Pessoa(nome1, endereco1)
pessoa2 = Pessoa(nome2, endereco2)

#imprimir cada um dos objetos
print("\nclasse Pessoa")
print(f"\nNome: {pessoa1.get_nome()}, Endereço: {pessoa1.get_ender()}")
print(f"\nNome: {pessoa2.get_nome()}, Endereço: {pessoa2.get_ender()}")

# outro exemplo de classe
# classe Animal

class Animal:
    def __init__(self, raca, porte):
        self.raca = raca
        self.porte = porte

    def imprimir(self):
        print(self.raca, "é do porte", self.porte)

    def getPorte(self):
        return self.porte
    
    def setPorte(self, porte):
        self.porte = porte

animal = Animal("husky siberiano", "grande")
print("\n\nclasse Animal\n")
animal.imprimir()

# exemplo de herança

class Humor:
    def __init__(self, raca, porte, temperamento):
        super().__init__(raca, porte)
        self.temperamento = temperamento

    def imprimir(self):
        animal.imprimir()
        print("\t e tem o temperamento", self.temperamento)

animal = Humor("husky siberiano", "grande", "teimoso")
animal.imprimir()