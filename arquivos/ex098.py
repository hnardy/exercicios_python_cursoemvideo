# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep


def contador(ini, fin, passo):
    print()
    print(f'contando de {ini} até {fin} de {passo} em {passo}')
    if passo == 0 or '':
        passo = 1

    if ini > fin:
        fin -= 1
        if passo > 0:
            passo = passo * -1

    elif fin > ini:
        fin += 1
        if passo < 0:
            passo = passo * -1

    for x in range(ini, fin, passo):
        print(x, end=' ')
        sleep(0.1)


contador(1, 10, 1)
contador(10, 0, -2)

print()
inicio = int(input('inicio'))
fim = int(input('fim:'))
pas = int(input('passo'))
contador(inicio, fim, pas)
