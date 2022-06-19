# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[],[]]

for c in range(0, 7):
    n = int(input(f'digite o {c + 1}° valor'))
    if c % 2 == 0:
        lista[0].append(n)
        lista[0].sort()
    else:
        lista[1].append(n)
        lista[1].sort()

print(f'lista completa {lista}')
print(f' São ímpares {lista[0]} ')
print(f' São pares {lista[1]}')
