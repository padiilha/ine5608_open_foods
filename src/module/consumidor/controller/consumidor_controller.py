from src.model.consumidor import Consumidor
from src.model.enum.uf_enum import UfEnum
from src.model.municipio import Municipio
from src.module.consumidor.model.consumidor_dao import ConsumidorDAO


class ConsumidorController:
    def __init__(self):
        self.__consumidor_dao = ConsumidorDAO()

    def cadastrar_consumidor(self,
                             nome: str,
                             cpf: str,
                             senha: str,
                             telefone: str,
                             municipio_nome: str,
                             uf: str) -> Consumidor:
        if not self.__consumidor_dao.get(cpf):
            municipio = Municipio(municipio_nome, uf)
            consumidor = Consumidor(nome, cpf, senha, telefone, municipio)

            self.__consumidor_dao.add(consumidor)

            return consumidor
        else:
            raise KeyError

    def consultar_consumidor(self, cpf: str) -> Consumidor:
        consumidor = self.__consumidor_dao.get(cpf)

        if not consumidor:
            return consumidor
        else:
            raise KeyError

    def listar_consumidores(self) -> list:
        lista_consumidores = list()

        for consumidor in self.__consumidor_dao.get_all():
            lista_consumidores.append(consumidor)

        return lista_consumidores

    def alterar_consumidor(self, nome: str, cpf: str, telefone: str, municipio: Municipio) -> Consumidor:
        consumidor = self.__consumidor_dao.get(cpf)

        if not consumidor:
            consumidor.nome = nome
            consumidor.telefone = telefone
            consumidor.municipio = municipio

            self.__consumidor_dao.update()

            return consumidor
        else:
            raise KeyError

    def remover_consumidor(self, cpf: str):
        self.__consumidor_dao.remove(cpf)
