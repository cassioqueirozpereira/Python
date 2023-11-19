# Implementar uma classe Veículo com atributos de instância "velocidade máxima" e "quilômetros percorridos por litro"

class Veiculo:

    def __init__(self, velocidade_maxima, quilometro_por_litro):
        self.velocidade_maxima = velocidade_maxima
        self.quilometro_por_litro = quilometro_por_litro
    
    def radar(self, velocidade):
        self.velocidade = velocidade
        if velocidade <= self.velocidade_maxima:
            print("Use cinto de segurança")
        else:
            print("Acima do limite de velocidade. Multado!")

    def consumo(self, combustivel):
        self.combustivel = combustivel
        return print("\nO consumo é {}km/l" . format(self.quilometro_por_litro / combustivel))
    
transporte = Veiculo(100, 300)

transporte.radar(101)

transporte.consumo(20)