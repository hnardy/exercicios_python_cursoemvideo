#Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

v1 = int(input('valor 1'))
v2 = int(input('valor 2'))
acao = 0
while acao !=5:
    acao = int(input('''oque você desejaria fazer com os valores {} e {}?
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] descobrir qual é maior?
[ 4 ] novos numeros
[ 5 ] fechar o programa? \n : '''.format(v1,v2)))
    if acao == 1:
        print('o resultado da soma entre {} e {} é {}\n'.format(v1,v2,v1+v2))

    elif acao == 2:
        print('o resultado da multiplicação entre {} e {} é {}\n'.format(v1,v2,v1*v2))

    elif acao == 3:
        if v1 > v2:
            print('{} é o maior número\n'.format(v1))
        elif v1 < v2:
            print('{} é o maior número\n'.format(v2))
        else:
            print('ambos numeros possuem o mesmo valor {}\n'.format(v1))

    elif acao == 4:
        v1 = int(input('valor 1'))
        v2 = int(input('valor 2'))

    elif acao != 5:
        print('comando invalido, tente de novo')

print('programa fechado')