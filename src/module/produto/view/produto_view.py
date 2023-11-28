import tkinter as tk

from src.model.consumidor import Consumidor
from src.module.produto.view.produto_cadastro_view import ProdutoCadastroView
from src.module.produto.view.produto_list_view import ProdutoListView


class ProdutoView:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__view = None
        self.__main_view()

    def __cadastrar_produto(self):
        self.__view = ProdutoCadastroView(self.__usuario)

    def __listar_produtos(self):
        self.__view = ProdutoListView(self.__usuario)

    def __main_view(self):
        if isinstance(self.__usuario, Consumidor):
            self.__listar_produtos()
        else:
            root = tk.Tk()
            root.title("Produto")

            button_signup = tk.Button(root, text="Cadastrar produto", command=self.__cadastrar_produto)
            button_signup.grid(row=0, column=0, columnspan=2, pady=10)

            button_signup = tk.Button(root, text="Listar produtos", command=self.__listar_produtos)
            button_signup.grid(row=1, column=0, columnspan=2, pady=10)

            root.mainloop()
