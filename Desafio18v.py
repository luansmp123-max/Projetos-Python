# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno
# e tangente desse ângulo.
# a   30º      45º      60º
# sen 1/2      sqrt2/2  sqrt3/3
# cos sqrt3/2  sqrt2/2  1/2
# tg  sqrt3/3  1        sqrt3
# Dica: biblioteca específica
from math import sin, cos, tan, radians
a = float(input('Digite o valor do ângulo para ver seu sen, cos e tg: '))
sen = sin(radians(a))
cos = cos(radians(a))
tg = tan(radians(a))
print('Sen: {:.2f}\nCos {:.2f}\nTg {:.2f}'.format(sen, cos, tg))