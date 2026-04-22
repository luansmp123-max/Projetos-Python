# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Entre com uma medida em metros: '))
nc = m*100
nmm = m*1000
print('Seu valor em centímetros é {}cm.\nSeu valor em milímetros é {}mm.'.format(nc,nmm))