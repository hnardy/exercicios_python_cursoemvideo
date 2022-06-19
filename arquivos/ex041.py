# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date
a = date.today().year #obter ano atual

n = int(input('em que ano você nasceu?')) # ano de nascimento
i = a - n #idade = ano atual - ano de nascimento

print('você tem {} anos e portanto sua categoria é:'.format(i))

if i <= 9:
    print('MIRIN')

elif 9 < i <= 14 : # i <=14
    print('INFANTIL'
          )
elif 14 < i <=19: #i <= 19
    print('JÚNIOR')

elif 19 < i <=25: # i <= 25
    print('SÊNIOR')

elif i > 25: #else:
    print('MASTER')
