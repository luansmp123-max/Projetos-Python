# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Preço do produto: R$'))
d = p*0.05
df = p-d
print('Novo preço com desconto de 5%: R${:.2f}.'.format(df))