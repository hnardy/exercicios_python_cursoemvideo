# faça um programa que leia um número inteiro e mostre sua tabuada
n = int(input('digite um numero para ver sua tabuada '))
print('=' * 10)
print(
    ' {} x 0 = {}\n {} x 1 = {}\n {} x 2 = {}\n {} x 3 = {}\n {} x 4 = {}\n {} x 5 = {}\n'
    ' {} x 6 = {}\n {} x 7 = {}\n {} x 8 = {}\n {} x 9 = {}\n {} x 10 = {}\n'
        .format(n, n * 0, n, n * 1, n, n * 2, n, n * 3, n, n * 4, n, n * 5, n, n * 6, n, n * 7, n, n * 8, n, n * 9, n,
                n * 10))
print('='*10)