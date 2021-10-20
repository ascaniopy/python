import tkinter as tk

class Tela:
    def __init__(self, master):
        self.nossaTela = master

        # self.coisa = tk.NomeDoWidget(widgetPai, opcoesDeConfiguracao)

        self.lbl = tk.Label(self.nossaTela, text="Primeiro Label.", background="red")
        self.lbl["font"] = ["Verdana", "16"]
        self.lbl.pack(pady=20, side=tk.LEFT, fill=tk.Y)

        self.lbl2 = tk.Label(self.nossaTela, text="Segundo Label.", background="blue")
        self.lbl2["font"] = ["Verdana", "20"]
        self.lbl2.pack(ipadx=25, ipady=10, side=tk.RIGHT)

        self.lbl3 = tk.Label(self.nossaTela, text="Terceiro Label.", background="green")
        self.lbl3["font"] = ["Verdana", "24"]
        self.lbl3.pack(fill=tk.X)

# Gerar a nossa interface
janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()