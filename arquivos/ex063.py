# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

n  = int(input('quantos elementos da sequência de fibonacci você quer ver?'))
at = 1 #atual
an = 0 #anterior
s = 0 #segurador

while n > 0:
    n-=1
    print(an,end = ' ')
    s = an # segura o valor do anterior
    an = at  # atualiza o valor do anterior
    at = s + an  # atual é igual o valor dele agora mais o valor segurado
