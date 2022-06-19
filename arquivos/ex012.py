#faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
n = float(input('qual é o preço atual do produto?'))
print('{} com 5% de desconto passa a valer {}'.format(n,n -(n*5/100)))