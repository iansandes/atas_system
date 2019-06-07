from datetime import date

class Sugestao:
    """docstring for Sugestao"""

    def __init__(self):
        self.id = ""
        self.data = date.today()
        self.descricao = ""

    def emitirSugestao(self):
        self.descricao = input('Insira sua sugestão: ')

    def selecionarSugestao(self):
        ...
