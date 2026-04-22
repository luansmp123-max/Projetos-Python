# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.
km = float(input('Qual a quantidade de km rodados: '))
dia = int(input('Por quantos dias ele foi alugado: '))
precokm = km * 0.15
precodia = dia * 60
precototal = precokm + precodia
print('O preço a ser pago pelo aluguel do carro é: R$ {:.2f}.'.format(precototal))