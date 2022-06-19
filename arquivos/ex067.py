# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
print('-='*30)
print('{:^60}'.format('gerador de tabuada'))
print('-='*30)
while True:
    n = int(input('digite um numero para ver sua tabuada' ))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
print('programa encerrado')
