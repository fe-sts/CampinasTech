#Lista criada de forma Global, assim pode ser chamada para qlqer uma das Funções
lista_livros = ['Harry Potter e a Pedra Filosofal', 
'Harry Potter e a Câmara Secreta', 
'Harry Potter e o Prisioneiro de Azkaban', 
'Harry Potter e o Cálice de Fogo', 
'Harry Potter e a Ordem da Fênix', 'Harry Potter e o Enigma do Príncipe', 
'Harry Potter e as Relíquias da Morte', 
'Contos Inacabados', 
'O Hobbit', 
'O Senhor dos Anéis']

class Livros:
    def __init__(self):
        indice = 0 
        for item in lista_livros: #Lista dos livros
            print(f"{indice + 1} - {item}") #Imprime os livros com os i­ndices
            indice += 1 #Incrementa os indices

    def livro_escolhido(escolha):
        return lista_livros[escolha - 1]
        #print(lista_livros[escolha - 1])
        


