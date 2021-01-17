'''
7. Fazer um sistema de Loteria (Deve pedir o nome do usuário, pedir um número e comparar com um conjunto 
aleatório de número (de 0 a 100) e dizer se o usuário advinhou)
'''
num_usuario = []
print('-='*30)
nome = str(input('Digite seu nome: '))
print('-='*30)
print('Digite 6 números entre 0 a 100')

for cont1 in range(1,7):
    num = int(input(f'Digite o {cont1}º número: ')) #Utiliza o contador 'i' para numerar o escreva
    if num > 100:
        print(f'Entre com número de 0 a 100. Você digitou {num}') #Tratamento para caso digitar um numero maior que 100
    elif num <=100:
        num_usuario.append(num) #Insere o numero digitado no final da lista
print('*'*30)


#Computador vai sortear 6 numeros aleatórios
import random
num_computador = []
acertos = []
num_computador = random.sample((range(0, 100)), 6) #sample seleciona dentro do range de 0 a 100, 6 numeros sem repetição
print('Os números sorteados pelo computador foram: {}'.format(num_computador))
print('*'*30)


#Compara Numeros inseridos com os Números sorteados pelo computador
for cont2 in range (0, (len(num_computador))):
    #print(num_computador[cont2])
    if num_computador[cont2] in num_usuario: #Se o nº da Lista do computador estiver contida na Lista do Usuário
        #print(num_computador[cont3]) 
        acertos.append(num_computador[cont2])#Vai inserir número na Lista de Acertos
    #else:
    #    print(f'NÃO ESTÁ {num_computador[cont3]}')

#Se acertou todos os números, escreve Parabéns
if (len(acertos) == 6):
    print('Parabéns você acertou todos os números!')
    print('Os numeros acertados por {} foram: {}'.format(nome, acertos)) #Informa os numeros acertados
else:
    print('Os numeros acertados por {} foram: {}'.format(nome, acertos)) #Senão, informa os numeros acertados
print('*'*30)