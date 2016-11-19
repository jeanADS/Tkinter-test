# -*- coding: utf-8 -*-
# - importando o módulo Tkinter


from tkinter import *


# - iniciando a classe Janela


class Janela(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_janela()

# - iniciando a janela e colocando suas caracteristica

    def init_janela(self):
        self.master.title("Primeiro programa")
        self.pack(fill=BOTH, expand=1)

        # - Aqui é onde é inserido o Label

        texto = Label(self, text="Olá mundo", font="Heveltica, 12", fg="blue")
        texto.pack()

        # - definição da função que vai modificar o label (texto)
        def MudaCor(self):
            texto = Label(self, text="O texto mudou!",
                          font="Heveltica, 12", fg="Red")
            texto.pack()

        # - criação do botão

        botaoEnviar = Button(self, text="Mudar cor", command=self.MudaCor)
        botaoEnviar.pack()


if __name__ == '__main__':

    root = Tk()
    root.geometry("400x300")
    app = Janela(root)
    root.mainloop()
