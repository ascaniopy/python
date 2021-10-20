import tkinter as tk

class Tela:
    def __init__(self, master):
        self.nossaTela = master

        # self.coisa = tk.NomeDoWidget(widgetPai, opcoesDeConfiguracao)

        self.lbl = tk.Label(self.nossaTela, text="Olá Mundo!", background="red")
        self.lbl["font"] = ["Verdana", "18"]
        self.lbl.pack()

        self.lbl2 = tk.Label(self.nossaTela, text="Olá Mundo!", background="blue")
        self.lbl2["font"] = ["Verdana", "24"]
        self.lbl2.pack()


# Gerar a nossa interface
janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()