# implementar uma classe que herde tudo da classe Veiculo
from ex01 import Veiculo
print("\n\n Classe Ônibus")
class Onibus(Veiculo):
    # def __init__(self, velocidade_maxima, quilometro_por_litro):
    #     super().__init__(velocidade_maxima, quilometro_por_litro)

    def tipo(self, comprimento):
        self.comprimento = comprimento
        
        if comprimento <= 14:
            return print("\nÔnibus padrão")
        elif comprimento <= 16.8:
            return print("\nÔnibus articulado")
        else:
            return print("\nÔnibus biarticulado")

onibus = Onibus(80, 300)
onibus.consumo(35)
onibus.radar(80)
onibus.tipo(17)

# print(f"\nO tipo do ônibus é: {onibus.tipo}, ")