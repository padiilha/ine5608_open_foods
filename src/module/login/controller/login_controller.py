from src.model.consumidor import Consumidor
from src.model.produtor import Produtor
from src.model.usuario import Usuario
from src.module.consumidor.model.consumidor_dao import ConsumidorDAO
from src.module.consumidor.view.consumidor_view import ConsumidorView
from src.module.produtor.model.produtor_dao import ProdutorDAO
from src.module.produtor.view.produtor_view import ProdutorView


class LoginController:
    def __init__(self):
        self.__produtor_dao = ProdutorDAO()
        self.__consumidor_dao = ConsumidorDAO()
        self.__usuario: Usuario or None = None

    def iniciar_sessao(self, cpf: str, senha: str):
        if not isinstance(cpf, str) or not isinstance(senha, str):
            raise Exception

        if len(cpf) == 11:
            self.__usuario = self.__verifica_cpf(cpf)
        else:
            raise Exception

        if not self.__usuario:
            raise Exception

        if not self.__valida_senha(senha):
            raise Exception

    def redireciona(self):
        if isinstance(self.__usuario, Produtor):
            ProdutorView()
        elif isinstance(self.__usuario, Consumidor):
            ConsumidorView()
        else:
            raise Exception

    def __verifica_cpf(self, cpf: str) -> Usuario or None:
        produtor = self.__produtor_dao.get(cpf)
        consumidor = self.__consumidor_dao.get(cpf)

        if produtor:
            return produtor
        elif consumidor:
            return consumidor

        return None

    def __valida_senha(self, senha: str) -> bool:
        return self.__usuario.senha == senha
