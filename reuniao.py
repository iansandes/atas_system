from funcionario import Funcionario
from externo import ParticipanteExterno
from ata import Ata
import sqlite3
from sugestao import Sugestao


class Reuniao:
    """docstring for ParticipandeReuniao"""
    def __init__(self):
        self.func = Funcionario()
        self.ext = ParticipanteExterno()
        self.part = Ata()
        self.sugest = Sugestao()
        
    def incluirParticipante(self):
        tipo_participante = int(input('É um funcionário [1] ou participante externo [2]? '))
        if tipo_participante == 1:
            con = sqlite3.connect('banco_funcionarios.db')
            cur = con.cursor()
            matricula = input('Informe a matrícula do funcionário: ')
            cur.execute("SELECT * FROM funcionarios WHERE matricula = '{}'".format(matricula))
            funcionario = cur.fetchall()
            self.part.participarAta(funcionario)
        elif tipo_participante == 2:
            con = sqlite3.connect('participante_externo.db')
            cur = con.cursor()
            nome = input('Informe o nome do participante externo: ')
            cur.execute("SELECT * FROM externo WHERE name = '{}'".format(nome))   
            externo = cur.fetchall()
            self.part.participarAta(externo)  

    def adicionarSugestao(self):
        sugestao = input('Existe alguma sugestão [S/N]?')
        if sugestao.upper() == 'S':
            nome = input('Insira o nome da pessoa que sugeriu: ')
            self.sugest.emitirSugestao()
