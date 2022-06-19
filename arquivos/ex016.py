# crie um programa que leia um numero real qualque pelo teclado e mostre na tela a sua porção inteira
import math
n = float(input('digite um número real'))
print (' a parte inteira de {} vale {} '.format(n,math.trunc(n)))