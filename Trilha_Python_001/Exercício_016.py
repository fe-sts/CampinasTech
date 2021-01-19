''' FALTA TERMINAR!!!
16. Fazer um sistema de Agenda de contatos (Deve criar um dicionário com Nome, Telefone e Endereço, 
Imprimir os dados do dicionário, ser capaz de inserir e excluir um contato)
'''

nome = str(input('Digite seu nome: ').strip())
telefone = int(input('Digite seu telefone: ').strip())
endereco = str(input('Digite seu endereço: ').strip())

dicionario_dados = {"Nome: ": nome, "Telefone: ": telefone, "Endereço: ": endereco}

print(dicionario_dados)

continua = str(input('Deseja inserir mais algum contato? [S/N) ').strip())
if continua in "Ss":
    nome = str(input('Digite seu nome: ').strip())
    telefone = int(input('Digite seu telefone: ').strip())
    endereco = str(input('Digite seu endereço: ').strip())

dicionario_dados = {"Nome: ": nome, "Telefone: ": telefone, "Endereço: ": endereco}

print(dicionario_dados)
'''
17. Fazer um sistema de Agenda de revisão do Carro (Deve pedir o nome do carro, ano e modelo, 
nome do proprietário, data e hora da revisão. Depois deve guardar os dados em um dicionário e 
mostrar a lista de dicionários (agendamentos) na tela)

18. Fazer um sistema de compras (Deve mostrar um dicionário com os objetos (Nome, Preço e Cor), pedir o nome do usuário e fazer com o que o usuário selecione um objeto e imprimir a compra na tela)
'''