import tkinter as tk

from tkinter import messagebox

from src.model.enum.tipo_certificacao_enum import TipoCertificacaoEnum
from src.model.enum.tipo_chave_pix_enum import TipoChavePixEnum
from src.model.enum.uf_enum import UfEnum
from src.module.produtor.controller.produtor_controller import ProdutorController


class ProdutorCadastroView:
    def __init__(self):
        self.__produtor_controller = ProdutorController()
        self.__nome_input = None
        self.__cpf_input = None
        self.__senha_input = None
        self.__telefone_input = None
        self.__municipio_input = None
        self.__uf_selected = None
        self.__nome_fantasia_input = None
        self.__cnpj_input = None
        self.__tipo_certificacao_selected = None
        self.__logradouro_input = None
        self.__numero_logradouro_input = None
        self.__tipo_chave_pix_selected = None
        self.__chave_pix_input = None
        self.cadastro_view()

    def cadastrar_produtor(self):
        nome = self.__nome_input.get()
        cpf = self.__cpf_input.get()
        senha = self.__senha_input.get()
        telefone = self.__telefone_input.get()
        municipio = self.__municipio_input.get()
        uf = self.__uf_selected.get()
        nome_fantasia = self.__nome_fantasia_input.get()
        cnpj = self.__cnpj_input.get()
        tipo_certificacao = self.__tipo_certificacao_selected.get()
        logradouro = self.__logradouro_input.get()
        numero_logradouro = self.__numero_logradouro_input.get()
        tipo_chave_pix = self.__tipo_chave_pix_selected.get()
        chave_pix = self.__chave_pix_input.get()

        if nome and cpf and senha:
            try:
                self.__produtor_controller.cadastrar_produtor(nome,
                                                              cpf,
                                                              senha,
                                                              telefone,
                                                              municipio,
                                                              uf,
                                                              nome_fantasia,
                                                              cnpj,
                                                              tipo_certificacao,
                                                              logradouro,
                                                              numero_logradouro,
                                                              tipo_chave_pix,
                                                              chave_pix)
                messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso")
            except KeyError:
                messagebox.showerror("Erro", "CPF já cadastrado")
        else:
            messagebox.showerror("Erro", "Campos obrigatórios não preenchidos")

    def cadastro_view(self):
        root = tk.Tk()
        root.title("Cadastro de produtor")

        nome_label = tk.Label(root, text="Nome:")
        nome_label.grid(row=0, column=0, padx=10, pady=10)

        self.__nome_input = tk.Entry(root)
        self.__nome_input.grid(row=0, column=1, padx=10, pady=10)

        cpf_label = tk.Label(root, text="CPF:")
        cpf_label.grid(row=1, column=0, padx=10, pady=10)

        self.__cpf_input = tk.Entry(root)
        self.__cpf_input.grid(row=1, column=1, padx=10, pady=10)

        senha_label = tk.Label(root, text="Senha:")
        senha_label.grid(row=2, column=0, padx=10, pady=10)

        self.__senha_input = tk.Entry(root, show="*")
        self.__senha_input.grid(row=2, column=1, padx=10, pady=10)

        telefone_label = tk.Label(root, text="Telefone:")
        telefone_label.grid(row=3, column=0, padx=10, pady=10)

        self.__telefone_input = tk.Entry(root)
        self.__telefone_input.grid(row=3, column=1, padx=10, pady=10)

        municipio_label = tk.Label(root, text="Município:")
        municipio_label.grid(row=4, column=0, padx=10, pady=10)

        self.__municipio_input = tk.Entry(root)
        self.__municipio_input.grid(row=4, column=1, padx=10, pady=10)

        uf_label = tk.Label(root, text="UF:")
        uf_label.grid(row=5, column=0, padx=10, pady=10)

        uf = [uf.value for uf in UfEnum]
        self.__uf_selected = tk.StringVar()
        self.__uf_selected.set(uf[0])

        uf_dropdown = tk.OptionMenu(root, self.__uf_selected, *uf)
        uf_dropdown.grid(row=5, column=1, padx=10, pady=10)

        nome_fantasia_label = tk.Label(root, text="Nome fantasia:")
        nome_fantasia_label.grid(row=0, column=2, padx=10, pady=10)

        self.__nome_fantasia_input = tk.Entry(root)
        self.__nome_fantasia_input.grid(row=0, column=3, padx=10, pady=10)

        cnpj_label = tk.Label(root, text="CNPJ:")
        cnpj_label.grid(row=1, column=2, padx=10, pady=10)

        self.__cnpj_input = tk.Entry(root)
        self.__cnpj_input.grid(row=1, column=3, padx=10, pady=10)

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
        tipo_chave_pix_label.grid(row=5, column=2, padx=10, pady=10)

        tipo_chave_pix = [tipo_chave_pix.value for tipo_chave_pix in TipoChavePixEnum]
        self.__tipo_chave_pix_selected = tk.StringVar()
        self.__tipo_chave_pix_selected.set(tipo_chave_pix[0])

        tipo_chave_pix_dropdown = tk.OptionMenu(root, self.__tipo_chave_pix_selected, *tipo_chave_pix)
        tipo_chave_pix_dropdown.grid(row=5, column=3, padx=10, pady=10)

        chave_pix_label = tk.Label(root, text="Chave pix:")
        chave_pix_label.grid(row=6, column=0, padx=10, pady=10)

        self.__chave_pix_input = tk.Entry(root)
        self.__chave_pix_input.grid(row=6, column=1, columnspan=3)

        button_signup = tk.Button(root, text="Cadastrar", command=self.cadastrar_produtor)
        button_signup.grid(row=7, column=0, columnspan=4, pady=10)

        root.mainloop()
