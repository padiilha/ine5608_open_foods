import tkinter as tk

from src.module.consumidor.view.consumidor_list_view import ConsumidorListView


class ConsumidorView:
    def __init__(self):
        self.__view = None
        self.main_view()

    def listar_consumidores(self):
        self.__view = ConsumidorListView()

    def catalogo_produtos(self):
        ...

    def main_view(self):
        root = tk.Tk()
        root.title("Consumidor")

        button_signup = tk.Button(root, text="Listar consumidores", command=self.listar_consumidores)
        button_signup.grid(row=0, column=0, columnspan=2, pady=10)

        button_signup = tk.Button(root, text="Abrir catálogo de produtos", command=self.catalogo_produtos)
        button_signup.grid(row=1, column=0, columnspan=2, pady=10)

        root.mainloop()
