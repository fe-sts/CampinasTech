'''
13. Fazer um cadastro de viagem (Deve pedir o nome do viajante, dar as opções de destino e imprimir a 
selecionada)
'''
lista_destinos = ['Tokyo', 'Budapeste', 'Fortaleza', 'Hanói', 'Bangkok']
print('*****Cadstro de Viagem*****')
nome = str(input('Qual o seu nome? ').strip())
print('Olá {}! Para onde gostaria de viajar?'.format(nome))
print('[1] Tokyo\n[2] Budapeste\n[3] Fortaleza\n[4] Hanói\n[5] Bangkok\n')
destino = int(input('Escolha seu destino pelo número: ').strip())

print('Parabéns pela escolha! Tenha uma boa viagem para {}'.format(lista_destinos[destino - 1]))

'''
14. Fazer um sistema de biblioteca (Deve imprimir uma lista com 10 livros, pedir o nome do solicitante do empréstimo, pedir para selecionar um livro e imprimir o livro selecionado)
15. Fazer um sistema de Feira Livre(Deve imprimir uma lista com as frutas e pedir para o solicitante colocar o nome e selecionar a fruta e depois deve imprimir o nome do solicitante e a fruta)
16. Fazer um sistema de Agenda de contatos (Deve criar um dicionário com Nome, Telefone e Endereço, Imprimir os dados do dicionário, ser capaz de inserir e excluir um contato)
17. Fazer um sistema de Agenda de revisão do Carro (Deve pedir o nome do carro, ano e modelo, nome do proprietário, data e hora da revisão. Depois deve guardar os dados em um dicionário e mostrar a lista de dicionários (agendamentos) na tela)
18. Fazer um sistema de compras (Deve mostrar um dicionário com os objetos (Nome, Preço e Cor), pedir o nome do usuário e fazer com o que o usuário selecione um objeto e imprimir a compra na tela)
'''
