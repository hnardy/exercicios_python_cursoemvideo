# desenvolva um programa que leia nome,idade e sexo de 4 pessoas, no final do programa mostre
# a média de idade do grupo
# qual é p nome do homem mais velho
# quantas mulheres tem menos de 20 anos

acidade = 0# acumulador idade
hvelho ='' # homem mais velho
ivelho = 00 # idade do homem mais velho
idademulher =0 # quantidade de mulheres com menos de 20 anos
for c in range (1,5):
    nome = str(input('qual é o nome da {}° pessoa?'.format(c))).strip().capitalize()
    idade= int(input('qual é a idade da {}° pessoa?'.format(c)))
    sexo = str(input('qual é o sexo da {}°pessoa?'.format(c))).strip().lower()

    acidade +=idade

    if sexo == 'masculino':
        if idade > ivelho:
            ivelho = idade
            hvelho = nome
        elif idade == ivelho:
             hvelho = (hvelho + ' e ' + nome)

    elif sexo == 'feminino':
        if idade < 20:
            idademulher +=1



print(' a média de idade do grupo é de {} anos'.format(acidade/4))
print(' o homem mais velho é {} com {} anos'.format(hvelho,ivelho))
print(' existem {} mulheres com menos de 20 anos'.format(idademulher))