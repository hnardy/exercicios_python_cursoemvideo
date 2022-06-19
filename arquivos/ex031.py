#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

n = int(input('quantos quilometros tem essa viagem?'))

if n <=200:
    print(' a passagem irá custar R$:{:.2f}'.format(n*0.50))
else:
    print('a passagem ira custar R$:{:.2f}'.format(n*0.45))