import pyautogui
import time

time.sleep(5)
print(pyautogui.position()) # irá mostrar a posição do mouse

pyautogui.scroll(10000) # irá rolar a barra para cima conforme o valor positivo. Para baixo se negativo.