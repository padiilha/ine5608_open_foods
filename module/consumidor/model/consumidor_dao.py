from common.data.dao import DAO
from model.consumidor import Consumidor


class ConsumidorDAO(DAO):
    def __init__(self):
        super().__init__("consumidores.pkl")

    def add(self, consumidor: Consumidor):
        if consumidor is not None and isinstance(consumidor, Consumidor):
            super().add(consumidor.cpf, consumidor)

    def get(self, cpf: str):
        return super().get(cpf)

    def get_all(self):
        return super().get_all()

    def update(self):
        return super().update()

    def remove(self, cpf: str):
        if isinstance(cpf, str):
            super().remove(cpf)
