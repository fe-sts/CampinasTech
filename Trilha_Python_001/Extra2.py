nome_user = input("OlÃ¡! Por favor insira o nome do usuÃ¡rio por favor.\n") #Pergunte pelo nome do usuÃ¡rio
lista_agendamentos =[] #Cria uma lista de agendamentos vazia para comeÃ§ar o programa
lista_opcoes = ["","1 -) Listar Agendamentos", "2 -) Excluir um agendamento", "3 -) Inserir um Agendamento", "4 -) Sair"] #Cria uma lista de opÃ§Ãµes para o usuÃ¡rio ver na tela
while True: #Loop infinito para manter o programa e as variÃ¡veis vivos
    print(f"OlÃ¡ {nome_user}, selecione uma das opÃ§Ãµes abaixo:") #DÃ¡ as boas vindas ao usuÃ¡rio
    for opcao in lista_opcoes: #Lista as opÃ§Ãµes na tela do usuÃ¡rio
        print(opcao) #Imprime as opÃ§Ãµes
    opcao_selecionada = int(input("")) #Aguarda para receber um valor do usuÃ¡rio (Pode ter um tratamento aqui)
    if opcao_selecionada == 1: #Se a opÃ§Ã£o selecionada for a 1, entÃ£o liste os agendamentos existentes
        print(lista_agendamentos) #Imprima os agendamentos existentes na lista
        
    elif opcao_selecionada == 2: #Se a opÃ§Ã£o selecionada for a 2, entÃ£o prepare para excluir um agendamento
        while True: #Loop infinito para navegar nas "Telas" de exclusÃ£o
            indice = 0 #Ãndice para controlar as opÃ§Ãµes de exclusÃ£o
            for item in lista_agendamentos: #Lista dos agendamentos
                print(f"{indice} - {item}") #Imprime os Agendamentos com os seus respectivos Ã­ndices
                indice += 1 #Incrementa os Ã­ndices
            print(f"Selecione {indice} para sair...") #DÃ¡ a opÃ§Ã£o para o usuÃ¡rio sair desta tela de exclusÃ£o
            indice_selecionado = input("Qual desses items vocÃª deseja excluir? (Selecione um nÃºmero) \n") #Pergunte para o usuÃ¡rio qual Ã© o item que ele deseja excluir, dado o Ã­ndice
            if indice_selecionado.isnumeric(): #Verifica se o Ã­ndice Ã© numÃ©rico
                indice_selecionado_convertido = int(indice_selecionado) #caso seja um Ã­ndice numÃ©rico, entÃ£o converta para inteiro
                if indice_selecionado_convertido in range(0, indice): #Verifica se o nÃºmero convertido estÃ¡ no range da lista
                    print("Apagando...") #Avise ao usuÃ¡rio que estÃ¡ apagando
                    item_selecionado = lista_agendamentos.pop(indice_selecionado_convertido) #Apague o item (Dado o seu Ã­ndice) e extraia o item excluÃ­do
                    print(f"Seu item {item_selecionado} foi removido!") #Avise para o usuÃ¡rio que o item foi excluÃ­do
                    break #Saia da tela fazendo o comando break para sair do loop
                elif indice_selecionado_convertido == indice: #Se o usuÃ¡rio selecionou o Ãºltimo indice (ou indice extra), entÃ£o saia da tela de excluir
                    break #Saia da tela fazendo o comando break para sair do loop
                else: #SenÃ£o, se o usuÃ¡rio digitou algum Ã­ndice numÃ©rico que nÃ£o exista, entÃ£o mostre que nÃ£o hÃ¡ essa opÃ§Ã£o
                    print("NÃ£o existe essa opÃ§Ã£o!") #Mostre para o usuÃ¡rio que nÃ£o hÃ¡ essa opÃ§Ã£o
            else: #SenÃ£o, se o usuÃ¡rio digitou algo nÃ£o numÃ©rico, entÃ£o avise que a opÃ§Ã£o estÃ¡ incorreta
                print("OpÃ§Ã£o incorreta ou inexistente!") #Mostre para o usuÃ¡rio que essa opÃ§Ã£o nÃ£o existe

    elif opcao_selecionada ==3: #Se o usuÃ¡rio optou por inserir entÃ£o, vamos inserir um novo registro
        nome_cliente = input("Insira o nome do cliente\n") #Campo para inserir o nome do cliente no dicionÃ¡rio
        veiculo_cliente = input("Insira o veÃ­culo do cliente\n") #Campo para inserir o veÃ­culo do cliente no dicionÃ¡rio
        dicionario_veiculo = {"nome_cliente":nome_cliente,"veiculo_cliente":veiculo_cliente} #Criando um dicionÃ¡rio com os dados acima
        lista_agendamentos.append(dicionario_veiculo) #Inserindo o dicionÃ¡rio na lista (Escopo Global)
        print("Cliente inserido") #Avise para o usuÃ¡rio que o agendamento foi inserido
    elif opcao_selecionada == 4: #Se o usuÃ¡rio selecionar a opÃ§Ã£o 4, entÃ£o saia do sistema
        print("VocÃª saiu do sistema!") #Avise para o usuÃ¡rio que ele saiu do sistema
        break #Saia do sistema fazendo o comando break para sair do loop infinito
    elif opcao_selecionada not in(1,2,3,4): #Se o usuÃ¡rio nÃ£o selecionou nenhuma das opÃ§Ãµes existentes entÃ£o avise que nÃ£o existe a opÃ§Ã£o
        print("OpÃ§Ã£o errada ou inexistente!") #Mostre para o usuÃ¡rio que a opÃ§Ã£o nÃ£o existe