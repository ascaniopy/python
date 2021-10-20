import tkinter as tk

class Tela:
    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title("Primeira tela")


# Gerar a nossa interface
janelaRaiz = tk.Tk()

Tela(janelaRaiz)
janelaRaiz.mainloop()
