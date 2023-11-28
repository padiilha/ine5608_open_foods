from src.model.enum.unidade_medida_enum import UnidadeMedidaEnum
from src.model.produtor import Produtor


class Produto:
    def __init__(self,
                 id_produto: int,
                 nome: str,
                 descricao: str,
                 preco_unitario: float,
                 unidade_medida: UnidadeMedidaEnum,
                 produtor: Produtor):
        self.__id_produto: int = id_produto
        self.__nome: str = nome
        self.__descricao: str = descricao
        self.__preco_unitario: float = preco_unitario
        self.__unidade_medida: UnidadeMedidaEnum = unidade_medida
        self.__produtor: Produtor = produtor

    @property
    def id_produto(self) -> int:
        return self.__id_produto

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
    def unidade_medida(self) -> UnidadeMedidaEnum:
        return self.__unidade_medida

    @unidade_medida.setter
    def unidade_medida(self, unidade_medida: UnidadeMedidaEnum):
        self.__unidade_medida = unidade_medida

    @property
    def produtor(self) -> Produtor:
        return self.__produtor

    @produtor.setter
    def produtor(self, produtor: Produtor):
        self.__produtor = produtor
