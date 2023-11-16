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

class Humor (Animal):
    def __init__(self, raca, porte, temperamento):
        super() . __init__(raca, porte)
        self.temperamento = temperamento

    def imprimir(self):
        super() . imprimir()
        print("e tem o temperamento", self.temperamento)

animal = Humor("husky siberiano", "grande", "teimoso")
print("\n\nclasse Humor (herança da classe Animal)\n")
animal.imprimir()