#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    v = str(input('digite um valor numerico'))
    if v not in lista:
        lista.append(v)
        print(f'\033[32mvalor {v} adicionado a lista\033[m')
    else:
        print(f' \033[31mo valor {v} já existe na lista e não foi adicionado novamente...\033[m')

    escolha = ' '
    while escolha not in 'snSN':
        escolha = str(input('deseja continuar? S/N')).upper().strip()[0]
    if escolha == 'N':
        break
lista.sort()
print(f'os valores digitados em ordem crescente são {lista}')