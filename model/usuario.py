from abc import ABC, abstractmethod

from model.municipio import Municipio


class Usuario(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: str, senha: str, municipio: Municipio):
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__senha: str = senha
        self.__telefone: str or None = None
        self.__municipio: Municipio = municipio

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, senha: str):
        self.__senha = senha

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone

    @property
    def municipio(self) -> Municipio:
        return self.__municipio

    @municipio.setter
    def municipio(self, municipio: Municipio):
        self.__municipio = municipio
