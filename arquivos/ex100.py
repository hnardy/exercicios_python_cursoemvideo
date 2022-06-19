# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

números = list()


def sorteia():
    for c in range(0, 5):
        p = randint(0, 10)
        números.append(p)
        print(p, end=' ')
        sleep(0.5)
    print(f'\n números sorteados: {números}')


def somapar():
    soma = 0
    for x in números:
        if x % 2 == 0:
            soma += x
    print(f'a soma dos valores pares entre {números} resulta em {soma}')


sorteia()
somapar()
