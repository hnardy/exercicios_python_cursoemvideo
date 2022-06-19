# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint
from operator import itemgetter

jogadas = {}
ranking = []
for c in range(1, 5):
    jogadas[f'jogador{c}'] = randint(1, 6)
    print(f'o jogador {c} tirou:', jogadas[f"jogador{c}"])
    sleep(0.3)

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
for pos, v in enumerate(ranking):
    print(f' em {pos + 1}° lugar {v[0]} com {v[1]}')
    sleep(0.3)
