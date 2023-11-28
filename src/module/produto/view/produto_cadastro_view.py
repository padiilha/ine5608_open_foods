import tkinter as tk
from tkinter import messagebox

from src.model.enum.unidade_medida_enum import UnidadeMedidaEnum
from src.module.produto.controller.produto_controller import ProdutoController


class ProdutoCadastroView:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__produto_controller = ProdutoController()
        self.__nome_input = None
        self.__descricao_input = None
        self.__preco_unitario_input = None
        self.__unidade_medida_selected = None
        self.__cadastro_view()

    def __cadastrar_produto(self):
        nome = self.__nome_input.get()
        descricao = self.__descricao_input.get()
        preco_unitario = self.__preco_unitario_input.get()
        unidade_medida = self.__unidade_medida_selected.get()

        if nome and preco_unitario:
            try:
                self.__produto_controller.cadastrar_produto(nome,
                                                            descricao,
                                                            preco_unitario,
                                                            unidade_medida,
                                                            self.__usuario)
                messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso")
            except Exception:
                messagebox.showerror("Erro", "Ocorreu um erro ao tentar cadastrar produto")
        else:
            messagebox.showerror("Erro", "Campos obrigatórios não preenchidos")

    def __cadastro_view(self):
        root = tk.Tk()
        root.title("Cadastro de produto")

        nome_label = tk.Label(root, text="Nome:")
        nome_label.grid(row=0, column=0, padx=10, pady=10)

        self.__nome_input = tk.Entry(root)
        self.__nome_input.grid(row=0, column=1, padx=10, pady=10)

        descricao_label = tk.Label(root, text="Descrição:")
        descricao_label.grid(row=1, column=0, padx=10, pady=10)

        self.__descricao_input = tk.Entry(root)
        self.__descricao_input.grid(row=1, column=1, padx=10, pady=10)

        preco_unitario_label = tk.Label(root, text="Preço unitário:")
        preco_unitario_label.grid(row=2, column=0, padx=10, pady=10)

        self.__preco_unitario_input = tk.Entry(root)
        self.__preco_unitario_input.grid(row=2, column=1, padx=10, pady=10)

        unidade_medida_label = tk.Label(root, text="Unidade de medida:")
        unidade_medida_label.grid(row=3, column=0, padx=10, pady=10)

        unidade_medida = [unidade_medida.value for unidade_medida in UnidadeMedidaEnum]
        self.__unidade_medida_selected = tk.StringVar()
        self.__unidade_medida_selected.set(unidade_medida[0])

        unidade_medida_dropdown = tk.OptionMenu(root, self.__unidade_medida_selected, *unidade_medida)
        unidade_medida_dropdown.grid(row=3, column=1, padx=10, pady=10)

        button_signup = tk.Button(root, text="Cadastrar", command=self.__cadastrar_produto)
        button_signup.grid(row=4, column=0, columnspan=4, pady=10)

        root.mainloop()
