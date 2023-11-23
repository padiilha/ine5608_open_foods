from model.municipio import Municipio
from model.usuario import Usuario


class Consumidor(Usuario):
    def __init__(self, nome: str, cpf: str, senha: str, municipio: Municipio):
        super().__init__(nome, cpf, senha, municipio)
