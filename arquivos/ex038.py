# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais
n1 = int(input('digite um numero'))
n2 = int(input('digite outro numero'))
if n1 > n2:
    print('o primeiro valor é maior')
elif n1 < n2:
    print('o segundo valor é maior ')
else:
    print('não existe valor maior, ambos são iguais')