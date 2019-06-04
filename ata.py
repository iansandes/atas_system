from datetime import date


class Ata(object):
    """docstring for Ata"""
    def __init__(self):
        self.titulo = ""
        self.dataEmissao = date.today()
        self.inicio = ""
        self.termino = ""
        self.pauta = ""
        self.descricao = ""
        self.palavrasChaves = ""
        self.tipo = ""
        self.estatus = ""

    def emitirAta(self):
        ...

    def exibirAta(self):
        ...

    def salvarAta(self):
        ...

    def atualizarAta(self):
        ...
