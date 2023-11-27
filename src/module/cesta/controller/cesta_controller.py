from src.model.consumidor import Consumidor
from src.model.enum.dia_semana_enum import DiaSemanaEnum
from src.model.pedido import Pedido
from src.model.pedido_item import PedidoItem
from src.model.produto import Produto


class CestaController:
    def __init__(self):
        self.__itens_pedido = list()
        self.__id_counter = 1
        self.__produtor = None
        self.__valor_final = 0.0

    def adicionar_item(self, produto: Produto, quantidade: int):
        item = PedidoItem(self.__id_counter, produto, quantidade)
        self.__itens_pedido.append(item)
        self.__id_counter += 1
        self.__produtor = item.produto.produtor

    def remover_item(self, id_item: int):
        self.__itens_pedido.pop(id_item - 1)
        self.__id_counter -= 1

    def listar_itens(self) -> list:
        return self.__itens_pedido

    def esvaziar_cesta(self):
        self.__itens_pedido.clear()
        self.__id_counter = 1

    def incrementar_item(self, id_item: int):
        self.__itens_pedido[id_item].quantidade += 1

    def decrementar_item(self, id_item: int):
        self.__itens_pedido[id_item].quantidade -= 1

    def finalizar_pedido(self,
                         consumidor: Consumidor,
                         dia_retirada: DiaSemanaEnum) -> float:
        pedido = Pedido(consumidor, self.__produtor, dia_retirada)

        for item in self.__itens_pedido:
            item.pedido = pedido
            self.__valor_final += item.produto.preco_unitario * item.quantidade

        return self.__valor_final
