# Implementar uma classe Veículo com atributos de instância "velocidade máxima" e "quilômetros percorridos por litro"
print("\n\n Classe Veículo")
class Veiculo:

    def __init__(self, velocidade_maxima, quilometro_por_litro):
        self.velocidade_maxima = velocidade_maxima
        self.quilometro_por_litro = quilometro_por_litro
    
    def radar(self, velocidade):
        self.velocidade = velocidade
        if velocidade <= self.velocidade_maxima:
            print(f"\nSua velocidade foi de: {velocidade}Km/h. Use cinto de segurança.")
        else:
            print(f"\nSua velocidade foi de: {velocidade}Km/h. Acima do limite de velocidade: {self.velocidade_maxima}Km/h. Multado!")

    def consumo(self, combustivel):
        self.combustivel = combustivel
        consumo = self.quilometro_por_litro / combustivel
        return print(f"\nO consumo é {consumo:.0f}km/l")
    
transporte = Veiculo(110, 300)

transporte.radar(111)

transporte.consumo(20)