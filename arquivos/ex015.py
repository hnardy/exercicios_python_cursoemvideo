# %escreva um programa que pergunte a quantidade de quilometros percorridos por um carro alugado  e por quantos dias ele foi alugao calcule o preço a pagar por (considere dia = 60.00 e KM = 0,15)

km = float( input('quantos km foram rodados?'))
d = float(input('por quantos dias o veiculo foi alugado?'))

print('com {} km rodados durante {} dias o valor a ser cobrado é {}'.format(km, d, (km * 0.15) + (d * 60.00)))
