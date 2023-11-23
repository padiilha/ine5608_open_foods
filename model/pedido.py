from model.consumidor import Consumidor
from model.enum.dias_semana_enum import DiasSemanaEnum
from model.produtor import Produtor


class Pedido:
    def __init__(self, consumidor: Consumidor, produtor: Produtor, dia_retirada: DiasSemanaEnum):
        self.__consumidor: Consumidor = consumidor
        self.__produtor: Produtor = produtor
        self.__dia_retirada: DiasSemanaEnum = dia_retirada

    @property
    def consumidor(self) -> Consumidor:
        return self.__consumidor

    @property
    def produtor(self) -> Produtor:
        return self.__produtor

    @property
    def dia_retirada(self) -> DiasSemanaEnum:
        return self.__dia_retirada

    @dia_retirada.setter
    def dia_retirada(self, dia_retirada: DiasSemanaEnum):
        self.__dia_retirada = dia_retirada
