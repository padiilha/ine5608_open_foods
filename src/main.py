import tkinter as tk

from src.module.consumidor.view.consumidor_cadastro_view import ConsumidorCadastroView
from src.module.login.view.login_view import LoginView
from src.module.produtor.view.produtor_cadastro_view import ProdutorCadastroView

if __name__ == '__main__':
    root = tk.Tk()
    root.title("OpenFoods")

    button_signup = tk.Button(root, text="Cadastrar consumidor", command=ConsumidorCadastroView)
    button_signup.grid(row=0, column=0, columnspan=2, pady=10)

    button_signup = tk.Button(root, text="Cadastrar produtor", command=ProdutorCadastroView)
    button_signup.grid(row=0, column=2, columnspan=2, pady=10)

    button_signup = tk.Button(root, text="Entrar", command=LoginView)
    button_signup.grid(row=1, column=0, columnspan=4, pady=10)

    root.mainloop()
