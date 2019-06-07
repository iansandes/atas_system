from datetime import date
import sqlite3


class Ata(object):

    """docstring for Ata"""
    def __init__(self):
        self.titulo = ""
        self.dataEmissao = date.today()
        self.inicio = ""
        self.termino = ""
        self.pauta = ""
        self.descricao = ""
        self.palavrasChaves = []
        self.tipo = ""
        self.status = ""
        self.funcionario = ""
        self.participantes = []


    def emitirAta(self):
        if len(self.participantes) >= 2:
            con = sqlite3.connect('banco_funcionarios.db')
            cur = con.cursor()
            matricula = input("Insira a matrícula do funcionário que irá emitir a ata: ")
            cur.execute("SELECT name FROM funcionarios WHERE matricula = '{}'".format(matricula))
            funcionario = cur.fetchall()
            
            self.titulo = input('Título da ata: ')
            self.inicio = input('Horário de início [hh:mm]: ')
            self.termino = input('Horário de término [hh:mm]: ')
            self.pauta = input('Pauta da reunião: ')
            self.descricao = input('Descrição da reunião: ')
            for x in range(0,5):
                self.palavrasChaves.append(input('Palavra-chave: '))
                ask = input('Deseja adicionar mais uma palavra chave [S/N]? ')
                if ask.upper() == 'S':
                    pass
                else:
                    if len(self.palavrasChaves) < 2:
                        pass
                    else:
                        break
            self.tipo = input('Tipo: ')
            aprovacao = input('A ata foi aprovada [S/N]? ')
            if aprovacao.upper() == 'S':
                self.status = "Emitida"
                self.funcionario = funcionario
            else:
                print('Ata não aprovada!')
            
        else:
            print('Impossível emitir ata!')
            
    def participarAta(self, participante):
        if len(self.participantes) < 10:
            self.participantes.append(participante)
            print(self.participantes)
        else:
            print("Reunião lotada") 

    def exibirAta(self):
        print('Título: {}'.format(self.titulo))
        print('Data de emissão: {}'.format(self.dataEmissao))
        print('Hora de início: {}'.format(self.inicio)) 
        print('Hora de término: {}'.format(self.termino))
        print('Pauta: {}'.format(self.pauta))
        print('Descrição: {}'.format(self.descricao))
        print('Palavras-chaves: {}'.format(self.palavrasChaves))
        print('Tipo: {}'.format(self.tipo))
        print('Status: {}'.format(self.status))
        print('Funcionário que emitiu a ata: {}'.format(self.funcionario))

    def salvarAta(self):
        ...

    def atualizarAta(self):
        ...
