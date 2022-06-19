#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('-='*20,'\n {:^35} \n'.format('gerador de PA'), '-='*20 )

p = float(input('qual é o primeiro termo da sua PA?'))
r = float(input('qual é a razão da sua PA?'))
t = int(input('quantos termos você quer na sua PA?'))
res = p
j = 0 # repetições

while j != t:
    print('{}'.format(res),end= ' ')
    j += 1
    res += r
