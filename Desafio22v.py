# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1. O nome com todas as letras maiúsculas;
# 2. O nome com todas as letras minúsculas;
# 3. Quantas letras por completo (sem considerar os espaços);
# 4. Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
print('Nome todo em Maiúsculo: {}\nNome todo em Minúsculo: {}'.format(nome.upper(), nome.lower()))
print('Quantidade de letras ao todo: {}'. format(len(nome) - nome.count(' ')))
#Ao usar find(' '), ele encontra o primeiro espaço depois do primeiro nome,
#delimitando-o assim.
#print('Seu primeiro nome possui {} letras'.format(nome.find(' ')))
nome = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome[0], len(nome[0])))