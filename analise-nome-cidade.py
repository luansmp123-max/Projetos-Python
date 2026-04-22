# Crie um programa que leia o nome de uma cidade e diga se
# ela começa ou não com o nome "Santo"
cidade = str(input('Digite o nome da cidade onde você nasceu: '))
m = cidade.lower()
santo = 'santo' in m
print(santo)