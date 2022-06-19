# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
a = 0
cont =0
for c in range(0,6):
    n = int(input('digite um numero'))
    if n % 2 == 0:
        a += n
        cont +=1
        # print(a)
print('a soma {} dos numeros pares digitados é {}'.format(cont,a))
