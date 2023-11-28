from src.model.enum.dia_semana_enum import DiaSemanaEnum
from src.model.enum.uf_enum import UfEnum
from src.model.feira import Feira
from src.model.municipio import Municipio
from src.model.produtor import Produtor
from src.module.feira.model.feira_dao import FeiraDAO


class FeiraController:
    def __init__(self):
        self.__feira_dao = FeiraDAO()
        self.__id_counter = 1

    def cadastrar_feira(self,
                        nome: str,
                        municipio_nome: str,
                        uf: UfEnum,
                        dia_semana: DiaSemanaEnum) -> Feira:
        municipio = Municipio(municipio_nome, uf)
        feira = Feira(self.__id_counter, nome, municipio, dia_semana)

        self.__feira_dao.add(feira)
        self.__id_counter += 1

        return feira

    def consultar_feira(self, id_feira: int) -> Feira:
        feira = self.__feira_dao.get(id_feira)

        return feira

    def listar_feiras(self) -> list:
        lista_feiras = list()

        for feira in self.__feira_dao.get_all():
            lista_feiras.append(feira)

        if len(lista_feiras) > 0:
            return lista_feiras
        else:
            raise Exception

    def alterar_feira(self,
                      id_feira: int,
                      municipio_nome: str,
                      uf: UfEnum,
                      dia_semana: DiaSemanaEnum) -> Feira:
        feira = self.__feira_dao.get(id_feira)

        if feira:
            municipio = Municipio(municipio_nome, uf)

            feira.municipio = municipio
            feira.dia_semana = dia_semana

            self.__feira_dao.update()

            return feira
        else:
            raise KeyError

    def remover_feira(self, id_feira: int):
        self.__feira_dao.remove(id_feira)

    def vincular_feira(self, produtor: Produtor, id_feira: int):
        feira = self.consultar_feira(id_feira)
        produtor.add_feira(feira)

    def desvincular_feira(self, produtor: Produtor, id_feira: int):
        feira = self.consultar_feira(id_feira)
        produtor.remove_feira(feira)
