'''
10. Fazer uma busca sequencial em uma lista (Criar uma tupla [0....20] e pedir para o usuário fazer uma busca)
'''
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print(len(tupla))
num = int(input("Digite um número para buscar na na arquivo: ").strip())

if num in tupla:
    print('O número {} consta no arquivo!'.format(num))
else:
    print('O número inserido não consta no arquivo')