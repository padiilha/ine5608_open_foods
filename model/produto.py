from model.produtor import Produtor


class Produto:
    def __init__(self, nome: str, preco_unitario: float, produtor: Produtor):
        self.__nome: str = nome
        self.__descricao: str or None = None
        self.__preco_unitario: float = preco_unitario
        self.__produtor: Produtor = produtor

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def preco_unitario(self) -> float:
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario: float):
        self.__preco_unitario = preco_unitario

    @property
    def produtor(self) -> Produtor:
        return self.__produtor

    @produtor.setter
    def produtor(self, produtor: Produtor):
        self.__produtor = produtor
