# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
n = str(input('digite uma frase')).upper().strip()
n = n.replace(' ','')
carac = len(n)
f= ''
for c in range(carac-1,-1,-1):
    f = f+n[c]
if n == f:
    print('temos um palindromo :) {} | {}'.format(n,f))
else:
    print('não temos um palindromo :( {} | {}'.format(n,f))