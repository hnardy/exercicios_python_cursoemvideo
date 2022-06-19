# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
posmaior = []
posmenor = []
lista = []
for c in range(0,5):
    lista.append(int(input(f'digite o {c}° valor')))
maior = max(lista)
menor = min(lista)

for p1, v1 in enumerate(lista):
    if v1 == maior:
        posmaior.append(p1)
    if v1 == menor:
        posmenor.append(p1)



print(f'o maior valor é {maior} na posição {posmaior}')
print(f'o menor calor é {menor} na posição {posmenor}')

