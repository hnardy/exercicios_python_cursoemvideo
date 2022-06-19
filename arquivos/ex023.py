#crie um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separadamente
n = int(input('digite um  numero'))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('numero {}'.format(n))
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))

