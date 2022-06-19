# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = list()
jogador = dict()
gols = list()
while True:
    jogador['nome'] = str(input('nome do jogador:')).strip().capitalize()
    partidas = int(input(f'quantas partidas {jogador["nome"]} jogou?'))
    for c in range (0,partidas):
        gols.append(int(input(f'quantos gols ele fez na {c+1}° partida?:')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    jogador.clear()
    while True:
        resp = str(input('deseja continuar? [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('comando invalido, tente novamente')
    if resp == 'N':
        break
print('='*45)
print(f'{"Cod.":^3}{"NOME":^15}{"gols":^5} {"partida"}')
for pos, x in enumerate(time):
   print(f'{pos:^3} {x["nome"]:^15} {x["total"]:^5}{x["gols"]}')
print('='*45)

while True:
    while True:
        visu = int(input('digite o cod do jogador para mais detalhes (999 para)'))
        if visu <= len(time)-1 or visu == 999:
            break
        print('codigo invalido')

    if visu == 999:
        break

    for pos, c in enumerate(time[visu]['gols']):
        print(f'na partida {pos+1} o jogador {time[visu]["nome"]} fez {c} gols')
print('Programa finalizado ')

