# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    print()
    mai = 0
    for x, c in enumerate(num):
        if x == 0:
            mai = c
        if c > mai:
            mai = c
    print(f' conjunto \n {num}\n valores digitados: {len(num)}\n maior: {mai}')

maior()
maior(1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
maior(100,1000,10000)
maior([1,20,30,100])
maior(0)
