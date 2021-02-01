lista_frutas = ['Abacate','Abacaxi','Abiu','Abricó','Abrunho','Açaí','Acerola','Akee','Alfarroba','Ameixa','Amêndoa','Amora','Ananás','Anona','Araçá','Arando','Araticum','Ata','Atemoia','Avelã']
class Frutas:
    def frutas():
        for cont in range(len(lista_frutas)):
            print('[{}] {}'.format(cont, lista_frutas[cont - 1]))
    def pedido(nome, escolha):
        print('Solicitante: {}\nFruta escolhida: {}'.format(nome, lista_frutas[escolha - 1]))