import tkinter as tk

from tkinter import messagebox

from src.model.enum.uf_enum import UfEnum
from src.module.consumidor.controller.consumidor_controller import ConsumidorController


class ConsumidorCadastroView:
    def __init__(self):
        self.__consumidor_controller = ConsumidorController()
        self.__nome_input = None
        self.__cpf_input = None
        self.__senha_input = None
        self.__telefone_input = None
        self.__municipio_input = None
        self.__uf_selected = None
        self.cadastro_view()

    def cadastrar_consumidor(self):
        nome = self.__nome_input.get()
        cpf = self.__cpf_input.get()
        senha = self.__senha_input.get()
        telefone = self.__telefone_input.get()
        municipio = self.__municipio_input.get()
        uf = self.__uf_selected.get()

        if nome and cpf and senha:
            try:
                self.__consumidor_controller.cadastrar_consumidor(nome, cpf, senha, telefone, municipio, uf)
                messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso")
            except KeyError:
                messagebox.showerror("Erro", "CPF já cadastrado")
        else:
            messagebox.showerror("Erro", "Campos obrigatórios não preenchidos")

    def cadastro_view(self):
        root = tk.Tk()
        root.title("Cadastro de consumidor")

        nome_label = tk.Label(root, text="Nome:")
        nome_label.grid(row=0, column=0, padx=10, pady=10)

        self.__nome_input = tk.Entry(root)
        self.__nome_input.grid(row=0, column=1, padx=10, pady=10)

        cpf_label = tk.Label(root, text="CPF:")
        cpf_label.grid(row=1, column=0, padx=10, pady=10)

        self.__cpf_input = tk.Entry(root)
        self.__cpf_input.grid(row=1, column=1, padx=10, pady=10)

        senha_label = tk.Label(root, text="Senha:")
        senha_label.grid(row=2, column=0, padx=10, pady=10)

        self.__senha_input = tk.Entry(root, show="*")
        self.__senha_input.grid(row=2, column=1, padx=10, pady=10)

        telefone_label = tk.Label(root, text="Telefone:")
        telefone_label.grid(row=3, column=0, padx=10, pady=10)

        self.__telefone_input = tk.Entry(root)
        self.__telefone_input.grid(row=3, column=1, padx=10, pady=10)

        municipio_label = tk.Label(root, text="Município:")
        municipio_label.grid(row=4, column=0, padx=10, pady=10)

        self.__municipio_input = tk.Entry(root)
        self.__municipio_input.grid(row=4, column=1, padx=10, pady=10)

        uf_label = tk.Label(root, text="UF:")
        uf_label.grid(row=5, column=0, padx=10, pady=10)

        uf = [uf.value for uf in UfEnum]
        self.__uf_selected = tk.StringVar()
        self.__uf_selected.set(uf[0])

        uf_dropdown = tk.OptionMenu(root, self.__uf_selected, *uf)
        uf_dropdown.grid(row=5, column=1, padx=10, pady=10)

        button_signup = tk.Button(root, text="Cadastrar", command=self.cadastrar_consumidor)
        button_signup.grid(row=6, column=0, columnspan=2, pady=10)

        root.mainloop()
