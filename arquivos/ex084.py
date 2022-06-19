# Faça um programa que leia nome e peso de várias pessoas
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
g = list()
lista = list()
pesadas = list()
leves = list()
menorp = maiorp = cadastros = peso = 0
while True:
    cadastros +=1
    nome = str(input('nome:'))
    peso = float(input('peso:'))
    print('cadastro realizado')
    g.append(peso)
    g.append(nome)
    lista.append(g[:])
    g.clear()
    if cadastros == 1:
        menorp = maiorp = peso

    if peso == maiorp:
        pesadas.append(nome)
    if peso == menorp:
        leves.append(nome)

    if peso > maiorp:
        maiorp = peso
        pesadas.clear()
        pesadas.append(nome)
    if peso < menorp:
        menorp = peso
        leves.clear()
        leves.append(nome)

    resp = str(input('adicionar novo cadastro? [S/N]')).strip().upper()[0]
    if resp in 'N':
        break

print('=-='*40)
print(f'pessoas cadastradas = {cadastros}')
print(f'pessoas mais pessadas {pesadas} com {maiorp}Kg')
print(f'pessoas mais leves {leves} com {menorp}Kg')
