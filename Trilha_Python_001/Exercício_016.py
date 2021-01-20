''' 
16. Fazer um sistema de Agenda de contatos (Deve criar um dicionário com Nome, Telefone e Endereço, 
Imprimir os dados do dicionário, ser capaz de inserir e excluir um contato)

usar LIsta de dicionario
'''
print('\033[1;31;47m***** Agenda de Contatos *****\033[m')
nome_usuario = str(input('Entre com o seu nome: ').strip())
print('\nOlá {}! Escolha uma das opções abaixo: '.format(nome_usuario))

lista_agenda_opcoes = ["","Listar Contatos", "Inserir um Contato", "Excluir um Contato", "Sair da Agenda"]
lista_contatos = []
#acao = 0
escolha = 0
excluido = []
while escolha !=4:
    for cont in range(1, len(lista_agenda_opcoes)):
        #print(cont)
        print('[{}] {}'.format(cont, lista_agenda_opcoes[cont]))
    escolha = int(input('--> ').strip())

    if escolha == 1:
        if not lista_contatos:
            print("Agenda vazia!")
        else:
            print('\033[1;33mSua lista de contatos é a seguinte: \033[m')
            for cont in range(len(lista_contatos)):
                print('[{}] {}'.format(cont + 1, lista_contatos[cont]))
            print('\nEscolha uma nova opção: ')

    elif escolha == 2: # ADICIONAR CONTATO
        nome = str(input('Digite o nome do contato: ').strip())
        telefone = int(input('Digite telefone: ').strip())
        endereco = str(input('Digite endereço: ').strip())
        dicionario_dados = {"Nome: ": nome, "Telefone: ": telefone, "Endereço: ": endereco}
        lista_contatos.append(dicionario_dados)
        print('Contato adicionado!')

    elif escolha == 3:
        if not lista_contatos:
            print('Lista vazia! Não tem o que excluir!')
        else:
            for cont2 in range (len(lista_contatos)):
                print('[{}] {}'.format(cont2 + 1, lista_contatos[cont2]))
            escolha_exclusao = int(input('\nEscolha o número do contato que quer excluir: ').strip())
            excluido = lista_contatos.pop(escolha_exclusao - 1)
            print(excluido)
            print('\033[1;33mO contato {} foi excluido\033[m'.format(excluido))
            
    elif escolha == 4:
        print("Agenda finalizada!")

    elif escolha not in (1, 2, 3, 4):
        print('Opção errada! Escolha uma opção válida!')

'''
17. Fazer um sistema de Agenda de revisão do Carro (Deve pedir o nome do carro, ano e modelo, 
nome do proprietário, data e hora da revisão. Depois deve guardar os dados em um dicionário e 
mostrar a lista de dicionários (agendamentos) na tela)

18. Fazer um sistema de compras (Deve mostrar um dicionário com os objetos (Nome, Preço e Cor), 
pedir o nome do usuário e fazer com o que o usuário selecione um objeto e imprimir a compra na tela)
'''