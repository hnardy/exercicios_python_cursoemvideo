# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = 0
digit = 0
soma = 0
while n != 999:
    n = int(input('digite um numero inteiro'))
    if n !=999:
      digit +=1
      soma +=n
print('foram digitados {} numeros e a soma entre todos eles vale {}'.format(digit,soma))