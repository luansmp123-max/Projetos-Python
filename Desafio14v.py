# Escreva um programa que converta uma temperatura digitada em ºC para ºF
# ºF>ºC= F=1.8xC+32
c = float(input('Informe a temperatura em Celsius: '))
f = (c*1.8)+32
print('A temperatura em Fahrenheit é: {}.'.format(f))