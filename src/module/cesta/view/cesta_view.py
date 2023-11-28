import tkinter as tk

from tkinter import messagebox

from src.module.cesta.controller.cesta_controller import CestaController


class CestaView:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__cesta_controller = CestaController()
        self.__item = None
        self.__main_view()
        ...

    def adicionar_item(self, produto):
        self.__cesta_controller.adicionar_item(produto)

    def __retirar_item(self):
        self.__cesta_controller.remover_item(self.__item.id_item)

    def __incrementar_item(self):
        self.__cesta_controller.incrementar_item(self.__item)

    def __decrementar_item(self):
        self.__cesta_controller.decrementar_item(self.__item)

    def __esvaziar_cesta(self):
        self.__cesta_controller.esvaziar_cesta()

    def __finalizar_pedido(self):
        self.__view = CestaFinalizarView(self.__usuario)

    def __main_view(self):
        try:
            row_count = 1

            root = tk.Tk()
            root.title("Cesta")

            id_item_label = tk.Label(root, text="Item")
            id_item_label.grid(row=0, column=0, padx=10, pady=10)

            nome_label = tk.Label(root, text="Nome")
            nome_label.grid(row=0, column=1, padx=10, pady=10)

            preco_unitario_label = tk.Label(root, text="Preço unitário")
            preco_unitario_label.grid(row=0, column=2, padx=10, pady=10)

            unidade_medida_label = tk.Label(root, text="Unidade medida")
            unidade_medida_label.grid(row=0, column=3, padx=10, pady=10)

            quantidade_label = tk.Label(root, text="Quantidade")
            quantidade_label.grid(row=0, column=4, padx=10, pady=10)

            preco_item_label = tk.Label(root, text="Preço item")
            preco_item_label.grid(row=0, column=5, padx=10, pady=10)

            produtor_label = tk.Label(root, text="Produtor")
            produtor_label.grid(row=0, column=6, padx=10, pady=10)

            for item in self.__cesta_controller.listar_itens():
                self.__item = item

                id_item_value = tk.Label(root, text=item.id_item)
                id_item_value.grid(row=row_count, column=0, padx=10, pady=10)

                nome_value = tk.Label(root, text=item.produto.nome)
                nome_value.grid(row=row_count, column=1, padx=10, pady=10)

                preco_unitario_value = tk.Label(root, text=item.produto.preco_unitario)
                preco_unitario_value.grid(row=row_count, column=2, padx=10, pady=10)

                unidade_medida_value = tk.Label(root, text=item.produto.unidade_medida)
                unidade_medida_value.grid(row=row_count, column=3, padx=10, pady=10)

                quantidade_value = tk.Label(root, text=item.quantidade)
                quantidade_value.grid(row=row_count, column=4, padx=10, pady=10)

                preco_item_value = tk.Label(root, text=item.produto.preco_unitario * item.quantidade)
                preco_item_value.grid(row=row_count, column=5, padx=10, pady=10)

                produtor_value = tk.Label(root, text=item.produto.produtor.nome)
                produtor_value.grid(row=row_count, column=6, padx=10, pady=10)

                button_signup = tk.Button(root, text="Incrementar item", command=self.__incrementar_item)
                button_signup.grid(row=row_count, column=7, padx=10, pady=10)

                button_signup = tk.Button(root, text="Decrementar item", command=self.__decrementar_item)
                button_signup.grid(row=row_count, column=8, padx=10, pady=10)

                button_signup = tk.Button(root, text="Retirar da cesta", command=self.__retirar_item)
                button_signup.grid(row=row_count, column=9, padx=10, pady=10)

                row_count += 1

            button_signup = tk.Button(root, text="Esvaziar cesta", command=self.__esvaziar_cesta)
            button_signup.grid(row=row_count, column=0, columnspan=4, pady=10)

            button_signup = tk.Button(root, text="Finalizar pedido", command=self.__finalizar_pedido)
            button_signup.grid(row=row_count, column=4, columnspan=4, pady=10)

            root.mainloop()

        except Exception:
            messagebox.showerror("Erro", "Não há produtos na cesta")
