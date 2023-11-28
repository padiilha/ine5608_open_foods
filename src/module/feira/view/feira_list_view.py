import tkinter as tk

from tkinter import messagebox

from src.module.feira.controller.feira_controller import FeiraController
from src.module.feira.view.feira_alterar_view import FeiraAlterarView


class FeiraListView:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__feira_controller = FeiraController()
        self.__view = None
        self.__feira = None
        self.__list_view()

    def __alterar_feira(self):
        self.__view = FeiraAlterarView(self.__feira.id_feira)

    def __remover_feira(self):
        self.__feira_controller.remover_feira(self.__feira.id_feira)

    def __vincular_feira(self):
        self.__feira_controller.vincular_feira(self.__usuario, self.__feira.id_feira)

    def __desvincular_feira(self):
        self.__feira_controller.desvincular_feira(self.__usuario, self.__feira.id_feira)

    def __list_view(self):
        try:
            row_count = 1

            root = tk.Tk()
            root.title("Feiras")

            nome_label = tk.Label(root, text="Nome")
            nome_label.grid(row=0, column=0, padx=10, pady=10)

            municipio_label = tk.Label(root, text="Município")
            municipio_label.grid(row=0, column=1, padx=10, pady=10)

            uf_label = tk.Label(root, text="UF")
            uf_label.grid(row=0, column=2, padx=10, pady=10)

            dia_semana_label = tk.Label(root, text="Dia da semana")
            dia_semana_label.grid(row=0, column=3, padx=10, pady=10)

            for feira in self.__feira_controller.listar_feiras():
                self.__feira = feira

                nome_value = tk.Label(root, text=feira.nome)
                nome_value.grid(row=row_count, column=0, padx=10, pady=10)

                municipio_value = tk.Label(root, text=feira.municipio.nome)
                municipio_value.grid(row=row_count, column=1, padx=10, pady=10)

                uf_value = tk.Label(root, text=feira.municipio.uf)
                uf_value.grid(row=row_count, column=2, padx=10, pady=10)

                dia_semana_value = tk.Label(root, text=feira.dia_semana)
                dia_semana_value.grid(row=row_count, column=3, padx=10, pady=10)

                button_signup = tk.Button(root, text="Alterar", command=self.__alterar_feira)
                button_signup.grid(row=row_count, column=4, padx=10, pady=10)

                button_signup = tk.Button(root, text="Remover", command=self.__remover_feira)
                button_signup.grid(row=row_count, column=5, padx=10, pady=10)

                button_signup = tk.Button(root, text="Vincular", command=self.__vincular_feira)
                button_signup.grid(row=row_count, column=6, padx=10, pady=10)

                button_signup = tk.Button(root, text="Desvincular", command=self.__desvincular_feira)
                button_signup.grid(row=row_count, column=7, padx=10, pady=10)

                row_count += 1

            root.mainloop()

        except Exception:
            messagebox.showerror("Erro", "Não há feiras cadastradas")
