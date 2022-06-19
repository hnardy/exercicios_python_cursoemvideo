# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for
ta = 0
t = int(input('digite um número para ver sua tabuada:'))
ti = int(input('quantos itens você quer em sua tabuada?'))

for c in range (0,ti + 1):
    ta = (t * c)
    print(' {} X {} = {}'.format(t,c,ta))
