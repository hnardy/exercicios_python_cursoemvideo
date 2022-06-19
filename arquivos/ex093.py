# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.
gols = []
total = 0
jogador = dict()
jogador['nome'] = str(input('nome do jogador')).strip().capitalize()
partidas = int(input(f'quantas partidas {jogador["nome"]} jogou?:'))
for c in range(0, partidas):
    pontos = int(input(f' quantos gols o jogador {jogador["nome"]} fez na partida {c+1}?:'))
    total += pontos
    gols.append(pontos)
jogador['gols'] = gols[:]
jogador['total'] = total

print('-='*30)
print(jogador)
print('-='*30)

for k,v in jogador.items():
    print(f'o campo {k} tem valor {v}')
print('-='*30)

print(f'o jogador {jogador["nome"]} jogou {partidas} partidas')

for pos, x in enumerate(jogador['gols']):
    print(f'na partida {pos + 1} ele marcou {x} pontos')
print(f' foi um total de {jogador["total"]} gols')
