from src.model.enum.uf_enum import UfEnum


class Municipio:
    def __init__(self, nome: str, uf: UfEnum):
        self.__nome: str = nome
        self.__uf: UfEnum = uf
