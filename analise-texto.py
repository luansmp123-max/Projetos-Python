# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ela.
p = input ('Digite algo: ')
print('O tipo primitivo desse valor é',type(p))
print('Só tem espaços?',p.isspace())
print('É um número?',p.isnumeric())
print('É alfabético?',p.isalpha())
print('É alfanumérico?',p.isalnum())
print('Está em maiúsculas?',p.isupper())
print('Está em minúsculas?',p.islower())
print('Está capitalizado?',p.istitle())