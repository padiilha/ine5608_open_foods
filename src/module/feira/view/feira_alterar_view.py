import tkinter as tk

from tkinter import messagebox

from src.model.enum.dia_semana_enum import DiaSemanaEnum
from src.model.enum.uf_enum import UfEnum
from src.module.feira.controller.feira_controller import FeiraController


class FeiraAlterarView:
    def __init__(self, id_feira: int):
        self.__feira_controller = FeiraController()
        self.__id_feira = id_feira
        self.__municipio_input = None
        self.__uf_selected = None
        self.__dia_semana_selected = None
        self.__alterar_view()

    def __alterar_feira(self):
        municipio = self.__municipio_input.get()
        uf = self.__uf_selected.get()
        dia_semana = self.__dia_semana_selected.get()

        try:
            self.__feira_controller.alterar_feira(self.__id_feira, municipio, uf, dia_semana)
            messagebox.showinfo("Sucesso", "Feira atualizada com sucesso")
        except KeyError:
            messagebox.showerror("Erro", "Feira não encontrada")

    def __alterar_view(self):
        try:
            feira = self.__feira_controller.consultar_feira(self.__id_feira)

            root = tk.Tk()
            root.title("Atualizar feira")

            nome_label = tk.Label(root, text="Nome:")
            nome_label.grid(row=0, column=0, padx=10, pady=10)

            nome_value = tk.Label(root, text=feira.nome)
            nome_value.grid(row=0, column=1, padx=10, pady=10)

            municipio_label = tk.Label(root, text="Município:")
            municipio_label.grid(row=1, column=0, padx=10, pady=10)

            self.__municipio_input = tk.Entry(root)
            self.__municipio_input.grid(row=1, column=1, padx=10, pady=10)

            uf_label = tk.Label(root, text="UF:")
            uf_label.grid(row=2, column=0, padx=10, pady=10)

            uf = [uf.value for uf in UfEnum]
            self.__uf_selected = tk.StringVar()
            self.__uf_selected.set(uf[0])

            uf_dropdown = tk.OptionMenu(root, self.__uf_selected, *uf)
            uf_dropdown.grid(row=2, column=1, padx=10, pady=10)

            dia_semana_label = tk.Label(root, text="Dia da semana:")
            dia_semana_label.grid(row=3, column=0, padx=10, pady=10)

            dia_semana = [dia_semana.value for dia_semana in DiaSemanaEnum]
            self.__dia_semana_selected = tk.StringVar()
            self.__dia_semana_selected.set(dia_semana[0])

            dia_semana_dropdown = tk.OptionMenu(root, self.__dia_semana_selected, *dia_semana)
            dia_semana_dropdown.grid(row=3, column=1, padx=10, pady=10)

            button_signup = tk.Button(root, text="Atualizar informações", command=self.__alterar_feira)
            button_signup.grid(row=4, column=0, columnspan=4, pady=10)

            root.mainloop()

        except KeyError:
            messagebox.showerror("Erro", "Feira não encontrada")
