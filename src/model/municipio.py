

class Municipio:
    def __init__(self, nome: str, uf: str):
        self.__nome: str = nome
        self.__uf: str = uf

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def uf(self) -> str:
        return self.__uf

    @uf.setter
    def uf(self, uf: str):
        self.__uf = uf
