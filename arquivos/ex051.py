# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
t = float(input('qual o primeiro termo da sua PA?'))
r = float(input('qual é a razão da sua PA?'))
te =int(input('quantos termos você quer:'))
pa = t
for c in range(0,te):
    print(pa, end=' ')
    pa +=r
print('acabou :]')

'''
p = int(input('primeiro termo'))
r = int(input('razao'))
decimo = primeiro +(10 - 1) * r
for c in range (p, decimo + r, r):
    print('{}'.format(c), end= '->'
print('acabou')
'''