# Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date
anoAtual= date.today().year
idade = 0


def voto(i):
    x = anoAtual - i
    if x <16:
        v = 'NEGADO'
    elif 16<= x <18:
        v = 'OPCIONAL'
    elif 65>x>=18:
        v = 'OBRIGATORIO'
    else:
        v = 'OPCIONAL'
    return v,x

x,y = voto(int(input('em que ano você nasceu?')))
print(f'você tem {y} anos e o voto é {x}' )
