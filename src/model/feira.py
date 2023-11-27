from src.model.enum.dia_semana_enum import DiaSemanaEnum
from src.model.municipio import Municipio


class Feira:
    def __init__(self,
                 id_feira: int,
                 nome: str,
                 municipio: Municipio,
                 dia_semana: DiaSemanaEnum):
        self.__id_feira: int = id_feira
        self.__nome: str = nome
        self.__municipio: Municipio = municipio
        self.__dia_semana: DiaSemanaEnum = dia_semana

    @property
    def id_feira(self) -> int:
        return self.__id_feira

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def municipio(self) -> Municipio:
        return self.__municipio

    @municipio.setter
    def municipio(self, municipio: Municipio):
        self.__municipio = municipio

    @property
    def dia_semana(self) -> DiaSemanaEnum:
        return self.__dia_semana

    @dia_semana.setter
    def dia_semana(self, dia_semana: DiaSemanaEnum):
        self.__dia_semana = dia_semana
