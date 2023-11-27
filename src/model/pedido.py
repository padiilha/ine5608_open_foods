from src.model.consumidor import Consumidor
from src.model.enum.dia_semana_enum import DiaSemanaEnum
from src.model.produtor import Produtor


class Pedido:
    def __init__(self,
                 consumidor: Consumidor,
                 produtor: Produtor,
                 dia_retirada: DiaSemanaEnum):
        self.__consumidor: Consumidor = consumidor
        self.__produtor: Produtor = produtor
        self.__dia_retirada: DiaSemanaEnum = dia_retirada

    @property
    def consumidor(self) -> Consumidor:
        return self.__consumidor

    @property
    def produtor(self) -> Produtor:
        return self.__produtor

    @property
    def dia_retirada(self) -> DiaSemanaEnum:
        return self.__dia_retirada

    @dia_retirada.setter
    def dia_retirada(self, dia_retirada: DiaSemanaEnum):
        self.__dia_retirada = dia_retirada
