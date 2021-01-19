'''
9. Elabore um algoritmo em Python que calcule a área e o perímetro de um círculo, sabendo que A = πr² e P=2πr.
'''
import math

raio = float(input('Digite o raio do circulo em metros: ').strip())
area = math.pi * (raio ** 2)
print('A area do círculo é {:.2f}'.format(area)) #mostra 2 casas decimais após .

perimetro = 2 * (math.pi * (raio ** 2))
print('O perímetro para este raio é {:.2f}'.format(perimetro))

#perimetro = float(input('Digite o perímetro: ').strip())