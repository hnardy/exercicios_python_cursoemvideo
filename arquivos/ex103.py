# Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(n='< desconhecido >', g= '0'):
    """
    :param n: nome do jogador
    :param g:  quantidade de gols
    :return:
    """
    print(f'no campeonato o jogador {n} fez {g} gols')

j = str(input('jogador'))
gols = str(input('gols'))

if j == '' and gols == '':
    ficha()

if gols.isnumeric():
    int(gols)
    if j.strip() != '':
        ficha(j,gols)
    else:
        ficha(g=gols)

elif j.strip() != '':
    ficha(n=j)