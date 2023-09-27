import pyautogui # executar as tarefas
import time # controlar o tempo entre as tarefas

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas)
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
pyautogui.click(x=722, y=449) 
# clicks=3 -> ele vai dar tres cliques
# button="right" -> ele vai clicar com o botão direito
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha aqui")
pyautogui.press("tab")
pyautogui.press("enter")

#pythonimpressionador@gmail.com sua senha aqui 
import pandas # importar a base de dados
 
tabela = pandas.read_csv("produtos.csv")
print(tabela)