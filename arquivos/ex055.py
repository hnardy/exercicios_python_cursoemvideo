# faça um programa que leia o peso de cinco pessoas no final mostre qual foi o maior e o menor peso lido
maior =0
menor =0
for c in range(1,6):
    p = float(input('digite o {}° peso'.format(c)))

    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
                maior = p
        if p < menor:
                menor = p

print(' maior = {} menor = {}'.format(maior,menor))