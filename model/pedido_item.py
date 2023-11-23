from model.produto import Produto


class PedidoItem:
    def __init__(self, produto: Produto, quantidade: int):
        self.__produto: Produto = produto
        self.__quantidade: int = quantidade
