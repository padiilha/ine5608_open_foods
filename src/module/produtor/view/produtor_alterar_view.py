import tkinter as tk

from tkinter import messagebox

from src.model.enum.tipo_certificacao_enum import TipoCertificacaoEnum
from src.model.enum.tipo_chave_pix_enum import TipoChavePixEnum
from src.model.enum.uf_enum import UfEnum
from src.module.produtor.controller.produtor_controller import ProdutorController


class ProdutorAlterarView:
    def __init__(self, cpf: str):
        self.__produtor_controller = ProdutorController()
        self.__nome_input = None
        self.__cpf = cpf
        self.__telefone_input = None
        self.__municipio_input = None
        self.__uf_selected = None
        self.__nome_fantasia_input = None
        self.__tipo_certificacao_selected = None
        self.__logradouro_input = None
        self.__numero_logradouro_input = None
        self.__tipo_chave_pix_selected = None
        self.__chave_pix_input = None
        self.alterar_view()

    def alterar_produtor(self):
        nome = self.__nome_input.get()
        telefone = self.__telefone_input.get()
        municipio = self.__municipio_input.get()
        uf = self.__uf_selected.get()
        nome_fantasia = self.__nome_fantasia_input.get()
        tipo_certificacao = self.__tipo_certificacao_selected.get()
        logradouro = self.__logradouro_input.get()
        numero_logradouro = self.__numero_logradouro_input.get()
        tipo_chave_pix = self.__tipo_chave_pix_selected.get()
        chave_pix = self.__chave_pix_input.get()

        try:
            self.__produtor_controller.alterar_produtor(nome,
                                                        self.__cpf,
                                                        telefone,
                                                        municipio,
                                                        uf,
                                                        nome_fantasia,
                                                        tipo_certificacao,
                                                        logradouro,
                                                        numero_logradouro,
                                                        tipo_chave_pix,
                                                        chave_pix)
            messagebox.showinfo("Sucesso", "Produtor atualizado com sucesso")
        except KeyError:
            messagebox.showerror("Erro", "CPF não encontrado")

    def alterar_view(self):
        try:
            produtor = self.__produtor_controller.consultar_produtor(self.__cpf)

            root = tk.Tk()
            root.title("Atualizar produtor")

            nome_label = tk.Label(root, text="Nome:")
            nome_label.grid(row=0, column=0, padx=10, pady=10)

            self.__nome_input = tk.Entry(root)
            self.__nome_input.grid(row=0, column=1, padx=10, pady=10)

            cpf_label = tk.Label(root, text="CPF:")
            cpf_label.grid(row=1, column=0, padx=10, pady=10)

            cpf_label = tk.Label(root, text=produtor.cpf)
            cpf_label.grid(row=1, column=1, padx=10, pady=10)

            telefone_label = tk.Label(root, text="Telefone:")
            telefone_label.grid(row=2, column=0, padx=10, pady=10)

            self.__telefone_input = tk.Entry(root)
            self.__telefone_input.grid(row=2, column=1, padx=10, pady=10)

            municipio_label = tk.Label(root, text="Município:")
            municipio_label.grid(row=3, column=0, padx=10, pady=10)

            self.__municipio_input = tk.Entry(root)
            self.__municipio_input.grid(row=3, column=1, padx=10, pady=10)

            uf_label = tk.Label(root, text="UF:")
            uf_label.grid(row=4, column=0, padx=10, pady=10)

            uf = [uf.value for uf in UfEnum]
            self.__uf_selected = tk.StringVar()
            self.__uf_selected.set(uf[0])

            uf_dropdown = tk.OptionMenu(root, self.__uf_selected, *uf)
            uf_dropdown.grid(row=4, column=1, padx=10, pady=10)

            nome_fantasia_label = tk.Label(root, text="Nome fantasia:")
            nome_fantasia_label.grid(row=0, column=2, padx=10, pady=10)

            self.__nome_fantasia_input = tk.Entry(root)
            self.__nome_fantasia_input.grid(row=0, column=3, padx=10, pady=10)

            cnpj_label = tk.Label(root, text="CNPJ:")
            cnpj_label.grid(row=1, column=2, padx=10, pady=10)

            cnpj_label = tk.Label(root, text=produtor.cnpj)
            cnpj_label.grid(row=1, column=3, padx=10, pady=10)

            tipo_certificacao_label = tk.Label(root, text="Certificação:")
            tipo_certificacao_label.grid(row=2, column=2, padx=10, pady=10)

            tipo_certificacao = [tipo_certificacao.value for tipo_certificacao in TipoCertificacaoEnum]
            self.__tipo_certificacao_selected = tk.StringVar()
            self.__tipo_certificacao_selected.set(tipo_certificacao[0])

            tipo_certificacao_dropdown = tk.OptionMenu(root, self.__tipo_certificacao_selected, *tipo_certificacao)
            tipo_certificacao_dropdown.grid(row=2, column=3, padx=10, pady=10)

            logradouro_label = tk.Label(root, text="Logradouro:")
            logradouro_label.grid(row=3, column=2, padx=10, pady=10)

            self.__logradouro_input = tk.Entry(root)
            self.__logradouro_input.grid(row=3, column=3, padx=10, pady=10)

            numero_logradouro_label = tk.Label(root, text="Número:")
            numero_logradouro_label.grid(row=4, column=2, padx=10, pady=10)

            self.__numero_logradouro_input = tk.Entry(root)
            self.__numero_logradouro_input.grid(row=4, column=3, padx=10, pady=10)

            tipo_chave_pix_label = tk.Label(root, text="Tipo de chave pix:")
            tipo_chave_pix_label.grid(row=5, column=0, padx=10, pady=10)

            tipo_chave_pix = [tipo_chave_pix.value for tipo_chave_pix in TipoChavePixEnum]
            self.__tipo_chave_pix_selected = tk.StringVar()
            self.__tipo_chave_pix_selected.set(tipo_chave_pix[0])

            tipo_chave_pix_dropdown = tk.OptionMenu(root, self.__tipo_chave_pix_selected, *tipo_chave_pix)
            tipo_chave_pix_dropdown.grid(row=5, column=1, padx=10, pady=10)

            chave_pix_label = tk.Label(root, text="Chave pix:")
            chave_pix_label.grid(row=5, column=2, padx=10, pady=10)

            self.__chave_pix_input = tk.Entry(root)
            self.__chave_pix_input.grid(row=5, column=3, padx=10, pady=10)

            button_signup = tk.Button(root, text="Atualizar informações", command=self.alterar_produtor)
            button_signup.grid(row=6, column=0, columnspan=2, pady=10)

            root.mainloop()
        except KeyError:
            messagebox.showerror("Erro", "CPF não encontrado")
