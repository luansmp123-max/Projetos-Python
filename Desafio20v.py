# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de
# trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.
from random import shuffle
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
print('Os alunos sem embaralhar são:\n{}.'.format(lista))
shuffle(lista)
print('A ordem embaralhada vai ser:\n{}.'.format(lista))