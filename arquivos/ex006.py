#faça um programa que pergunte um número e mostre seu dobro, triplo e raiz quadrada
n = float(input('digite um numero'))
n2 = n*2
n3 = n*3
n4 = n**(1/2)
print (' numero {} \n dobro {} \n triplo {} \n raiz quadrada {:.2f}'.format(n,n2,n3,n4))