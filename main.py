from funcionario import Funcionario
from ata import Ata
from reuniao import Reuniao
from externo import ParticipanteExterno



def menu_reuniao():
    reuniao = Reuniao()
    while True:
        print("--------------------\n"
            "1 - Iniciar Reunião e emitir Ata\n"
            "2 - Exibir Ata\n"
            "3 - Salvar Ata\n"
            '4 - Atualizar Ata\n'
            "5 - Sugestão\n"
            "6 - Sair\n"
            "--------------------")
        opcao = int(input("Escolha o tipo de atendimento a ser usado: "))
        

        if opcao == 1:
            reuniao.incluirParticipante()
            reuniao.ata.emitirAta()
        if opcao == 2:
            reuniao.ata.exibirAta()   
        if opcao == 3:
            reuniao.ata.salvarAta()    
        if opcao == 4:
            reuniao.ata.atualizarAta()
        if opcao == 5:
            reuniao.sugest.adicionarSugestao()
        if opcao == 6:
            menu_principal()
            
        
            


def menu_principal():
    print("\n")
    print(20 * "-=")
    print("       SISTEMA DE ATAS")
    print(20 * "-=")

    print("--------------------\n"
          "1 - Cadastrar Funcionário\n"
          "2 - Cadastrar Participante Externo\n"
          "3 - Reunião\n"
          "--------------------")

    while True:
        atendimento = int(input("Escolha o tipo de atendimento a ser usado: "))
        if atendimento == 1:
            funcionario = Funcionario()
            funcionario.incluir()
        elif atendimento == 2:
           participante_externo = ParticipanteExterno()
           participante_externo.incluir()
        elif atendimento == 3:
            menu_reuniao()
        else:
            print("Opção inválida!\n")



menu_principal()