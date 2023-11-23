from model.enum.dias_semana_enum import DiasSemanaEnum
from model.municipio import Municipio


class Feira:
    def __init__(self, nome: str, municipio: Municipio, dias_semana: DiasSemanaEnum):
        self.__nome: str = nome
        self.__municipio: Municipio = municipio
        self.__dias_semana: DiasSemanaEnum = dias_semana
