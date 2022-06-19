# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas
lista = []
pares = []
impares = []
while True:
    v = int(input('digite um valor'))
    lista.append(v)
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
    resp = str(input('deseja continuar? S/N')).upper().strip()[0]
    if resp in 'N':
        break
print(f' são pares os números {pares}')
print(f' sãp ímpares os números {impares}')
print(f' a lista completa fica {lista}')
