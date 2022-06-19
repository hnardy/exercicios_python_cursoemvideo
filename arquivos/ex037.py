# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('escreva um numero'))
print('''escolha uma base para conversão
[ 1 ] para binario 
[ 2 ] para octal
[ 3 ] para hexadecimal ''')
b = int(input('digite o numero referente a base desejada:'))
if b == 1:
   print('o numero {} na base binaria vale {}'.format(n,bin(n)[2:]))
elif b == 2:
    print('o numero {} na base octal vale {}'.format(n,oct(n)[2:]))
elif b == 3:
    print('o numero {} na base hexadecimal vale {}'.format(n,hex(n)[2:]))
else:
    print ('\033[31m COMANDO INVALIDO \033[m')