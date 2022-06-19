# : Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
maior = menor = 0

from random import randint
lista = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
for cont  in range (0,len(lista)) :
    if cont == 0:
        menor = lista[0]
        maior = lista[0]
    if lista[cont] > maior:
        maior = lista[cont]
    if lista[cont] < menor:
        menor = lista[cont]


print(lista)
print(f'maior: {maior}')
print(max(lista))
print(min(lista))
print(f'menor: {menor}')
