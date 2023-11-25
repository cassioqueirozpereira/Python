import threading

import time

# exemplo de função com parâmetros
def funcao2(mensagem):
    for i in range(3):
        print(i, mensagem)
        time.sleep(1)

print("Iniciando programa!")
# no target é passado a função e no args é passado o parâmetro
x = threading.Thread(target= funcao2, args= ("Executando!",))
x.start()
print("Finalizando o programa")