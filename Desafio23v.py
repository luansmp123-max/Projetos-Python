# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# E.g.: Digite um número: 1834
# unidade: 4 //dezena: 3 //centena: 8 //milhar: 1
# Tentar fazer como str e matematicamente
"""num = int(input('Digite um número entre 0 e 9999: '))
n = str(num)
print('Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}'.format(n[0], n[1], n[2], n[3]))"""
num = int(input('Digite um número entre 0 e 9999: '))
#// = divisão inteira (e.g.: 7/2=3,5.·.3=inteiro.·.7//2=3)
#% = divisão por módulo (e.g.: 12/10=1,2.·.2=módulo.·.12%10=2)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Milhar: {}\n'
      'Centena: {}\n'
      'Dezena: {}\n'
      'Unidade: {}'.format(m, c, d, u))