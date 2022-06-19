# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

# para o ano ser bissexto ele deve ser perfeitamente divisivel por 4
# e não ser perfeitamente divisivel por 100
from datetime import date

n = int(input('digite um ano'))
if n == 0:    # caso seja digitado o valor 0 será exibido o ano atual 
    n = date.today().year

if n % 4 == 0:
    if n % 100 != 0:
        print(' o ano {} é bissexto'.format(n))
    else:
        if n % 400 == 0:
            print('o ano {} é bissexto'.format(n))
        else:
            print('o ano {} não é bissexto'.format(n))
else:
    print('o ano {} não é bissexto'.format(n))


    #a formula pode ser simplificada com if n % 4 ==0 and n % 4 !=0 or n % 400 ==0
