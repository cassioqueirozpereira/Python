# executar as tarefas
import pyautogui
# controlar o tempo entre as tarefas
import time
# importar a base de dados
import pandas

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas)

pyautogui.PAUSE = 0.1
pyautogui.press("win")
# aguarda 0.6 seconds antes da próxima tarefa
time.sleep(.8)
pyautogui.write("chrome")
time.sleep(.8)
pyautogui.press("enter")
time.sleep(.8)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
# selecionando o ponto da tela onde vai ser clicado
# pyautogui.click(x=722, y=449) #tirei pois conforme o tamanho da tela não clica no lugar certo

# clicks=3 -> ele vai dar tres cliques
# button="right" -> ele vai clicar com o botão direito

# pythonimpressionador@gmail.com sua senha aqui
pyautogui.press("tab")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha aqui")
pyautogui.press("tab")
pyautogui.press("enter") 

# tabela recebe pandas que lê o arquivo tipo csv, com seu respectivo diretório
tabela = pandas.read_csv("atividades_internet/primeira-automacao/produtos.csv")
# mostra a tabela, somente para conferir se carregou o arquivo corretamente. Como já foi verificado, vou comentar
# print(tabela)

time.sleep(1)
# para cada linha da tabela
for linha in tabela.index:

    # click na posição escolhida através do auxiliar.py
    pyautogui.press("tab")
    # pyautogui.click(x=785, y=310)

    # codigo recebe tabela na localização da linha "nome da coluna" (banco de dados). Obs: O comando write só escreve no formato string, se estiver em outro formato, é necessário converte-lo
    codigo = tabela.loc[linha, "codigo"]
    
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # como é número, foi necessário converter para str (string)
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # como é número, foi necessário converter para str (string)
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # como é número, foi necessário converter para str (string)
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    # se negação do banco de dados está vazio no campo "obs", ou seja, só escreva o campo "obs", se este estiver com dados preenchidos
    if not pandas.isna(obs):
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("tab", presses=8, interval=0.01)

    # rola a barra de rolagem para cima se o número for positivo e para baixo se for negativo, quanto maior o número mais irá rolar
    # pyautogui.scroll(10000)