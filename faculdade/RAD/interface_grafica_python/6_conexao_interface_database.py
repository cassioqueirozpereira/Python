import tkinter as tk
from tkinter import ttk
import class_database as crud

class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()
        self.lb_codigo = tk.Label(win, text="Código do Produto:")
        self.lb_nome = tk.Label(win, text="Nome do Produto:")
        self.lb_preco = tk.Label(win, text="Preço:")

        self.txt_codigo = tk.Entry()
        self.txt_nome = tk.Entry()
        self.txt_preco = tk.Entry()
        self.btn_cadastrar = tk.Button(win, text="CADASTRAR", command=self.f_cadastrar_produto)
        self.btn_atualizar = tk.Button(win, text="ATUALIZAR", command=self.f_atualizar_produto)
        self.btn_excluir = tk.Button(win, text="EXCLUIR", command=self.f_excluir_produto)
        self.btn_limpar = tk.Button(win, text="LIMPAR", command=self.f_limpar_tela)

        self.dados_colunas = ("CÓDIGO", "NOME", "PREÇO")
        self.tree_produtos = ttk.Treeview(win, columns=self.dados_colunas, selectmode="browse")
        self.verscrlbar = ttk.Scrollbar(win, orient="vertical", command=self.tree_produtos.yview)

        self.verscrlbar.pack(side="right", fill="y")
        self.tree_produtos.configure(yscrollcommand=self.verscrlbar.set)

        for coluna in self.dados_colunas:
            self.tree_produtos.heading(coluna, text=coluna)
            self.tree_produtos.column(coluna, minwidth=0, width=100)

        self.tree_produtos.pack(padx=10, pady=10)
        self.tree_produtos.bind("<<TreeviewSelect>>", self.apresentar_registros_selecionados)

        self.lb_codigo.place(x=100, y=50)
        self.txt_codigo.place(x=250, y=50)
        self.lb_nome.place(x=100, y=100)
        self.txt_nome.place(x=250, y=100)
        self.lb_preco.place(x=100, y=150)
        self.txt_preco.place(x=250, y=150)
        self.btn_cadastrar.place(x=100, y=200)
        self.btn_atualizar.place(x=200, y=200)
        self.btn_excluir.place(x=300, y=200)
        self.btn_limpar.place(x=400, y=200)
        self.tree_produtos.place(x=100, y=300)
        self.verscrlbar.place(x=605, y=300, height=225)

        self.carregar_dados_iniciais()
    
    def apresentar_registros_selecionados(self, event):
        self.f_limpar_tela()
        for selection in self.tree_produtos.selection():
            item = self.tree_produtos.item(selection)
            codigo, nome, preco = item["values"]
            self.txt_codigo.insert(0, codigo)
            self.txt_nome.insert(0, nome)
            self.txt_preco.insert(0, preco)

    def carregar_dados_iniciais(self):
        try:
            registros = self.objBD.selecionar_dados()
            for item in registros:
                self.tree_produtos.insert("", "end", values=item)
        except Exception as e:
            print("Erro ao carregar dados:", e)

    def f_ler_campos(self):
        try:
            codigo = int(self.txt_codigo.get())
            nome = self.txt_nome.get()
            preco = float(self.txt_preco.get())
            return codigo, nome, preco
        except Exception as e:
            print("Erro ao ler campos:", e)
            return None, None, None

    def f_cadastrar_produto(self):
        codigo, nome, preco = self.f_ler_campos()
        if None not in (codigo, nome, preco):
            try:
                self.objBD.inserir_dados(codigo, nome, preco)
                # Se a inserção foi bem-sucedida, adicione à árvore
                self.tree_produtos.insert('', 'end', values=(codigo, nome, preco))
                self.f_limpar_tela()
                print("Produto cadastrado com sucesso!")
            except Exception as e:
                print("Não foi possível fazer o cadastro:", e)  # Mensagem de erro


    def f_atualizar_produto(self):
        codigo, nome, preco = self.f_ler_campos()
        if None not in (codigo, nome, preco):
            self.objBD.atualizar_dados(codigo, nome, preco)
            self.carregar_dados_iniciais()
            self.f_limpar_tela()
            print("Produto atualizado com sucesso!")

    def f_excluir_produto(self):
        codigo, _, _ = self.f_ler_campos()
        if codigo is not None:
            self.objBD.excluir_dados(codigo)
            self.carregar_dados_iniciais()
            self.f_limpar_tela()
            print("Produto excluído com sucesso!")

    def f_limpar_tela(self):
        self.txt_codigo.delete(0, tk.END)
        self.txt_nome.delete(0, tk.END)
        self.txt_preco.delete(0, tk.END)
        print("Campos limpos!")

# Programa principal
janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title("Bem vindo à aplicação de banco de dados")
janela.geometry("720x600+10+10")
janela.mainloop()
