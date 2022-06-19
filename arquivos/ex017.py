# faça um programa que leia o comprimento do cateto oposto e do careto adjacente de um triangulo retangulo e
#calcule o valor da hipotenusa

import math
a = float(input('quanto vale o cateto adjacente?'))
b = float(input('quanto vale o cateto oposto?'))
print(" a hipotenusa de {} e {} vale {:.3f}".format(a,b,math.hypot(a,b)))