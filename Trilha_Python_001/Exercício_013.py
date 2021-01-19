'''
13. Fazer um cadastro de viagem (Deve pedir o nome do viajante, dar as opções de destino e imprimir a 
selecionada)
'''
lista_destinos = ['Tokyo', 'Budapeste', 'Fortaleza', 'Hanói', 'Bangkok']
print('*****Cadastro de Viagem*****')
nome = str(input('Qual o seu nome? ').strip())
print('Olá {}! Para onde gostaria de viajar?'.format(nome))
print('[1] Tokyo\n[2] Budapeste\n[3] Fortaleza\n[4] Hanói\n[5] Bangkok\n')
destino = int(input('Escolha seu destino pelo número: ').strip())

print('Parabéns pela escolha! Tenha uma boa viagem para {}'.format(lista_destinos[destino - 1]))