from src.common.data.dao import DAO
from src.model.pedido_item import PedidoItem


class CestaDAO(DAO):
    def __init__(self):
        super().__init__("cesta.pkl")

    def add(self, item: PedidoItem):
        if item is not None and isinstance(item, PedidoItem) and isinstance(item.id_item, int):
            super().add(item.id_item, item)

    def get(self, id_item: int):
        return super().get(id_item)

    def get_all(self):
        return super().get_all()

    def update(self):
        return super().update()

    def remove(self, id_item: int):
        if isinstance(id_item, int):
            super().remove(id_item)
