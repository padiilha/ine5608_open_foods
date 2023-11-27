from src.module.login.controller.login_controller import LoginController


class LoginView:
    def __init__(self):
        self.__login_controller = LoginController()
        self.__window = None

    def main_view(self):
        while True:
            cpf_cnpj = input("Insira seu CPF ou CNPJ (sem pontuação): ")
            senha = input("Insira a sua senha: ")

            try:
                self.__login_controller.iniciar_sessao(cpf_cnpj, senha)
                break
            except Exception:
                print("[ERROR] Usuário ou senha inválido(s)")

        try:
            self.__login_controller.redireciona()
        except Exception:
            print("[ERROR] Um erro inesperado ocorreu. Usuário não é instância de Produtor ou instância de Consumidor")
