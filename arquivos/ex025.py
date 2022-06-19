#crie um programa que leia o nome de uma pessoa e diga se ela tem o nome silva no nome
n = str(input('digite seu nome'))
n = n.lower()
n.strip()
print ('seu nome possui "silva" {}'.format('silva ' in n ))
