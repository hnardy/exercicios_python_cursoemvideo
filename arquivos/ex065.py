# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
maior = menor = soma = cont = n = 0
c = str('S')
while c == 'S':
    n = int(input('digite um numero inteiro'))
    cont += 1
    soma += n
    if cont == 1:
        menor = n
        maior = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    c = ' '
    while c not in 'SN':
        c = str(input('você deseja continuar?[S/N]')).strip().upper()[0]
media = soma / cont
print(' média = {:.2f}\n maior = {} \n menor = {} \n '.format(media, maior, menor))
