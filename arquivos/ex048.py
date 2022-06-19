# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
j = int(0)
v = int(0)
for c in range(3,501,3):
   if c % 2 != 0:
        j += c
        v += 1
        print('c = {}'.format(c), )
        print('v = {}'.format(v), end= ' ')
        print('j = {}'.format(j), end= ' ')
print(' a soma dos {} valores é {}'.format(v,j))
