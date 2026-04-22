# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m².
l = float(input('Largura da parede em m: '))
a = float(input('Altura da parede em m: '))
aa = l*a
tn = aa/2
print('Área total da parede: {}m²'.format(aa))
print('Para pintar sua parede, levando em consideração que cada litro de tinta pinta 2m²,\n\
vão ser necessários {} litros de tinta.'.format(tn))