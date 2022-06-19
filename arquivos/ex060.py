#060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
n = int(input('digite um numero inteiro para ver o seu fatorial'))
r = n
print('{}! ='.format(n),end=" ")
print(n, end=' x ')
while n>1:
    n = n-1
    r = r * n
    print(n,end=' ')
    if n > 1:
        print(' X ',end=' ')
    if n == 1:
        print('=',end='  ')
print(r)
# este progrma tambem pode ser resolvido com o método factorial() da biblioteca math
# tambem ´possivel usando o metodo for
'''


n = int(input('digite um número para ver seu valor fatorial'))
r = 1
print('{}! = '.format(n),end='')
for n in range (n,0,-1):
    r *= n
    print(n,end=' ')
    print(' x ' if n > 1 else ' = ', end='' )
print(r)


