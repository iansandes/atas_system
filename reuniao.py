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
        self.ata = Ata()
        self.sugest = Sugestao()
        
    def incluirParticipante(self):
        while True:
            tipo_participante = int(input('\nÉ um funcionário [1] ou participante externo [2]? '))
            if tipo_participante == 1:
                con = sqlite3.connect('banco_funcionarios.db')
                cur = con.cursor()
                matricula = input('Informe a matrícula do funcionário: ')
                cur.execute("SELECT * FROM funcionarios WHERE matricula = '{}'".format(matricula))
                funcionario = cur.fetchall()
                if funcionario == []:
                    print('Não existe esse funcionário!')
                    break
                else:
                    self.ata.participarAta(funcionario)
            elif tipo_participante == 2:
                con = sqlite3.connect('participante_externo.db')
                cur = con.cursor()
                nome = input('Informe o nome do participante externo: ')
                cur.execute("SELECT * FROM externo WHERE name = '{}'".format(nome))   
                externo = cur.fetchall()
                if externo == []:
                    print('Não existe esse participante externo!')
                    break
                else:
                    self.ata.participarAta(externo)

            sair = input('\nDeseja inserir um novo participante [S/N] ? ')
            if sair.upper() == 'S':
                continue
            else: 
                break


    def adicionarSugestao(self):
        sugestao = input('\nExiste alguma sugestão [S/N]?')
        if sugestao.upper() == 'S':
            nome = input('Insira o nome da pessoa que sugeriu: ')
            self.sugest.emitirSugestao()
