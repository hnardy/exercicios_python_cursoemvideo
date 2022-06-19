# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
n =(date.today().year)
s = int(input('qual o seu sexo?\n [1] masculino\n [2] feminino\n'))
if s == 1:
    d = int(input('em que ano você nasceu?'))
    l = d + 18 #idade do alistamento
    i = n - d #idade
    if n < l:
        print('faltam {} ano(s) para seu alistamento obrigatorio'.format(l - n))
        print( 'voce está com {} anos e seu alistamento será em {}' .format(i,l) )
    elif n == l:
        print('você está com 18 anos! \033[32m HORA DE SE APRESENTAR, COMBATENTE\033[m')
    else:
        print('\033[31mVOCE ESTÁ ATRASADO!\033[m você deveria ter se apresentado há {} anos'.format(n-l))
        print('voce está com {} anos e deveria ter se alistado em {} '.format(i,l))
else:
    print('você não é obrigada a se apresentar ao exercito')