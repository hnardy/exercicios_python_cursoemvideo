# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('qual o valor a ser sacado?'))
n50 = n20 = n10 = n1 = 0
while True:
    if valor >= 50:
        n50 += 1
        valor -= 50
    elif valor >=20:
        n20 += 1
        valor -= 20
    elif valor >=10:
        n10 += 1
        valor -= 10
    elif valor >=1:
        n1 +=1
        valor -=1
    if valor == 0:
        break

print(f' notas de R$:50.00: {n50}\n notas de R$:20.00: {n20}\n notas de R$:10.00: {n10}\n notas de R$:1.00:  {n1}')


##solução do professor
''' while True:
    if total >= ced
        total -=ced
        totced +=1
                    % a ação foi automatizada
    else:
if ced ==50
ced ==20
elif ced ==20
ced = 10
elif ced == 10
ced = 1 

#os valores são quem muda'''