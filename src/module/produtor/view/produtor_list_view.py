import tkinter as tk

from tkinter import messagebox

from src.module.produtor.controller.produtor_controller import ProdutorController
from src.module.produtor.view.produtor_alterar_view import ProdutorAlterarView


class ProdutorListView:
    def __init__(self):
        self.__produtor_controller = ProdutorController()
        self.__view = None
        self.__produtor = None
        self.__list_view()

    def __alterar_produtor(self):
        self.__view = ProdutorAlterarView(self.__produtor.cpf)

    def __remover_produtor(self):
        self.__produtor_controller.remover_produtor(self.__produtor.cpf)

    def __list_view(self):
        try:
            row_count = 1

            root = tk.Tk()
            root.title("Produtores")

            nome_label = tk.Label(root, text="Nome")
            nome_label.grid(row=0, column=0, padx=10, pady=10)

            cpf_label = tk.Label(root, text="CPF")
            cpf_label.grid(row=0, column=1, padx=10, pady=10)

            telefone_label = tk.Label(root, text="Telefone")
            telefone_label.grid(row=0, column=2, padx=10, pady=10)

            municipio_label = tk.Label(root, text="Município")
            municipio_label.grid(row=0, column=3, padx=10, pady=10)

            uf_label = tk.Label(root, text="UF")
            uf_label.grid(row=0, column=4, padx=10, pady=10)

            nome_fantasia_label = tk.Label(root, text="Nome fantasia")
            nome_fantasia_label.grid(row=0, column=5, padx=10, pady=10)

            cnpj_label = tk.Label(root, text="CNPJ")
            cnpj_label.grid(row=0, column=6, padx=10, pady=10)

            tipo_certificacao_label = tk.Label(root, text="Certificação")
            tipo_certificacao_label.grid(row=0, column=7, padx=10, pady=10)

            logradouro_label = tk.Label(root, text="Logradouro")
            logradouro_label.grid(row=0, column=8, padx=10, pady=10)

            numero_logradouro_label = tk.Label(root, text="Número")
            numero_logradouro_label.grid(row=0, column=9, padx=10, pady=10)

            tipo_chave_pix_label = tk.Label(root, text="Tipo de chave pix")
            tipo_chave_pix_label.grid(row=0, column=10, padx=10, pady=10)

            chave_pix_label = tk.Label(root, text="Chave pix")
            chave_pix_label.grid(row=0, column=11, padx=10, pady=10)

            for produtor in self.__produtor_controller.listar_produtores():
                self.__produtor = produtor

                nome_value = tk.Label(root, text=produtor.nome)
                nome_value.grid(row=row_count, column=0, padx=10, pady=10)

                cpf_value = tk.Label(root, text=produtor.cpf)
                cpf_value.grid(row=row_count, column=1, padx=10, pady=10)

                telefone_value = tk.Label(root, text=produtor.telefone)
                telefone_value.grid(row=row_count, column=2, padx=10, pady=10)

                municipio_value = tk.Label(root, text=produtor.municipio.nome)
                municipio_value.grid(row=row_count, column=3, padx=10, pady=10)

                uf_value = tk.Label(root, text=produtor.municipio.uf)
                uf_value.grid(row=row_count, column=4, padx=10, pady=10)

                nome_fantasia_value = tk.Label(root, text=produtor.nome_fantasia)
                nome_fantasia_value.grid(row=row_count, column=5, padx=10, pady=10)

                cnpj_value = tk.Label(root, text=produtor.cnpj)
                cnpj_value.grid(row=row_count, column=6, padx=10, pady=10)

                tipo_certificacao_value = tk.Label(root, text=produtor.tipo_certificacao)
                tipo_certificacao_value.grid(row=row_count, column=7, padx=10, pady=10)

                logradouro_value = tk.Label(root, text=produtor.logradouro)
                logradouro_value.grid(row=row_count, column=8, padx=10, pady=10)

                numero_logradouro_value = tk.Label(root, text=produtor.numero_logradouro)
                numero_logradouro_value.grid(row=row_count, column=9, padx=10, pady=10)

                tipo_chave_pix_value = tk.Label(root, text=produtor.tipo_chave_pix)
                tipo_chave_pix_value.grid(row=row_count, column=10, padx=10, pady=10)

                chave_pix_value = tk.Label(root, text=produtor.chave_pix)
                chave_pix_value.grid(row=row_count, column=11, padx=10, pady=10)

                button_signup = tk.Button(root, text="Alterar", command=self.__alterar_produtor)
                button_signup.grid(row=row_count, column=12, padx=10, pady=10)

                button_signup = tk.Button(root, text="Remover", command=self.__remover_produtor)
                button_signup.grid(row=row_count, column=13, padx=10, pady=10)

                row_count += 1

            root.mainloop()

        except Exception:
            messagebox.showerror("Erro", "Não há produtores cadastrados")
