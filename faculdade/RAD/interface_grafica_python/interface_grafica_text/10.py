import tkinter as tk

contador = 0

def contador_label(lblRotulo):
    def funcao_contar():
        global contador
        contador += 1
        lblRotulo.config(text=str(contador))
        lblRotulo.after(1000, funcao_contar)  # Chama a função novamente após 1 segundo

    funcao_contar()  # Chama a função uma vez para iniciar a contagem

janela = tk.Tk()
janela.title("Contagem dos Segundos")

lblRotulo = tk.Label(janela, fg="red", font=("Helvetica", 48))  # Aumenta o tamanho da fonte
lblRotulo.pack()

contador_label(lblRotulo)

btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', width=50, command=janela.destroy)
btnAcao.pack()

janela.mainloop()
