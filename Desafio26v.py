# Faça um programa que leia uma frase pelo teclado e mostre:
# 1. Quantas vezes aparece a letra "a";
# 2. Em que posição ela aparece a primeira vez;
# 3. Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().upper()
print('Analisando sua frase...')
print('A letra \'a\' aparece {} vezes'.format(frase.count('A')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('Ela também aparece por último na posição {}'.format(frase.rfind('A')+1))
print(len(frase))