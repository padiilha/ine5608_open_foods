import tkinter as tk

from src.module.feira.view.feira_cadastro_view import FeiraCadastroView
from src.module.feira.view.feira_list_view import FeiraListView


class FeiraView:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__view = None
        self.__main_view()

    def __cadastrar_feira(self):
        self.__view = FeiraCadastroView()

    def __listar_feiras(self):
        self.__view = FeiraListView(self.__usuario)

    def __main_view(self):
        root = tk.Tk()
        root.title("Feira")

        button_signup = tk.Button(root, text="Cadastrar feira", command=self.__cadastrar_feira)
        button_signup.grid(row=0, column=0, columnspan=2, pady=10)

        button_signup = tk.Button(root, text="Listar feiras", command=self.__listar_feiras)
        button_signup.grid(row=1, column=0, columnspan=2, pady=10)

        root.mainloop()
