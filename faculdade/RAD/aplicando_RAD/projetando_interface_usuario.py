import tkinter as tk
from tkinter import ttk
import pandas as pd

class principal_rad:
    def __init__(self, win):
        #componentes
        self.lb_nome = tk.Label(win, text= "Nome do aluno:")
        self.lb_nota1 = tk.Label(win, text= "Nota 1")
        self.lb_nota2 = tk.Label(win, text= "Nota 2")
        self.lb_media = tk.Label(win, text= "Média")
        self.text_nome = tk.Entry(bd= 3)
        self.text_nota1 = tk.Entry()
        self.text_nota2 = tk.Entry()
        self.btn_calcular = tk.Button(win, text= "Calcular Média", command= self.calcular_media())
        self.btn_salvar = tk.Button(win, text= "Salvar Dados", command= self.salvar_dados())

        # componente treeview
        self.dados_colunas = ("Aluno", "Nota1", "Nota2", "Média", "Situação")

        self.tree_medias = ttk.Treeview(win, columns= self.dados_colunas, selectmode= "browse")

        self.verscrlbar = ttk.Scrollbar(win, orient= "vertical", command= self.tree_medias.yview)

        self.verscrlbar.pack(side= "right", fill= "x")

        self.tree_medias.configure(yscrollcommand= self.verscrlbar.set)

        self.tree_medias.heading("Aluno", text= "Aluno")
        self.tree_medias.heading("Nota1", text= "Nota 1")
        self.tree_medias.heading("Nota2", text= "Nota 2")
        self.tree_medias.heading("Média", text= "Média")
        self.tree_medias.heading("Situação", text= "Situação")

        self.tree_medias.column("Aluno", minwidth=0, width=100)
        self.tree_medias.column("Nota1", minwidth=0, width=100)
        self.tree_medias.column("Nota2", minwidth=0, width=100)
        self.tree_medias.column("Média", minwidth=0, width=100)
        self.tree_medias.column("Situação", minwidth=0, width=100)

        self.tree_medias.pack(padx=10, pady=10)

        # posicionamento dos componentes na janela
        self.lb_nome.place(x=100, y=50)
        self.text_nome.place(x=200, y=50)

        self.lb_nota1.place(x=100, y=100)
        self.text_nota1.place(x=200, y=100)

        self.lb_nota2.place(x=100, y=150)
        self.text_nota2.place(x=200, y=150)

        self.btn_calcular.place(x=100, y=200)
        self.btn_salvar.place(x=220, y=200)

        self.tree_medias.place(x=100, y=300)
        self.verscrlbar.place(x=805, y=300, height=225)

        self.id = 0
        self.iid = 0

        self.carregar_dados_iniciais()
    
    def carregar_dados_iniciais(self):
        try:
            fsave = "faculdade/RAD/aplicando_RAD/planilha_alunos.html"
            dados = pd.read_excel(fsave)
            print("*********************dados disponíveis*********************")
            print(dados)
            
            u = dados.count()
            print("u:" + str(u))
            nn = len(dados["Aluno"])
            for i in range(nn):
                nome = dados["Aluno"][i]
                nota1 = str(dados["Nota1"][i])
                nota2 = str(dados["Nota2"][i])
                media = str(dados["Média"][i])
                situacao = dados["Situação"][i]

                self.tree_medias.insert("", "end",
                                        iid=self.iid,
                                        values=(nome,
                                                nota1,
                                                nota2,
                                                media, situacao))
                
                self.id = self.id + 1
                self.iid = self.iid + 1
        except:
            print("Ainda não existem dados para carregar!")
    
    # salvar dados para uma planilha excel
    def salvar_dados(self):
        try:
            fsave = "planilha_alunos.xlsx"
            dados = []
        
            for line in self.tree_medias.get_children():
                lista_dados = []
                for value in self.tree_medias.item(line)["values"]:
                    lista_dados.append(value)
                dados.append(lista_dados)
            
            df = pd.DataFrame(data = dados, columns = self.dados_colunas)

            planilha = pd.ExcelWriter(fsave)
            df.to_excel(planilha, "dados", index = False)

            print("Dados salvos")
        except:
            print("Não foi possível salvar os dados")
    
    # calcula a média e verifica qual é a situação do aluno
    def verificar_situacao(self, nota1, nota2):
        media = (nota1 + nota2) / 2
        if (media >= 7):
            situacao = "Aprovado"
        elif (media >= 5):
            situacao = "Em Recuperação"
        else:
            situacao = "Reprovado"
        
        return media, situacao
    
    # imprime os dados do aluno
    def calcular_media(self):
        try:
            nome = self.text_nome.get()
            
            # verifica se as notas são numéricas
            nota1_str = self.text_nota1.get()
            nota2_str = self.text_nota2.get()

            if nota1_str == "" or nota2_str == "":
                print("As notas não podem estar vazias")

            nota1 = float(nota1_str)
            nota2 = float(nota2_str)

            media, situacao = self.verificar_situacao(nota1, nota2)

            self.tree_medias.insert("", "end",
                                    iid = self.iid,
                                    values = (nome,
                                              str(nota1),
                                              str(nota2),
                                              str(media),
                                              situacao))
            
            self.id = self.id + 1
            self.iid = self.iid + 1

            self.salvar_dados()

        except ValueError:
            print("Entre com valores válidos")
        
        finally:
            self.limpar_campos()
    
    def limpar_campos(self):
        self.text_nome.delete(0, "end")
        self.text_nota1.delete(0, "end")
        self.text_nota2.delete(0, "end")
        

# programa principal
janela = tk.Tk()
principal = principal_rad(janela)
janela.title("Bem Vindo ao RAD")
janela.geometry("820x600+10+10")
janela.mainloop()