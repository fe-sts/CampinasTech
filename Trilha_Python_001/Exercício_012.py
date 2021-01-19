'''
12. Elabore um algoritmo em Python que:
a) Primeiro exiba uma mensagem de boas vindas;
b) Pergunte o nome do usuário;
c) Exiba uma mensagem dizendo uma mensagem de olá
seguida pelo nome do usuário seguida por outra mensagem
fazendo um elogio.
'''
print('Bem vindo!')
nome = str(input('Qual o seu nome? ').strip())
print('Olá {}! Você tem um nome muito bonito! Show de bola!\nVou colocar no meu filho!'.format(nome))


