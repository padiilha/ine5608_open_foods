from src.model.pedido import Pedido
from src.model.produto import Produto


class PedidoItem:
    def __init__(self, id_item: int, produto: Produto):
        self.__id_item: int = id_item
        self.__produto: Produto = produto
        self.__quantidade: int = 1
        self.__pedido: Pedido or None = None

    @property
    def id_item(self) -> int:
        return self.__id_item

    @property
    def produto(self) -> Produto:
        return self.__produto

    @produto.setter
    def produto(self, produto: Produto):
        self.__produto = produto

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade

    @property
    def pedido(self) -> Pedido:
        return self.__pedido

    @pedido.setter
    def pedido(self, pedido: Pedido):
        self.__pedido = pedido
