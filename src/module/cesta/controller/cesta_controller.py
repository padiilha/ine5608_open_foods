from src.model.consumidor import Consumidor
from src.model.enum.dia_semana_enum import DiaSemanaEnum
from src.model.pedido import Pedido
from src.model.pedido_item import PedidoItem
from src.model.produto import Produto
from src.module.cesta.model.cesta_dao import CestaDAO


class CestaController:
    def __init__(self):
        self.__cesta_dao = CestaDAO()
        self.__produtor = None
        self.__valor_final = 0.0

    def adicionar_item(self, produto: Produto):
        try:
            id_item = self.__cesta_dao.get_last_item_id() + 1
        except Exception:
            id_item = 1

        item = PedidoItem(id_item, produto)
        self.__cesta_dao.add(item)
        self.__produtor = item.produto.produtor

    def remover_item(self, id_item: int):
        self.__cesta_dao.remove(id_item)

    def listar_itens(self) -> list:
        lista_itens = list()

        for item in self.__cesta_dao.get_all():
            lista_itens.append(item)

        if len(lista_itens) > 0:
            return lista_itens
        else:
            raise Exception

    def incrementar_item(self, id_item: int):
        item = self.__cesta_dao.get(id_item)

        if item:
            item.quantidade += 1
            self.__cesta_dao.update()

            return item
        else:
            raise KeyError

    def decrementar_item(self, id_item: int):
        item = self.__cesta_dao.get(id_item)

        if item:
            item.quantidade -= 1
            self.__cesta_dao.update()

            return item
        else:
            raise KeyError

    def esvaziar_cesta(self):
        self.__cesta_dao.clear()
        self.__produtor = None

    def finalizar_pedido(self,
                         consumidor: Consumidor,
                         dia_retirada: DiaSemanaEnum) -> float:
        pedido = Pedido(consumidor, self.__produtor, dia_retirada)

        for item in self.__cesta_dao.get_all():
            item.pedido = pedido
            self.__valor_final += item.produto.preco_unitario * item.quantidade

        self.__cesta_dao.clear()

        return self.__valor_final
