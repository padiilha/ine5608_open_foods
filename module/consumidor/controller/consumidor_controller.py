from module.consumidor.view.consumidor_view import ConsumidorView


class ConsumidorController:
    def __init__(self):
        self.__consumidor_view = ConsumidorView()

    def cadastrar_consumidor(self):
        self.__consumidor_view.cadastro_view()
        ...

    def consulta_consumidores(self):
        ...

    def alterar_consumidor(self):
        ...

    def remover_consumidor(self):
        ...

    def get_consumidores_by_cpf(self):
        ...

    def show_main_view(self):
        self.__consumidor_view.main_view()
