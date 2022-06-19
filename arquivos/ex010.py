# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar (considere 1 dolar 3,27 reais)
n= float(input('quantos reais você quer vender? R$:'))
print ( 'com {:.2f} reais você pode comprar U${:.2f} dolares'.format(n,n/3.27))