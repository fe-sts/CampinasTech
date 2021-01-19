'''
14. Fazer um sistema de biblioteca (Deve imprimir uma lista com 10 livros, pedir o nome do solicitante do 
empréstimo, pedir para selecionar um livro e imprimir o livro selecionado)
'''
lista_livros = ['Harry Potter e a Pedra Filosofal', 'Harry Potter e a Câmara Secreta', 'Harry Potter e o Prisioneiro de Azkaban', 'Harry Potter e o Cálice de Fogo', 'Harry Potter e a Ordem da Fênix', 'Harry Potter e o Enigma do Príncipe', 'Harry Potter e as Relíquias da Morte', 'Contos Inacabados', 'O Hobbit', 'O Senhor dos Anéis']
nome = str(input('Qual o seu nome? ').strip())
print('Escolha o livro que quer emprestar: ')
for cont in range(len(lista_livros)):
    print('[{}] {}'.format(cont + 1, lista_livros[cont]))
escolha = int(input('--> ').strip())
print('O livro escolhido foi: {}'.format(lista_livros[escolha]))