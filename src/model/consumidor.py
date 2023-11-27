from src.model.municipio import Municipio
from src.model.usuario import Usuario


class Consumidor(Usuario):
    def __init__(self, nome: str, cpf: str, senha: str, telefone: str, municipio: Municipio):
        super().__init__(nome, cpf, senha, telefone, municipio)
