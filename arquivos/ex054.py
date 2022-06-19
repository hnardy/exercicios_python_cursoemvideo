#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maiores =0
menores =0
for c in range(1,8):
    a = int(input('em que ano a {}° pessoa nasceu'.format(c)))
    i = (date.today().year - a)
    if i >= 18:
        maiores +=1
        print('maior')
    else:
        menores +=1
        print('menor')
print('''
São de maiores {} pessoas 
São de menores {} pessoas'''.format(maiores,menores))