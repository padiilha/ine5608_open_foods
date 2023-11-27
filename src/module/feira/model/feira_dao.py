from src.common.data.dao import DAO
from src.model.feira import Feira


class FeiraDAO(DAO):
    def __init__(self):
        super().__init__("feiras.pkl")

    def add(self, feira: Feira):
        if feira is not None and isinstance(feira, Feira) and isinstance(feira.id_feira, str):
            super().add(feira.id_feira, feira)

    def get(self, id_feira: int):
        return super().get(id_feira)

    def get_all(self):
        return super().get_all()

    def update(self):
        return super().update()

    def remove(self, id_feira: int):
        if isinstance(id_feira, int):
            super().remove(id_feira)
