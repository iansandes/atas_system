from funcionario import Funcionario
from ata import Ata
from reuniao import Reuniao

ian = Funcionario()
ian.incluir()

n = Funcionario()
n.incluir()

reuniao = Reuniao()
reuniao.incluirParticipante()
reuniao.incluirParticipante()

ata = Ata()
ata.emitirAta()