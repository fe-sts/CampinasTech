class Destinos:
    def __init__(self, indice_destino):
        self.indice_destino = indice_destino
        self.varsai = ''
        lista_destinos = ['Tokyo', 'Budapeste', 'Fortaleza', 'Hanói', 'Bangkok']

        if indice_destino == 0:
            for cont in range (len(lista_destinos)):
                print('[{}] {}'.format(cont + 1, lista_destinos[cont]))
            #self.indice_destino = int(input('Escolha seu destino pelo número: ').strip())
        else:
            self.varsai = lista_destinos[indice_destino - 1]