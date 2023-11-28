import tkinter as tk

from src.module.feira.view.feira_view import FeiraView
from src.module.produto.view.produto_view import ProdutoView
from src.module.produtor.view.produtor_list_view import ProdutorListView


class ProdutorView:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__view = None
        self.__main_view()

    def __listar_produtores(self):
        self.__view = ProdutorListView()

    def __gerenciar_produtos(self):
        self.__view = ProdutoView(self.__usuario)

    def __gerenciar_feiras(self):
        self.__view = FeiraView(self.__usuario)

    def __main_view(self):
        root = tk.Tk()
        root.title("Produtor")

        button_signup = tk.Button(root, text="Listar produtores", command=self.__listar_produtores)
        button_signup.grid(row=0, column=0, columnspan=2, pady=10)

        button_signup = tk.Button(root, text="Gerenciar produtos", command=self.__gerenciar_produtos)
        button_signup.grid(row=1, column=0, columnspan=2, pady=10)

        button_signup = tk.Button(root, text="Gerenciar feiras", command=self.__gerenciar_feiras)
        button_signup.grid(row=2, column=0, columnspan=2, pady=10)

        root.mainloop()
