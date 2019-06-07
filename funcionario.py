import sqlite3

class Funcionario:

    """docstring for Funcionario"""

    con = sqlite3.connect('banco_funcionarios.db')
    cur = con.cursor()
    try: 
        sql = """
        CREATE TABLE funcionarios(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                matricula TEXT NOT NULL,
                                sexo TEXT NOT NULL,
                                nascimento TEXT NOT NULL,
                                email TEXT NOT NULL) """

        cur.execute(sql)
        con.commit()
    except:
        con.close()

    def __init__(self):
        self.nome = ""
        self.matricula = 0
        self.sexo = ""
        self.nascimento = ""
        self.email = ""

    def incluir(self):
        self.nome = input('Nome: ')
        self.matricula = input('Matricula: ')
        self.sexo = input('Sexo [M/F]: ')
        self.nascimento = input('Data de nascimento [dd/mm/aaaa]: ')
        self.email = input('Email: ')

        con = sqlite3.connect('banco_funcionarios.db')
        cur = con.cursor()
        sql = """ INSERT INTO funcionarios(name, matricula, sexo, nascimento, email)
                  VALUES ('{}', '{}', '{}', '{}', '{}') """.format(self.nome, self.matricula,
                  self.sexo, self.nascimento, self.email)
        cur.execute(sql)
        con.commit()
        con.close()
