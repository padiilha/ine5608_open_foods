from enum import Enum


class TipoChavePixEnum(Enum):
    CPF_CNPJ = "CPF/CNPJ"
    CELULAR = "Celular"
    EMAIL = "Email"
    CHAVE_ALEATORIA = "Chave aleatória"
