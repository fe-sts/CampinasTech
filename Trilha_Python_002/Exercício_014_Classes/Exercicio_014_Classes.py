'''
14. Fazer um sistema de biblioteca (Deve imprimir uma lista com 10 livros, pedir o nome do solicitante do 
empréstimo, pedir para selecionar um livro e imprimir o livro selecionado)
'''
from livros import Livros
nome = str(input('Qual o seu nome? ').strip())
print('Escolha o livro que quer emprestar: ')

livros = Livros()
print(livros)
escolha = int(input('Digite o número do livro escolhido: '))
emprestado = Livros.livro_escolhido(escolha)
#escolha = (Livros.livro_escolhido(int(input(f'{nome}, digite número do livro escolhido: ')))) #retorna para o print a resposta do usuário
print(f'Parabéns {nome}, o livro "{emprestado}" é muito bom!')