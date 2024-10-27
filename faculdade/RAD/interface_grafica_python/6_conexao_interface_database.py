import tkinter as tk
from tkinter import ttk
import class_database as crud

class principal_BD:
    def __init__(self, win):
        self.objBD = crud.AppBD()
        #componentes
        self.lb_codigo = tk.Label(win, text = "Código do Produto:")
        self.lb_nome = tk.Label(win, text = "Nome do Produto:")
        self.lb_preco = tk.Label(win, text = "Preço:")

        self.txt_codigo = tk.Entry(bd = 3)
        self.txt_nome = tk.Entry()
        self.txt_preco = tk.Entry()
        self.btn_cadastrar = tk.Button(win, text = "CADASTRAR", command = self.f_cadastrar_produto)
        self.btn_atualizar = tk.Button(win, text = "ATUALIZAR", command = self.f_atualizar_produto)
        self.btn_excluir = tk.Button(win, text = "EXCLUIR", command = self.f_excluir_produto)
        self.btn_limpar = tk.Button(win, text = "LIMPAR", command = self.f_limpar_tela)
        
        # componente Tree View
        self.dados_colunas = ("CÓDIGO", "NOME", "PREÇO")

        self.tree_produtos = ttk.Treeview(win, columns = self.dados_colunas, selectmode = "browse")

        self.verscrlbar = ttk.Scrollbar(win, orient="vertical", command=self.tree_produtos.yview)

        self.verscrlbar.pack(side="right", fill="x")

        self.tree_produtos.configure(yscrollcommand=self.verscrlbar.set)

        self.tree_produtos.heading("CÓDIGO", text = "CÓDIGO")
        self.tree_produtos.heading("NOME", text = "NOME")
        self.tree_produtos.heading("PREÇO", text = "PREÇO")

        self.tree_produtos.column("CÓDIGO", minwidth=0, width=100)
        self.tree_produtos.column("NOME", minwidth=0, width=100)
        self.tree_produtos.column("PREÇO", minwidth=0, width=100)

        self.tree_produtos.pack(padx=10, pady=10)

        self.tree_produtos.bind("<<TreeviewSelect>>", self.apresentar_registros_selecionados)

        # posicionamento dos componentes na janela
        self.lb_codigo.place(x=100, y=50)
        self.txt_codigo.place(x=250, y=50)

        self.txt_nome.place(x=100, y=100)
        self.txt_nome.place(x=250, y=100)

        self.txt_preco.place(x=100, y=150)
        self.txt_preco.place(x=250, y=150)

        self.btn_cadastrar.place(x=100, y=200)
        self.btn_atualizar.place(x=200, y=200)
        self.btn_excluir.place(x=300, y=200)
        self.btn_limpar.place(x=400, y=200)

        self.tree_produtos.place(x=100, y=300)
        self.verscrlbar.place(x=605, y=300, height=225)
        self.carregar_dados_iniciais()
    
    def apresentar_registros_selecionados(self, event):
        self.f_limpartela()

        for selection in self.tree_produtos.selection():
            item = self.tree_produtos.item(selection)
            codigo, nome, preco = item["values"][0:3]
            self.txt_codigo.insert(0, codigo)
            self.txt_nome.insert(0, nome)
            self.txt_preco.insert(0, preco)
    
    def carregar_dados_iniciais(self):
        try:
            self.id = 0
            self.iid = 0
            registros = self.objBD.selecionar_dados()
            print("**************dados disponíveis no BD**************")
            for item in registros:
                codigo = item[0]
                nome = item[1]
                preco = item[2]
                print("CÓDIGO = ", codigo)
                print("NOME = ", nome)
                print("PREÇO = ", preco, "\n")

                self.tree_produtos.insert("", "end", iid=self.iid, values=(codigo, nome, preco))

                self.iid = self.iid + 1
                self.id = self.id + 1
            
            print("Dados da Base")
        
        except:
            print("Ainda não existem dados para carregar")

    
    def f_ler_campos(self):
        try:
            print("**************dados disponíveis**************")
            codigo = int(self.txt_codigo.get())
            print("CÓDIGO", codigo)
            nome = self.txt_nome.get()
            print("NOME", nome)
            preco = float(self.txt_preco.get())
            print("PREÇO", preco)
            print("Leitura dos dados com sucesso!")
        
        except:
            print("Não foi possível ler os dados.")
        
        return codigo, nome, preco
    
    # cadastrar produto
    def f_cadastrar_produto(self):
        try:
            print("**************dados disponíveis**************")
            codigo, nome, preco = self.f_ler_campos()
            self.objBD.inserir_dados(codigo, nome, preco)
            self.tree_produtos.insert('', 'end', iid=self.iid, values=(codigo, nome, preco))
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.f_limpar_tela()
            print("Produto cadastrado com sucesso!")
        except:
            print("Não foi possível fazer o cadastro.")

    
    def f_atualizar_produto(self):
        try:
            print("**************dados disponíveis**************")
            codigo, nome, preco = self.f_ler_campos()
            # recarregar dados na tela
            self.tree_produtos.delete(*self.tree_produtos.get_children())
            self.carregar_dados_iniciais()
            self.f_limpar_tela()
            print("Produto atualizado com sucesso!")
        except:
            print("Nâo foi possível fazer a atualização.")
    
    # excluir produto
    def f_excluir_produto(self):
        try:
            print("**************dados disponíveis**************")
            codigo, nome, preco = self.f_ler_campos()
            self.objBD.excluir_dados(codigo)
            # recarregar dados na tela
            self.tree_produtos.delete(*self.tree_produtos.get_children())
            self.carregar_dados_iniciais()
            self.f_limpar_tela()
            print("Produto excluido com sucesso!")
        except:
            print("Não foi possível excluir o produto.")
    
    #limpar tela
    def f_limpar_tela(self):
        try:
            print("**************dados disponíveis**************")
            self.txt_codigo.delete(0, tk.END)
            self.txt_nome.delete(0, tk.END)
            self.txt_preco.delete(0, tk.END)
            print("Campos limpoas!")
        except:
            print("Não foi possível limpar os campos.")

# programa principal
janela = tk.TK()
principal = principal_BD(janela)
janela.title("Bem vindo à aplicação de banco de dados")
janela.geometry("720x600+10+10")
janela.mainloop()