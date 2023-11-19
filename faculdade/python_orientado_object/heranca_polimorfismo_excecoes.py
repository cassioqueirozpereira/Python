# herança: bastante utilizada, para reduzir a quantidade de código que se escreve

# classe herança
print("\nExemplo de Herança")
class SomaMultiplica:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        return self.a + self.b
    
    def multiplicar(self):
        return self.a * self.b

# a classe que vai dentro dos parênteses, deixa todos os seus métodos e atributos, disponíveis para a classe que está sendo criada
class Derivada(SomaMultiplica):

    def subtrair(self):
        return self.a - self.b
    
    def dividir(self):
        return self.a / self.b
    
d = Derivada(10, 20)

# perceba que a função somar não tem na classe Derivada, mas sim na classe SumaMultiplica. Mas foi possível utilizar devido a classe Derivida herdar tudo da classe SomaMultiplica
print(f"\nA soma de 10 e 20 é: {d.somar()}\n")

print(f"Booleano, vai dar verdadeiro, se a primeira classe for a que herda a segunda classe: {issubclass(Derivada, SomaMultiplica)}")


# exemplo simples de sobrecarga
print("\n\nExemplo simples de sobrecarga\n")
# já inicializando as variáveis com valores, caso coloque nenhum, somente um ou somente dois valores, ainda é possível utilizar a função. Pois, se não inicializar com valores, só será possivel ultilizar a função quando for passado os tres valores
# exemplo errado, sem inicializar com valores. Comentado, para visualizar deve, descomentar
# def soma(x, y, z):
#     return x + y + z

# print(soma(20))

# exeplo correto, inicializando os valores.
def soma(x = 0, y = 0, z = 0):
    return x + y + z

print(soma(20))


# Exemplo de polimorfismo
print("\n\nExemplo de polimorfismo")
class Argentina:
    def capital(self):
        print("\nBuenos Aires é a capital da Argentina.")

    def lingua_oficial(self):
        print("\nO espanhol é a língua oficial da Argentina.")
class Brasil:
    def capital(self):
        print("\nBrasília é a capital do Brasil.")

    def lingua_oficial(self):
        print("\nO português é a língua oficial do Brasil.")

obj_arg = Argentina()
obj_bra = Brasil()

# aqui onde o polimorfismo acontece, onde a variável país nagega sobre os dois objetos (perceba, que as nas duas classes os métodos tem que ter o mesmo nome)
for pais in (obj_arg, obj_bra):
    pais.capital()
    pais.lingua_oficial()


# outro exemplo de polimorfismo
print("\n\nOutro exemplo de polimorfismo")
class Veículo:
    
    def rodar(self):
        print("\nReduz o consumo de combustível.")

class VeículoElétrico(Veículo):

    def rodar(self):
        # super() está chamando a classe Veículo, com todos códigos dentro da função rodar
        super().rodar()
        print("\nEsse veículo utiliza eletricidade\n")

veiculo_eletrico = VeículoElétrico()
veiculo_eletrico.rodar()


# Exemplo de Exceção
print("\nExemplo de exceção\n")

x = 10

if x > 5:
    raise Exception(f"x não pode ser teste maior que 5. O valor de x foi de: {x}")
else:
    print(f"Tudo certo")