#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
m1000 = pmenor = cont = total = 0
while True:
    nome = str(input('nome do produto:'))
    preço = int(input('preço do produto:'))
    total += preço
    cont += 1
    if cont == 1 or preço < pmenor:
        pmenor = preço
        menor = nome
    # if preço < pmenor: #pode ser simplificado no bloco de cima
    #     menor = nome
    #     pmenor = preço
    if preço > 1000:
        m1000 += 1
    escolha = ' '
    while escolha not in 'SsNn':
        escolha = str(input('adicionar produto? [S/N]')).strip().upper()[0]
    if escolha in 'Nn':
        break
print(f'total da compra {total}')
print(f'produtos com valor acima de R$:1000 : {m1000}')
print(f'produto mais barato {menor}')
