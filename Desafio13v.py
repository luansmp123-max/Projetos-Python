# Crie um algorítimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Salário do funcionário: R$'))
a = s*0.15
sa = s+a
print('Salário com aumento de 15%: R${:.2f}'.format(sa))