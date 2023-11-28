from src.model.enum.unidade_medida_enum import UnidadeMedidaEnum
from src.model.produto import Produto
from src.model.produtor import Produtor
from src.module.produto.model.produto_dao import ProdutoDAO


class ProdutoController:
    def __init__(self):
        self.__produtos_dao = ProdutoDAO()
        self.__id_counter = 1

    def cadastrar_produto(self,
                          nome: str,
                          descricao: str,
                          preco_unitario: float,
                          unidade_medida: UnidadeMedidaEnum,
                          produtor: Produtor) -> Produto:
        produto = Produto(self.__id_counter,
                          nome,
                          descricao,
                          preco_unitario,
                          unidade_medida,
                          produtor)

        self.__produtos_dao.add(produto)
        self.__id_counter += 1

        return produto

    def consultar_produto(self, id_produto: int) -> Produto:
        produto = self.__produtos_dao.get(id_produto)

        if not produto:
            return produto
        else:
            raise KeyError

    def listar_produtos(self) -> list:
        lista_produtos = list()

        for produto in self.__produtos_dao.get_all():
            lista_produtos.append(produto)

        if len(lista_produtos) > 0:
            return lista_produtos
        else:
            raise Exception

    def alterar_produto(self,
                        id_produto: int,
                        descricao: str,
                        preco_unitario: float,
                        unidade_medida: UnidadeMedidaEnum) -> Produto:
        produto = self.__produtos_dao.get(id_produto)

        if produto:
            produto.descricao = descricao
            produto.preco_unitario = preco_unitario
            produto.unidade_medida = unidade_medida

            self.__produtos_dao.update()

            return produto
        else:
            raise KeyError

    def remover_produto(self, id_produto: int):
        self.__produtos_dao.remove(id_produto)
