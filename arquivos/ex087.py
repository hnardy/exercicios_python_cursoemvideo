# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = soma = somater = 0

for c in range(0, 3):
    for l in range(0, 3):
        lista[c][l] = int(input(f'digite o valor para [{c},{l}]'))

for c in range(0, 3):
    for l in range(0, 3):
        print(f'{lista[c][l]:^5}', end=' ')
        soma += lista[c][l]
        if l == 2:
            somater+=lista[c][l]

        maior = max(lista[1])

        if lista[c][l] % 2 == 0:
            pares += lista[c][l]
    print()

print(f' a soma de todos os elementos da matriz vale {soma}')
print(f' a soma da terceira coluna {somater}')
print(f' o maior termo da segunda linha é {maior}')
print(f' a soma dos valores pares vale {pares}')