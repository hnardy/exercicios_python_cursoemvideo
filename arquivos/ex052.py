#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
#n = int(input('digite um numero'))
for n in range (0,1000):

    if n == 2 or n== 3 or n == 5 or n == 7 or n== 11:
        print("{} é primo".format(n))

    elif n > 1 and n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0 and n % 11 !=0:
        print("{} é primo".format(n))
    else:
        print(' o numero {} não é primo'.format(n))
''' # essa versão funciona como gerador de numeros primos

# versao alternativa
'''
m = int(input('digite um numero'))
t = 0
for c in range (1,m+1):
    if c == 2 or c ==3 or c==5 or c== 7 or c ==11:
        print('\033[32m{}\033[m'.format(c))

    elif c>1 and c % 2!= 0 and c % 3 != 0 and c % 5 != 0 and c % 7 != 0 and c % 11 != 0:
        print('\033[32m{}\033[m'.format(c))
        if c == m:
            print('o numero {} é primo'.format(m))
    else:
        print('\033[31m{}\033[m'.format(c))
        t +=1
        if c == m:
            print('  o numero {} foi dividido {} vezes e não é primo'.format(m,t))

''' # essa versão acerta se um numero é primo mas não é capaz de dizer por quais numeros ele foi dividido

#versão 3
r = int(input('digite um numero'))
t = 0
for c in range (1,r+1):
    if r % c == 0:
        print('\033[33m{}\033[m'.format(c),end= ' ')
        t +=1
    else:
        print(c,end=' ')

if t == 2:
    print(' ')
    print('o numero {} é primo'.format(r))
else:
    print(' ')
    print('o numero {} não é primo e foi dividido {} vezes'.format(r,t))
