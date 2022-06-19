# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
totidade = 0
cadastro = dict()
lista = list()
mulheres = []
acimedia = dict()
acima = list()
while True:
    cadastro['nome'] = str(input('nome:'))

    cadastro['sexo'] = str(input('sexo [M/F]')).strip().upper()[0]
    while cadastro['sexo'] not in 'MF':
        print('Digite apenas os valores M ou F')
        cadastro['sexo'] = str(input('sexo[M/F]')).strip().upper()[0]
    cadastro['idade'] = int(input('idade:'))
    lista.append(cadastro.copy())
    cadastro.clear()
    print('cadastro concluído!')
    resp = str(input('deseja adicionar cadastro? [S/N]')).strip().upper()[0]
    while resp not in 'SN':
        print('comando invalido! utilize apenas S e N')
        resp = str(input('deseja adicionar cadastro? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

# print(f' A) pessoas cadastradas: {len(lista)}')


for x, c in enumerate(lista):
    totidade += lista[x]['idade']

media = totidade / len(lista)

# print(f' B) media de idade {media:.1f}')

for x, c in enumerate(lista):  # seletor de mulheres
    if lista[x]['sexo'] == 'F':
        mulheres.append(lista[x]['nome'][:])

    if lista[x]['idade'] > media:  # identifica quem está acima da média
        acimedia['nome'] = lista[x]['nome']
        acimedia['idade'] = lista[x]['idade']
        acimedia['sexo'] = lista[x]['sexo']
        acima.append(acimedia.copy())
        acimedia.clear()

# print(f' C) mulheres {mulheres}')


print(f' A) pessoas cadastradas: {len(lista)}')
print(f' B) media de idade {media:.1f}')
print(f' C) mulheres {mulheres}')
print(f' D) estão acima da média')
for x, c in enumerate(acima):
    for y, z in c.items():
        print(f' {y:^5} = {z:^15}', end=' ')
    print()
