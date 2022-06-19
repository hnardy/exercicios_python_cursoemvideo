# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder
# , mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

vitorias: int = 0
while True:
    s = randint(1, 10)
    print('-=' * 20)
    j = int(input('insira um número:'))
    print('-=' * 20)
    while True:        # while e not in 'ip':
        print('=' * 20)
        e = str(input('ÍMPAR OU PAR? [I/P]')).strip().upper()[0]
        print('=' * 20)
        if e in 'IP':
            break
    total = j + s
    print(f''' Jogador= {j}\n computador= {s}\n total = {total} ''')
    if total % 2 == 0:
        ptotal = 'P'
        print(' PAR')
    else:
        ptotal = 'I'
        print(' ÍMPAR')
    if ptotal == e:
        print('você ganhou :]')
        vitorias += 1
    else:
        print('você perdeu :[')
        break
print(f'total de vitorias consecutivas = {vitorias}')
