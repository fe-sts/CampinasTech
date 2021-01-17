'''
8. Elabore um algoritmo em Python que receba um número inteiro e escreva na tela o número fornecido, 
o antecessor desse número e o sucessor desse número;
'''
print('*'*30)
num = int(input('Digite um número inteiro: ').strip())
print('*'*30)
print('O número inserido foi: {}.\nO número antecessor é: {}.\nO número sucessor é: {}'.format(num, num - 1, num + 1))
print('*'*30)