# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
mulheres20 = homens = maior18 = cont = 0
while True:

    print('-' * 20)
    print('folha de cadastro')
    print('-' * 20)
    cont += 1
    print(f'individuo #{cont}')
    idade = int(input('idade:'))
    while True:
        sexo = str(input('sexo [M/F]')).strip().upper()[0]
        if sexo in 'FM':
            break
    if idade >18:
        maior18 +=1
    if sexo =='M':
        homens += 1
    if sexo =='F' and idade <20:
        mulheres20 +=1
    while True:
        continuar = str(input('adicionar mais um cadastro? [S/N]')).upper().strip()[0]
        if continuar in 'NS':
            break
    if continuar == 'N':
        break
print(f'''
maiores de 18: {maior18}
homens cadastrados: {homens}
mulheres com menos de 20 anos: {mulheres20}
fim do programa 
''')