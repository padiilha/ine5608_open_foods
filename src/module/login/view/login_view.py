import tkinter as tk

from tkinter import messagebox

from src.module.login.controller.login_controller import LoginController


class LoginView:
    def __init__(self):
        self.__login_controller = LoginController()
        self.__cpf_input = None
        self.__senha_input = None
        self.__login_view()

    def __iniciar_sessao(self):
        cpf = self.__cpf_input.get()
        senha = self.__senha_input.get()

        if cpf and senha:
            try:
                self.__login_controller.iniciar_sessao(cpf, senha)
                self.__login_controller.redireciona()
            except Exception:
                messagebox.showerror("Erro", "Usuário ou senha inválido(s)")
        else:
            messagebox.showerror("Erro", "Campos obrigatórios não preenchidos")

    def __login_view(self):
        root = tk.Tk()
        root.title("Login")

        cpf_label = tk.Label(root, text="CPF:")
        cpf_label.grid(row=1, column=0, padx=10, pady=10)

        self.__cpf_input = tk.Entry(root)
        self.__cpf_input.grid(row=1, column=1, padx=10, pady=10)

        senha_label = tk.Label(root, text="Senha:")
        senha_label.grid(row=2, column=0, padx=10, pady=10)

        self.__senha_input = tk.Entry(root, show="*")
        self.__senha_input.grid(row=2, column=1, padx=10, pady=10)

        button_signup = tk.Button(root, text="Entrar", command=self.__iniciar_sessao)
        button_signup.grid(row=6, column=0, columnspan=2, pady=10)

        root.mainloop()
