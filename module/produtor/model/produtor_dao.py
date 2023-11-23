from common.data.dao import DAO
from model.produtor import Produtor


class ProdutorDAO(DAO):
    def __init__(self):
        super().__init__("produtores.pkl")

    def add(self, produtor: Produtor):
        if produtor is not None and isinstance(produtor, Produtor):
            super().add(produtor.cpf, produtor)

    def get(self, cpf: str):
        return super().get(cpf)

    def get_all(self):
        return super().get_all()

    def update(self):
        return super().update()

    def remove(self, cpf: str):
        if isinstance(cpf, str):
            super().remove(cpf)
