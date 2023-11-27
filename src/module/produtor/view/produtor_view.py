import tkinter as tk

from src.module.produtor.view.produtor_list_view import ProdutorListView


class ProdutorView:
    def __init__(self):
        self.__view = None
        self.main_view()

    def listar_produtores(self):
        self.__view = ProdutorListView()

    def gerenciar_produtos(self):
        ...

    def gerenciar_feiras(self):
        ...

    def main_view(self):
        root = tk.Tk()
        root.title("Produtor")

        button_signup = tk.Button(root, text="Listar produtores", command=self.listar_produtores)
        button_signup.grid(row=0, column=0, columnspan=2, pady=10)

        button_signup = tk.Button(root, text="Gerenciar produtos", command=self.gerenciar_produtos)
        button_signup.grid(row=1, column=0, columnspan=2, pady=10)

        button_signup = tk.Button(root, text="Gerenciar feiras", command=self.gerenciar_feiras)
        button_signup.grid(row=2, column=0, columnspan=2, pady=10)

        root.mainloop()
