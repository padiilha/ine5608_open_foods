import tkinter as tk

from src.module.consumidor.view.consumidor_list_view import ConsumidorListView
from src.module.produto.view.produto_view import ProdutoView


class ConsumidorView:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__view = None
        self.__main_view()

    def __listar_consumidores(self):
        self.__view = ConsumidorListView()

    def __catalogo_produtos(self):
        self.__view = ProdutoView(self.__usuario)

    def __main_view(self):
        root = tk.Tk()
        root.title("Consumidor")

        button_signup = tk.Button(root, text="Listar consumidores", command=self.__listar_consumidores)
        button_signup.grid(row=0, column=0, columnspan=2, pady=10)

        button_signup = tk.Button(root, text="Abrir catálogo de produtos", command=self.__catalogo_produtos)
        button_signup.grid(row=1, column=0, columnspan=2, pady=10)

        root.mainloop()
