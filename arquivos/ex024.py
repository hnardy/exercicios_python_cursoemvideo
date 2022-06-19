#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO

n = str(input('digite o nome da cidade')).strip().capitalize()

n1 = n.split()
print('o nome da cidade começa com Santo: {}'.format( 'Santo'in n1[0]))