class Exclusao:
    def __init__(self, escolha_exclusao, lista_contatos):
        self.escolha_exclusao = escolha_exclusao
        self.lista_contatos = lista_contatos
        lista_contatos.pop(escolha_exclusao - 1)