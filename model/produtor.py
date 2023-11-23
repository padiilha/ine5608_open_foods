from model.enum.tipo_certificacao_enum import TipoCertificacaoEnum
from model.enum.tipo_chave_pix_enum import TipoChavePixEnum
from model.feira import Feira
from model.municipio import Municipio
from model.usuario import Usuario


class Produtor(Usuario):
    def __init__(self,
                 nome: str,
                 cpf: str,
                 senha: str,
                 municipio: Municipio,
                 tipo_certificacao: TipoCertificacaoEnum,
                 logradouro: str,
                 numero_logradouro: int,
                 tipo_chave_pix: TipoChavePixEnum,
                 chave_pix: str):
        super().__init__(nome, cpf, senha, municipio)
        self.__nome_fantasia: str or None = None
        self.__cnpj: str or None = None
        self.__tipo_certificacao: TipoCertificacaoEnum = tipo_certificacao
        self.__logradouro: str = logradouro
        self.__numero_logradouro: int = numero_logradouro
        self.__tipo_chave_pix: TipoChavePixEnum = tipo_chave_pix
        self.__chave_pix: str = chave_pix
        self.__feiras: list[Feira] or None = None

    @property
    def nome_fantasia(self) -> str:
        return self.__nome_fantasia

    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia: str):
        self.__nome_fantasia = nome_fantasia

    @property
    def cnpj(self) -> str:
        return self.__cnpj

    @property
    def __tipo_certificacao(self) -> TipoCertificacaoEnum:
        return self.__tipo_certificacao

    @__tipo_certificacao.setter
    def __tipo_certificacao(self, certificacao: TipoCertificacaoEnum):
        self.__tipo_certificacao = certificacao

    @property
    def logradouro(self) -> str:
        return self.__logradouro

    @logradouro.setter
    def logradouro(self, logradouro: str):
        self.__logradouro = logradouro

    @property
    def numero_logradouro(self) -> int:
        return self.__numero_logradouro

    @numero_logradouro.setter
    def numero_logradouro(self, numero_logradouro: int):
        self.__numero_logradouro = numero_logradouro

    @property
    def tipo_chave_pix(self) -> TipoChavePixEnum:
        return self.__tipo_chave_pix

    @tipo_chave_pix.setter
    def tipo_chave_pix(self, tipo_chave_pix: TipoChavePixEnum):
        self.__tipo_chave_pix = tipo_chave_pix

    @property
    def chave_pix(self) -> str:
        return self.__chave_pix

    @chave_pix.setter
    def chave_pix(self, chave_pix: str):
        self.__chave_pix = chave_pix

    @property
    def feiras(self) -> list[Feira]:
        return self.__feiras

    def add_feira(self, feira: Feira):
        self.__feiras.include(feira)

    def remove_feira(self, feira: Feira):
        self.__feiras.remove(feira)
