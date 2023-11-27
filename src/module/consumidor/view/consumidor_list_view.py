import tkinter as tk
from tkinter import messagebox

from src.module.consumidor.controller.consumidor_controller import ConsumidorController
from src.module.consumidor.view.consumidor_alterar_view import ConsumidorAlterarView


class ConsumidorListView:
    def __init__(self):
        self.__consumidor_controller = ConsumidorController()
        self.__view = None
        self.__consumidor = None
        self.list_view()

    def alterar_consumidor(self):
        self.__view = ConsumidorAlterarView(self.__consumidor.cpf)

    def remover_consumidor(self):
        self.__consumidor_controller.remover_consumidor(self.__consumidor.cpf)

    def list_view(self):
        try:
            row_count = 1

            root = tk.Tk()
            root.title("Consumidores")

            nome_label = tk.Label(root, text="Nome")
            nome_label.grid(row=0, column=0, padx=10, pady=10)

            cpf_label = tk.Label(root, text="CPF")
            cpf_label.grid(row=0, column=1, padx=10, pady=10)

            telefone_label = tk.Label(root, text="Telefone")
            telefone_label.grid(row=0, column=2, padx=10, pady=10)

            municipio_label = tk.Label(root, text="Município")
            municipio_label.grid(row=0, column=3, padx=10, pady=10)

            uf_label = tk.Label(root, text="UF")
            uf_label.grid(row=0, column=4, padx=10, pady=10)

            for consumidor in self.__consumidor_controller.listar_consumidores():
                self.__consumidor = consumidor

                nome_value = tk.Label(root, text=consumidor.nome)
                nome_value.grid(row=row_count, column=0, padx=10, pady=10)

                cpf_value = tk.Label(root, text=consumidor.cpf)
                cpf_value.grid(row=row_count, column=1, padx=10, pady=10)

                telefone_value = tk.Label(root, text=consumidor.telefone)
                telefone_value.grid(row=row_count, column=2, padx=10, pady=10)

                municipio_value = tk.Label(root, text=consumidor.municipio.nome)
                municipio_value.grid(row=row_count, column=3, padx=10, pady=10)

                uf_value = tk.Label(root, text=consumidor.municipio.uf)
                uf_value.grid(row=row_count, column=4, padx=10, pady=10)

                button_signup = tk.Button(root, text="Alterar", command=self.alterar_consumidor)
                button_signup.grid(row=row_count, column=5, padx=10, pady=10)

                button_signup = tk.Button(root, text="Remover", command=self.remover_consumidor)
                button_signup.grid(row=row_count, column=6, padx=10, pady=10)

                row_count += 1

            root.mainloop()

        except Exception:
            messagebox.showerror("Erro", "Não há consumidores cadastrados")
