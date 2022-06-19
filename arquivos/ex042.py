# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes.
r1 = int(input('digite o valor da reta 1'))
r2 = int(input('digite o valor da reta 2'))
r3 = int(input('digite o valor da reta 3'))

if (r1 + r2) > r3 and (r2 + r3) > r1 and (r3 + r1) > r2:
    if r1 == r2 == r3:
        t = 'EQUILÁTERO'
    elif r1 == r2 or r1 == r3 or r2 == r3:
        t = 'ISÓSCELES'
    else:
        t = 'ESCALENO'
    print('as retas {}, {} e {} podem formar um triangulo do tipo {}'.format(r1,r2,r3,t))
else:
    print('as retas {}, {} e {} NÃO podem formar um triangulo'.format(r1,r2,r3))