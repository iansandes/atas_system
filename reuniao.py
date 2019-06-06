from funcionario import Funcionario
from externo import PaticipanteExterno


class ParticipanteReuniao:
    """docstring for ParticipandeReuniao"""
    def __init__(self):
        self.func = Funcionario()
        self.ext = ParticipanteExterno()

    def incluirParticipante(self):
        ...

    def selecionarParticipante(self):
        ...
