import threading

import time

# # exemplo de função sem parâmetros
def funcao():
    for i in range(3):
        print(i, "Executando a thread!")
        time.sleep(1)

print("Iniciando o programa!")
# no target é passado a função
threading.Thread(target= funcao).start()
print("Finalizando o programa!")