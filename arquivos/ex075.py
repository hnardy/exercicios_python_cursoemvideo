# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
noves = 0
pares =' '
lista = (int(input('digite um número')),int(input('digite mais um número')),int(input('digite o terceiro numero')),
         int(input('digite o ultimo número')))
print(lista)
'''
for n in range (0,len(lista)):
    if lista[n] == 9:
        noves +=1
'''
noves = lista.count(9)

for n in range (0,len(lista)):
    if lista[n] % 2 ==0:
        pares += str(lista[n]) + ' '

print('-='*30)
print(f'o numero 9 foi digitado {noves} vezes')
if 3 in lista:
    print(f'o número 3 apareceu pela primeira vez na {lista.index(3)+1}ª posição')
else: print('não há numero 3 ')
print(f'são pares os numeros {pares}')

