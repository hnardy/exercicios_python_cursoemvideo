# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = float(input('digite um número: '))
b = float(input('digite mais um número: '))
c = float(input('digite o ultimo número'))

if a > b and a > c:
    ma = a
if b > a and b > c:
    ma = b
if c > a and c > b:
    ma = c

if a < b and a < c:
    me = a
if b < a and b < c:
    me = b
if c < a and c < b:
    me = c

print('foram digitados os numeros {}, {} e {} '.format(a, b, c))
print('o maior numero é {} e o menor é {}'.format(ma, me))


''' outra solução
ma = a 
if b > a and b > c:
ma = b
if c > a and c > b:
#se assume um como certo e se muda caso outro seja maior assim eliminando um if




'''