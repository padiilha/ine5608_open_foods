from src.model.enum.uf_enum import UfEnum


class Municipio:
    def __init__(self, nome: str, uf: UfEnum):
        self.__nome: str = nome
        self.__uf: UfEnum = uf

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def uf(self) -> UfEnum:
        return self.__uf

    @uf.setter
    def uf(self, uf: UfEnum):
        self.__uf = uf
