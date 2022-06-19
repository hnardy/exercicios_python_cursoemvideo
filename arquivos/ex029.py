#faça um programa que leia a velocidade de um carro
#se ele ultrapassar 80 km/h mostre uma mensagem dizendo que ele foi multado
#a multa vai custar R$7,00 por cada KM/h acima do limite
v = int(input('qual a velocidade do motorista?'))
if v <= 80:
    print('tudo dentro dos conformes, boa viagem :)')
else:
    print('o motorista está acima do limite de velocidade de 80 Km/h >:(')
    e = v - 80
    m = float(e*7)
    print('a multa por estar {} km/h acima do limite de  fica R$:{:.2f}'.format(e,m))