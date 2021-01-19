'''
11. Fazer uma busca sequencial em uma matriz (Criar uma matriz 10 linhas e 10 colunas e pedir para o usuário 
fazer uma busca)
'''
linhas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
matriz = []
for cont in range (10):
    matriz.append(linhas)
#print(matriz)
#print(len(matriz))
#print(type(matriz))
print(len(linhas))

num = int(input('Busque um número na Matriz.\nDigite um número: '))

cont_linha = 0 
cont_coluna = 0 

for cont in matriz: #varre a linha da Matriz
    for coluna in cont: #varre a coluna da linha da Matriz
        if(coluna == num): #Compara para fazer a busca
            print("encontrou o {} na linha {} e na coluna {}".format(coluna, cont_linha, cont_coluna))
            isencontrado = True
        cont_coluna += 1
    #if isencontrado:
        #break
        #print('Encontrado!')
    cont_linha += 1
    cont_coluna = 0 #reset de coluna
'''
cont1 = 0
cont2 = 0
for linha in matriz:
    for coluna in linha:
        if num == matriz:
            print('Encontrou o item {} na linha {} e na coluna {}'.format(num, ))
        else:
            print('Número não encontrado!')
        cont1 += 1
    cont2 += 1
'''



