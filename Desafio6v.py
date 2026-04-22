# Crie um algorítmo que leia um número e mostre seu dobro, triplo e raiz quadrada.
p = int(input('Digite um número: '))
nd = p*2
nt = p*3
nrq = p**(1/2)
nrc = p**(1/3)
print('Sobre o seu número:\nSeu dobro é {}.\nSeu triplo é {}.\nSua raiz quadrada é {}.\n\
Sua raiz cúbica é {}.'.format(nd,nt,nrq,nrc))