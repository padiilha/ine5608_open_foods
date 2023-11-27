import tkinter as tk

from tkinter import messagebox

from src.model.enum.uf_enum import UfEnum
from src.module.consumidor.controller.consumidor_controller import ConsumidorController


class ConsumidorAlterarView:
    def __init__(self, cpf: str):
        self.__consumidor_controller = ConsumidorController()
        self.__nome_input = None
        self.__cpf = cpf
        self.__telefone_input = None
        self.__municipio_input = None
        self.__uf_selected = None
        self.alterar_view()

    def alterar_consumidor(self):
        nome = self.__nome_input.get()
        telefone = self.__telefone_input.get()
        municipio = self.__municipio_input.get()
        uf = self.__uf_selected.get()

        try:
            self.__consumidor_controller.alterar_consumidor(nome, self.__cpf, telefone, municipio, uf)
            messagebox.showinfo("Sucesso", "Consumidor atualizado com sucesso")
        except KeyError:
            messagebox.showerror("Erro", "CPF não encontrado")

    def alterar_view(self):
        try:
            consumidor = self.__consumidor_controller.consultar_consumidor(self.__cpf)

            root = tk.Tk()
            root.title("Atualizar consumidor")

            nome_label = tk.Label(root, text="Nome:")
            nome_label.grid(row=0, column=0, padx=10, pady=10)

            self.__nome_input = tk.Entry(root)
            self.__nome_input.grid(row=0, column=1, padx=10, pady=10)

            cpf_label = tk.Label(root, text="CPF:")
            cpf_label.grid(row=1, column=0, padx=10, pady=10)

            cpf_label = tk.Label(root, text=consumidor.cpf)
            cpf_label.grid(row=1, column=1, padx=10, pady=10)

            telefone_label = tk.Label(root, text="Telefone:")
            telefone_label.grid(row=2, column=0, padx=10, pady=10)

            self.__telefone_input = tk.Entry(root)
            self.__telefone_input.grid(row=2, column=1, padx=10, pady=10)

            municipio_label = tk.Label(root, text="Município:")
            municipio_label.grid(row=3, column=0, padx=10, pady=10)

            self.__municipio_input = tk.Entry(root)
            self.__municipio_input.grid(row=3, column=1, padx=10, pady=10)

            uf_label = tk.Label(root, text="UF:")
            uf_label.grid(row=4, column=0, padx=10, pady=10)

            uf = [uf.value for uf in UfEnum]
            self.__uf_selected = tk.StringVar()
            self.__uf_selected.set(uf[0])

            uf_dropdown = tk.OptionMenu(root, self.__uf_selected, *uf)
            uf_dropdown.grid(row=4, column=1, padx=10, pady=10)

            button_signup = tk.Button(root, text="Atualizar informações", command=self.alterar_consumidor)
            button_signup.grid(row=5, column=0, columnspan=2, pady=10)

            root.mainloop()
        except KeyError:
            messagebox.showerror("Erro", "CPF não encontrado")
