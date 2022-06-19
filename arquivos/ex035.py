#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# um triangulo é possivel quando a soma de duas retas SEMPRE for maior que a terceira

ra = float(input('valor da reta 1'))
rb = float(input('valor da reta 2'))
rc = float(input('valor da reta 3'))

if ra + rb > rc and ra + rc > rb and rb + rc > ra:
    print('as retas {}, {}, e  {} podem formar um triangulo'.format(ra, rb, rc))

else:
    print('as retas {}, {} e {} NÃO podem formar um triângulo'.format(ra, rb, rc))


#fim do mundo 1