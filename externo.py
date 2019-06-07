import sqlite3

class ParticipanteExterno:

    con = sqlite3.connect('participante_externo.db')
    cur = con.cursor()
    try: 
        sql = """
        CREATE TABLE externo(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                empresa TEXT NOT NULL,
                                email TEXT NOT NULL) """

        cur.execute(sql)
        con.commit()
        con.close()
    except:
        con.close()

    """docstring for PaticianpteExteno"""
    def __init__(self):
        self.nome = ""
        self.empresa = ""
        self.email = ""

    def incluir(self):
        self.nome = input('Nome: ')
        self.empresa = input('Empresa: ')
        self.email = input('Email: ')

        con = sqlite3.connect('participante_externo.db')
        cur = con.cursor()
        sql = """ INSERT INTO externo(name, empresa, email)
                  VALUES ('{}', '{}', '{}') """.format(self.nome, self.empresa,
                         self.email)
        cur.execute(sql)
        con.commit()
        con.close()
  
