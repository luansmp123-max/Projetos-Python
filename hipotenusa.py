# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
# Dica: módulos // a²=b²+c² // a=sqrt(b²+c²)
from math import hypot
op = float(input('Digite o valor do cateto oposto: '))
ad = float(input('Digite o valor do cateto adjacente: '))
'''hip = (op ** 2 + ad ** 2) ** (1/2)'''
'''from math import sqrt
hip = sqrt(op ** 2 + ad ** 2)'''
hip = hypot(op,ad)
print('O valor da hipotenusa é: {}.'.format(hip))