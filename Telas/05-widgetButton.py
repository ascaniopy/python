import tkinter as tk
from tkinter import messagebox

class Tela:
    def __init__(self, master):
        self.nossaTela = master

        #sef.coisa = tk.NomeDoWidget(widgetPai, opcoesDeConfiuracao)

        self.lbl = tk.Label(self.nossaTela, text="Abrir caixa", font=("Verdana", "16"), relief="raised")
        self.lbl.pack(pady=20)
        self.lbl.bind("<Button-1>", self.clique)
        self.lbl.bind("<ButtonRelease>", self.resposta)
        self.btn = tk.Button(self.nossaTela, text="Clique", font=("Verdana", "16"), command=self.respostabtn)
        self.btn.pack()

    def respostabtn(self):
        messagebox.showinfo("Caixa de mensagem", "Isso é uma mensagem")

    def clique(self, event):
        self.lbl["relief"] = "sunken"

    def resposta(self, event):
        print(event.x, event.y)
        self.lbl["relief"] = "raised"
        messagebox.showinfo("Caixa de mensagem", "Isso é uma mensagem")


# Gerar a nossa interface
janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()