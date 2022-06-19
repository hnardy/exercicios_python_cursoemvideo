#: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = float(input('digite um numero'))

if n % 2 == 0:
    print ('{} é par'.format(n))
else:
    print('{:.99f} é impar'.format(n))