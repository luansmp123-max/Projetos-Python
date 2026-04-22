# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela
# a sua porção inteira. E.g.: número: 6.127; porção inteira: 6.
# Dica: math
'''from math import floor
n = float(input('Digite um número Real: '))
print('A porção inteira do número digitado é: {}'.format(floor(n)))'''
'''from math import trunc
n = float(input('Digite um número Real: '))
print('A porção inteira de {} é: {}'.format(n, trunc(n)))'''
n = float(input('Digite um número Real: '))
print('A porção inteira de {} é: {}'.format(n, int(n)))