# esvreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
# e peça para o usuario tentar desckbrir qual foi o numero escolhido pelo computador

from random import choice
n = choice([1,2,3,4,5,6]) # faz o sorteio (pode ser substituido pelo comando randint(1,6)
print(' ')
print('iniciando bip...')
print(' I------I\n'
      ' I 0  0 I \n'
      ' I__--__I \n'
      '   I  I ')
print('olá, escolha um numero de 0 a 6 e eu jogarei o dado')
j = int(input('digite um numero:'))

if j == n:
    print(' ')
    print(' I------I\n'
          ' I 0  - I \n'
          ' I__--__I \n'
          '   I  I ')
    print('parabens, você acertou, o numero do dado é {}'.format(n))
else:
    print(' ')
    print(' I------I\n'
          ' I 0  0 I \n'
          ' I______I \n'
          '   I  I ')
    print(' o dado caiu {}, tente novamente'.format(n))
