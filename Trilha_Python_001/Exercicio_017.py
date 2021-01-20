'''
17. Fazer um sistema de Agenda de revisão do Carro (Deve pedir o nome do carro, ano e modelo, 
nome do proprietário, data e hora da revisão. Depois deve guardar os dados em um dicionário e 
mostrar a lista de dicionários (agendamentos) na tela)
'''
print('\033[1;32;40m***** Agenda Revisão de Carros *****\033[m')
escolha = 0
agenda_carro = []
lista_agenda_opcoes = ["","Listar Agendamentos", "Inserir Agendamento", "Sair da Agenda"]
while escolha != 4:
    print('\033[1;33;40mEscolha uma das opões no menu abaixo: \033[m')
    for cont in range(1, len(lista_agenda_opcoes)):
        print('\033[1;32;40m[{}] {}\033[m'.format(cont, lista_agenda_opcoes[cont]))
    escolha = int(input('--> '))

    if escolha == 1:
        if not agenda_carro:
            print('Agenda está vazia!')
        else:
            for cont2 in range (len(agenda_carro)):
                print('[{}] {}'.format(cont2 + 1, agenda_carro[cont2]))

    elif escolha == 2:
        nome_carro = str(input('Digite o nome do carro: ').strip())
        ano = int(input('Digite o ano de fabricação do carro: ').strip())
        modelo = str(input('Digite o modelo do carro: ').strip())
        nome_proprietario = str(input('Digite o nome do Proprietario: ').strip())   
        data = str(input('Digite a data da revisão (DD/MM/AAAA): ').strip())
        hora = str(input('Digite a hora do agendamento (HH:MM) Exemplo: 15:20: ').strip())
        lista_dados = {"Nome do Carro: ": nome_carro, "Ano: ": ano, "Modelo do carro: ": modelo, "Nome do Proprietario: ": nome_proprietario, "Data: ": data, "Hora do Agendamento: ": hora}
        agenda_carro.append(lista_dados)

    elif escolha == 3:
        print('Agenda fechada!')
        escolha = 4

    elif escolha not in (1, 2, 3):
        print('Escolha uma opção válida!')