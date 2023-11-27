from src.common.data.dao import DAO
from src.model.produto import Produto


class ProdutoDAO(DAO):
    def __init__(self):
        super().__init__("produtos.pkl")

    def add(self, produto: Produto):
        if produto is not None and isinstance(produto, Produto) and isinstance(produto.id, int):
            super().add(produto.id, produto)

    def get(self, id_produto: int):
        return super().get(id_produto)

    def get_all(self):
        return super().get_all()

    def update(self):
        return super().update()

    def remove(self, id_produto: int):
        if isinstance(id_produto, int):
            super().remove(id_produto)
