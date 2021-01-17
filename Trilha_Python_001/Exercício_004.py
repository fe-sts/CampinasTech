'''
4. Elabore um algoritmo em Python que leia, calcule e escreva a média aritmética entre quatro números;
'''

soma = 0
nota = 0
qtd_notas = 0
for cont in range(1, 5):
    nota = int(input('Insira a {}ª nota: '.format(cont)).strip())
    soma += nota
    qtd_notas += 1
print('A média aritmética entre as quatro notas é: {}'.format(soma / qtd_notas))