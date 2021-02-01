'''
15. Fazer um sistema de Feira Livre(Deve imprimir uma lista com as frutas e pedir para o solicitante 
colocar o nome e selecionar a fruta e depois deve imprimir o nome do solicitante e a fruta)

*Utilizando Classes
'''
from frutas import Frutas

print('***** Feira Livre Virtual *****')
nome = str(input('Digite seu nome: ').strip())
print('Veja abaixo a lista de frutas: ')
Frutas.frutas()
escolha = int(input('Insira o número da fruta escolhida: ').strip())
Frutas.pedido(nome, escolha)
