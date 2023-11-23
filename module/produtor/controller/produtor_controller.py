from module.produtor.view.produtor_view import ProdutorView


class ProdutorController:
    def __init__(self):
        self.__produtor_view = ProdutorView()

    def cadastrar_produtor(self):
        self.__produtor_view.cadastro_view()
        ...

    def consulta_produtores(self):
        ...

    def alterar_produtor(self):
        ...

    def remover_produtor(self):
        ...

    def get_produtores_by_id(self):
        ...

    def show_main_view(self):
        self.__produtor_view.main_view()
