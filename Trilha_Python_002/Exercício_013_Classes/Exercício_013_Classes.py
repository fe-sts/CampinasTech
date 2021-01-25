'''
13. Fazer um cadastro de viagem (Deve pedir o nome do viajante, dar as opções de destino e imprimir a 
selecionada)
*Refazer este exercício utilizando Classes.
'''
from Destinos import Destinos

print('*****Cadastro de Viagem*****')
nome = str(input('Qual o seu nome? ').strip())
print('Olá {}! Para onde gostaria de viajar?'.format(nome))
print(Destinos(0))
indice_destino = int(input('Escolha seu destino pelo número: ').strip())
x = Destinos(indice_destino)
print('Parabéns pela escolha! Tenha uma boa viagem para {} !!!'.format(x.varsai))