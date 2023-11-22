class End_simples(object):
    def __init__(self, rua, num, bairro):
        self.rua = rua
        self.num = num
        self.bairro = bairro

    def endereco(self):

        return self.rua + "," + self.num + self.bairro
    
class End_com(End_simples):
    def __init__(self, rua, num, bairro, com):
        End_simples.__init__(self, rua, num, bairro)
        self.com = com

    def endereco(self):
        return super(End_com, self).endereco() + "," + self.com
    
a = End_simples("\nAv Brasil", " 243", " Floresta")

b = End_com("\nAv Miracema", " 12", " Centro", " apto 3")

print(a.endereco())

print(b.endereco())