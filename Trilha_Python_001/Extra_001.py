#2 dimensões (2 loops para varrer)
matriz = [["espaço1","espaço2"]
         ,["espaço3","espaço4"]
         ,["espaço5","espaço6"]]

busca = "espaço2" #valor a ser buscado
i = 0 #contador de linha
j = 0 #contador de coluna
isencontrado = False #Flag para verificar se o dado foi encontrado
for linha in matriz: #varre a linha da Matriz
    for coluna in linha: #varre a coluna da linha da Matriz
        if(coluna == busca): #Compara para fazer a busca
            print(f"encontrou o {coluna} na linha {i} e na coluna {j}")
            isencontrado = True
            break
        j += 1
    if isencontrado:
        break
    i += 1
    j = 0 #reset de coluna

if isencontrado == False:
    print("Dado não encontrado")
