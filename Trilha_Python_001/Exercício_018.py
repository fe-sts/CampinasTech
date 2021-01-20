'''
18. Fazer um sistema de compras (Deve mostrar um dicionário com os objetos (Nome, Preço e Cor), 
pedir o nome do usuário e fazer com o que o usuário selecione um objeto e imprimir a compra na tela)
'''
#              [{'Nome: ': 'werwer', 'Telefone: ': 654, 'Endereço: ': 'wer'}, {'Nome: ': 'ghfgh', 'Telefone: ': 131, 'Endereço: ': '102321'}]
lista_opções = ['[1] Listar produtos', '[2] Itens comprados', '[3] Sair do sistema']
lista_itens = [{"Nome: ": "Apontador", "Preço: ": 6.70, "Cor: ": "Preto"}, {"Nome: ": "Lápis","Preço: ": 2.50,"Cor: ": "Amarelo"},{"Nome: ": "Tesoura","Preço: ": 8.90,"Cor: ": "Branco"},{"Nome: ": "Borracha","Preço: ": 4.90,"Cor: ": "Verde"},{"Nome: ": "Regua","Preço: ": 1.80,"Cor: ": "Azul" }]
lista_comprados = []

print("\033[1;36;40m******* Sistema de Compras ********\033[m\n")
while True:
    print('Escolha uma ação: ')
    for cont in range(len(lista_opções)):
        print('{}'.format(lista_opções[cont]))
    escolha = int(input('-->'))

    if escolha == 1:
        for cont in range(len(lista_itens)):
            print('[{}] {}'.format(cont + 1, lista_itens[cont]))
        produto = int(input('Escolha um produto para compra: '))
        if produto not in range(len(lista_itens) + 1):
            print('Escolha uma opção válida!')
        else:
            lista_comprados.append(lista_itens[produto - 1])

    if escolha == 2:
        if not lista_comprados:
            print('Lista está vazia!')
        else:
            print('\033[1;35;40mLista de produtos comprados: \033[m')
            for cont in range(len(lista_comprados)):
                print('[{}] {}'.format(cont + 1, lista_comprados[cont]))
        
    if escolha == 3:
        print('Sistema fechado!')
        break 

    if escolha not in (1, 2, 3):
        print('Escolha uma opção válida!')