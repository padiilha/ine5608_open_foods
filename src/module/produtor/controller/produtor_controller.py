from src.model.enum.tipo_certificacao_enum import TipoCertificacaoEnum
from src.model.enum.tipo_chave_pix_enum import TipoChavePixEnum
from src.model.feira import Feira
from src.model.municipio import Municipio
from src.model.produtor import Produtor
from src.module.produtor.model.produtor_dao import ProdutorDAO


class ProdutorController:
    def __init__(self):
        self.__produtor_dao = ProdutorDAO()

    def cadastrar_produtor(self,
                           nome: str,
                           cpf: str,
                           senha: str,
                           telefone: str,
                           municipio_nome: str,
                           uf: str,
                           nome_fantasia: str,
                           cnpj: str,
                           tipo_certificacao: TipoCertificacaoEnum,
                           logradouro: str,
                           numero_logradouro: int,
                           tipo_chave_pix: TipoChavePixEnum,
                           chave_pix: str) -> Produtor:
        if not self.__produtor_dao.get(cpf):
            municipio = Municipio(municipio_nome, uf)
            produtor = Produtor(nome,
                                cpf,
                                senha,
                                telefone,
                                municipio,
                                nome_fantasia,
                                cnpj,
                                tipo_certificacao,
                                logradouro,
                                numero_logradouro,
                                tipo_chave_pix,
                                chave_pix)

            self.__produtor_dao.add(produtor)

            return produtor
        else:
            raise Exception

    def consultar_produtor(self, cpf: str) -> Produtor:
        produtor = self.__produtor_dao.get(cpf)

        if produtor:
            return produtor
        else:
            raise KeyError

    def listar_produtores(self) -> list:
        lista_produtores = list()

        for produtor in self.__produtor_dao.get_all():
            lista_produtores.append(produtor)

        if len(lista_produtores) > 0:
            return lista_produtores
        else:
            raise Exception

    def alterar_produtor(self,
                         nome: str,
                         cpf: str,
                         telefone: str,
                         municipio_nome: str,
                         uf: str,
                         nome_fantasia: str,
                         tipo_certificacao: TipoCertificacaoEnum,
                         logradouro: str,
                         numero_logradouro: int,
                         tipo_chave_pix: TipoChavePixEnum,
                         chave_pix: str) -> Produtor:
        produtor = self.__produtor_dao.get(cpf)

        if produtor:
            municipio = Municipio(municipio_nome, uf)

            produtor.nome = nome
            produtor.telefone = telefone
            produtor.municipio = municipio
            produtor.nome_fantasia = nome_fantasia
            produtor.tipo_certificacao = tipo_certificacao
            produtor.logradouro = logradouro
            produtor.numero_logradouro = numero_logradouro
            produtor.tipo_chave_pix = tipo_chave_pix
            produtor.chave_pix = chave_pix

            self.__produtor_dao.update()

            return produtor
        else:
            raise KeyError

    def remover_produtor(self, cpf: str):
        self.__produtor_dao.remove(cpf)

    def vincular_feira(self, cpf: str, feira: Feira):
        produtor = self.consultar_produtor(cpf)
        produtor.add_feira(feira)

    def desvincular_feira(self, cpf: str, feira: Feira):
        produtor = self.consultar_produtor(cpf)
        produtor.remove_feira(feira)
