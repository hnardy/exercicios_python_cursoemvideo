# Crie um programa que faça o computador jogar Jokenpô com você.
import random
import emoji
import sys
pe = emoji.emojize(':volcano:')
pa = emoji.emojize(':newspaper:')
te = emoji.emojize(':scissors:')

print('''vamos jogar pedra papel ou tesoura 
faça sua jogada
[ 1 ] pedra {}
[ 2 ] papel {}
[ 3 ] tesoura {}'''.format(pe,pa,te))
j = int(input('qual a sua jogada?'))

if j == 1:
    escolha = pe
elif j == 2:
    escolha = pa
elif j == 3:
    escolha = te
else:
    print('comando errado')
    sys.exit()
op = [pe,pa,te]
n = random.choice(op)

print('você: {}'.format(escolha))
print('computador: {}'.format(n))

if escolha == n:
    print('empatou :]')
if escolha == pe:
    if n == pa:
        print('você perdeu :]')
    elif n == te:
        print('você ganhou de mim :[' )
elif escolha == pa:
    if n == te:
        print('você perdeu :]')
    elif n == pe:
        print('voce ganhou de mim:[')
elif escolha == te:
    if n == pe:
        print('você perdeu :]')
    elif n == pa:
        print('você ganhou de mim :[')