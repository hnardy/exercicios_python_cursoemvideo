# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []

while True:
    escolha = ' '
    lista.append(int(input('digite um valor')))
    while escolha not in 'SN':
        escolha = str(input('deseja continuar? S/N')).upper().strip()[0]
    if escolha == 'N':
        break
print('-='*30)
print(f'a lista ficou: {lista}')
print(f'foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'ordenada em forma decrescente a lista fica {lista} ')
if 5 in lista:
    print('o numero 5 se encotra na lista')
else:
    print('a lista não tem numero 5')