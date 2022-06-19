# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
# mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

p =float(input('qual é seu peso? (em Kg)'))
a =float(input('qual a sua altura (em metros)'))
imc =  p/(a**2)
print('seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print(' você está abaixo do peso ideal')
elif imc <= 25:
    print('você está no peso ideal')
elif imc <= 30:
    print('você está com sobrepeso')
elif imc <= 40:
    print('você está com obesidade')
elif imc > 40:
    print('você está com obesidade mórbida')
