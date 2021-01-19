'''
15. Fazer um sistema de Feira Livre(Deve imprimir uma lista com as frutas e pedir para o solicitante 
colocar o nome e selecionar a fruta e depois deve imprimir o nome do solicitante e a fruta)
'''
lista_frutas = ['Abacate','Abacaxi','Abiu','Abricó','Abrunho','Açaí','Acerola','Akee','Alfarroba','Ameixa','Amêndoa','Amora','Ananás','Anona','Araçá','Arando','Araticum','Ata','Atemoia','Avelã']

print('***** Feira Livre Virtual *****')
nome = str(input('Digite seu nome: ').strip())
print('Veja abaixo a lista de frutas: ')

for cont in range(len(lista_frutas)):
    print('[{}] {}'.format(cont, lista_frutas[cont - 1]))

fruta = int(input('Insira o número da fruta escolhida: ').strip())

print('Solicitante: {}\nFruta escolhida: {}'.format(nome, lista_frutas[fruta - 1]))

