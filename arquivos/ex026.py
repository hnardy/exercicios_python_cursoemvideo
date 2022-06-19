#faça um programa que leia uma frase pelo teclado e mostre
# quantas vezes aparece a letra "a"
#em que posição ela aparece pela primeira vez
# wm que posição ela aparece pela ultima vez

n= str(input('escreva uma frase')).strip().lower()

print(' letra "a" aparece {} vezes nessa frase'.format(n.count('a')))
print(' a letra "a" aparece pela primeira vez no caranter {}'.format(n.find('a')+1))
print(' a letra "a" aparece pela ultima vez no caractere {}'.format(n.rfind('a')+1))