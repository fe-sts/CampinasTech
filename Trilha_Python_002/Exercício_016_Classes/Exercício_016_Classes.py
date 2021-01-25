'''
1. Fazer um sistema de Agenda de contatos (Deve criar um dicionário com Nome, Telefone e Endereço, Imprimir os dados 
da classe, ser capaz de inserir e excluir um contato) - OBS: Tem que ser orientado a objeto.

- No mínimo usar Contato como classe!
- Ao inves de usar dicionario, usar classes
- Se conseguir usar herança, melhor ainda
-Se criar um classe Pessoa e Contato (aqui pode-se trabalhar com herança)
'''
from Exclusao import Exclusao
from Contato import Contato


print('\033[1;31;47m***** Agenda de Contatos *****\033[m')
nome_usuario = str(input('Entre com o seu nome: ').strip())
print('\nOlá {}! Escolha uma das opções abaixo: '.format(nome_usuario))

lista_agenda_opcoes = ["","Listar Contatos", "Inserir um Contato", "Excluir um Contato", "Sair da Agenda"]
lista_contatos = []
escolha = 0
excluido = []
cont_listar = 0
cont_exclui = 0


while escolha !=4:
    for cont in range(1, len(lista_agenda_opcoes)):
        print('[{}] {}'.format(cont, lista_agenda_opcoes[cont]))
    escolha = int(input('--> ').strip())

    if escolha == 1: #LISTAR CONTATOS
        if not lista_contatos:
            print("Agenda vazia!")
        else:
            print('\033[1;33mSua lista de contatos é a seguinte: \033[m')
            for contato in lista_contatos:
                print("[{}] Nome: {}\nTelefone: {}\nEndereço: {}".format(cont_listar + 1, contato.nome, contato.telefone, contato.endereco))
                cont_listar += 1
            print('\nEscolha uma nova opção: ')
            cont_listar = 0 #RESETA CONTADOR

    elif escolha == 2: # ADICIONAR CONTATO
        
        nome = str(input('Digite o nome do contato: ').strip())
        telefone = int(input('Digite telefone: ').strip())
        endereco = str(input('Digite endereço: ').strip())
        contato = Contato(nome, telefone, endereco) #INSTÂNCIA  Contato
        lista_contatos.append(contato)

    elif escolha == 3: #EXCLUIR CONTATO
        if not lista_contatos:
            print('Lista vazia! Não tem o que excluir!')
        else:
            for contato in lista_contatos:
                print("[{}] Nome: {}\nTelefone: {}\nEndereço: {}".format(cont_exclui + 1, contato.nome, contato.telefone, contato.endereco))
                cont_exclui += 1
            escolha_exclusao = int(input('\nEscolha o número do contato que quer excluir: ').strip())
            e = Exclusao(escolha_exclusao, lista_contatos) # INSTÂNCIA Exclusão
            print(e) #Usando Classe (em outro arquivo)
            print(lista_contatos)
            cont_exclui = 0 #RESETA CONTADOR

    elif escolha == 4:
        print("Agenda finalizada!")

    elif escolha not in (1, 2, 3, 4):
        print('Opção errada! Escolha uma opção válida!')