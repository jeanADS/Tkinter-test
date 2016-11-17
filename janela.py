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

        # - criação do botão
        def MudaCor(self):
            texto = Label(self, text="O texto mudou!",
                          font="Heveltica, 12", fg="Red")
            texto.pack()

        botaoEnviar = Button(self, text="Mudar cor", command=MudaCor)
        botaoEnviar.pack()

        # - Criação da barra de menu

       # menu = Menu(self.master)
       # self.master.config(menu=menu)

      #	file = Menu(menu)
        #file.add_command(label='Sair', command=self.quit)
       # menu.add_cascade(label='Arquivo', menu=file)

        #edit = Menu(menu)
        # edit.add_command(label='Desfazer')
        #menu.add_cascade(label='Editar', menu=edit)


if __name__ == '__main__':

    root = Tk()
    root.geometry("400x300")
    app = Janela(root)
    root.mainloop()
