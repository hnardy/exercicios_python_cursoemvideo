#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo (radianos)
import math
n = int(input('digite um ângulo'))
m = math.radians(n)
sen = math.sin(m)
cos = math.cos(m)
tan = math.tan(m)
print(' o ângulo de {} vale\n {:.2f} radianos,\n seno{:.2f}\n cosseno {:.2f}\n tangente {:.2f}'.format(n,m,sen,cos,tan))