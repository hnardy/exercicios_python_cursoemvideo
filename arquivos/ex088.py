# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = []
jogo = []
num = 0

jogos = int(input('quantos jogos você deseja gerar?'))
for c in range(0, jogos):
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
        if len(jogo) == 6:
            jogo.sort()
            lista.append(jogo[:])
            jogo.clear()
            break

for b in range(0,len(lista)):
    print(f'jogo {b+1}: {lista[b]}')
    sleep(0.3)