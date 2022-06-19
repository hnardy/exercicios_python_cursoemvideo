#faça um programa que leia a largura e a altura de uma parede em metros. calcule a sua area
#e a quantidade de tinta necessaria para pinta-la (considere 1l de tinta pinta 2m2
n1= float(input('qual é a altura da parede?'))
n2= float(input('qual é a largura da parede?'))
print(' a área da parede é {}m2 e são necessarios {} litros de tinta para pinta-la'.format(n1*n2,(n1*n2)/2))