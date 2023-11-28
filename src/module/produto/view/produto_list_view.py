import tkinter as tk

from tkinter import messagebox

from src.model.consumidor import Consumidor
from src.module.produto.controller.produto_controller import ProdutoController
from src.module.produto.view.produto_alterar_view import ProdutoAlterarView


class ProdutoListView:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__produto_controller = ProdutoController()
        self.__view = None
        self.__produto = None
        self.__list_view()

    def __alterar_produto(self):
        self.__view = ProdutoAlterarView(self.__produto.id_produto, self.__usuario)

    def __remover_produto(self):
        self.__produto_controller.remover_produto(self.__produto.id_produto)

    def __list_view(self):
        try:
            row_count = 1

            root = tk.Tk()
            root.title("Produtos")

            nome_label = tk.Label(root, text="Nome")
            nome_label.grid(row=0, column=0, padx=10, pady=10)

            descricao_label = tk.Label(root, text="Descrição")
            descricao_label.grid(row=0, column=1, padx=10, pady=10)

            preco_unitario_label = tk.Label(root, text="Preço unitário")
            preco_unitario_label.grid(row=0, column=2, padx=10, pady=10)

            unidade_medida_label = tk.Label(root, text="Unidade medida")
            unidade_medida_label.grid(row=0, column=3, padx=10, pady=10)

            produtor_label = tk.Label(root, text="Produtor")
            produtor_label.grid(row=0, column=4, padx=10, pady=10)

            for produto in self.__produto_controller.listar_produtos():
                self.__produto = produto

                nome_value = tk.Label(root, text=produto.nome)
                nome_value.grid(row=row_count, column=0, padx=10, pady=10)

                descricao_value = tk.Label(root, text=produto.descricao)
                descricao_value.grid(row=row_count, column=1, padx=10, pady=10)

                preco_unitario_value = tk.Label(root, text=produto.preco_unitario)
                preco_unitario_value.grid(row=row_count, column=2, padx=10, pady=10)

                unidade_medida_value = tk.Label(root, text=produto.unidade_medida)
                unidade_medida_value.grid(row=row_count, column=3, padx=10, pady=10)

                produtor_value = tk.Label(root, text=produto.produtor.nome)
                produtor_value.grid(row=row_count, column=4, padx=10, pady=10)

                if isinstance(self.__usuario, Consumidor):
                    ...
                else:
                    button_signup = tk.Button(root, text="Alterar", command=self.__alterar_produto)
                    button_signup.grid(row=row_count, column=5, padx=10, pady=10)

                    button_signup = tk.Button(root, text="Remover", command=self.__remover_produto)
                    button_signup.grid(row=row_count, column=6, padx=10, pady=10)

                row_count += 1

            root.mainloop()

        except Exception:
            messagebox.showerror("Erro", "Não há produtos cadastradas")
