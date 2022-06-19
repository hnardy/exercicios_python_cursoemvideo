# Crie um programa que declare uma matriz de dimensão 3x3
# e preencha com valores lidos pelo teclado. No final,
# mostre a matriz na tela, com a formatação correta.

lista = []
l = c = 0
for  c in range (0,3):
    for l in range(0,3):
        lista.append(int(input(f'insira o valor [{c},{l}] ')))
print(lista[0:3])
print(lista[3:6])
print(lista[6:9])
