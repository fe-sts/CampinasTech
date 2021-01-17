'''
5. Algoritmo para calcular a média do aluno (Deve colocar o nome do aluno, colocar 4 notas e 
imprimir sua média)
'''
nota = 0
media = 0
soma_nota = 0
nome = str(input('Digite o nome do Aluno: ').strip())
for cont in range (1, 5):
    nota = float(input('Entre com a {}ª nota: '.format(cont)).strip())
    soma_nota += nota
media = soma_nota / 4
print('A média do aluno {} é {}'.format(nome, media))