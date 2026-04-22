# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos Dólares ela pode comprar. Considere: U$ 1,00=R$ 3,27
m = float(input('Entre com seu valor em Reais para converter em Dólares: '))
c = m/3.27
print('Dólares compráveis: US${:.2f}'.format(c))