from model.consumidor import Consumidor
from model.produtor import Produtor
from model.usuario import Usuario
from module.consumidor.controller.consumidor_controller import ConsumidorController
from module.consumidor.model.consumidor_dao import ConsumidorDAO
from module.produtor.controller.produtor_controller import ProdutorController
from module.produtor.model.produtor_dao import ProdutorDAO


class LoginController:
    def __init__(self):
        self.__produtor_controller = ProdutorController()
        self.__consumidor_controller = ConsumidorController()
        self.__produtor_dao = ProdutorDAO()
        self.__consumidor_dao = ConsumidorDAO()
        self.__usuario: Usuario or None = None

    def iniciar_sessao(self, cpf_cnpj: str, senha: str):
        if not isinstance(cpf_cnpj, str) or not isinstance(senha, str):
            raise Exception

        if len(cpf_cnpj) == 11:
            self.__usuario = self.__verifica_cpf(cpf_cnpj)
        elif len(cpf_cnpj) == 14:
            self.__usuario = self.__verifica_cnpj(cpf_cnpj)
        else:
            raise Exception

        if not self.__usuario:
            raise Exception

        if not self.__valida_senha(senha):
            raise Exception

    def redireciona(self):
        if isinstance(self.__usuario, Produtor):
            self.__produtor_controller.show_main_view()
        elif isinstance(self.__usuario, Consumidor):
            self.__consumidor_controller.show_main_view()
        else:
            raise Exception

    def __verifica_cpf(self, cpf: str) -> Usuario or None:
        for produtor in self.__produtor_dao.get_all():
            if produtor.cpf == cpf:
                return produtor

        for consumidor in self.__consumidor_dao.get_all():
            if consumidor.cpf == cpf:
                return consumidor

        return None

    def __verifica_cnpj(self, cnpj: str) -> Usuario or None:
        for produtor in self.__produtor_dao.get_all():
            if produtor.cnpj == cnpj:
                return produtor

        return None

    def __valida_senha(self, senha: str) -> bool:
        return self.__usuario.senha == senha
