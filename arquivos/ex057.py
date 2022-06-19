 # faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
 # Caso esteja errado, peça a digitação novamente até ter um valor correto
''' # funciona porém muito complicado
s = 'indefinido'
while s == 'indefinido':
 sp = str(input('qual é seu sexo? [M/F]')).strip().upper()
 if sp =='M':
  s = 'masculino'
 elif sp =='F':
  s = 'feminino'
 else:
  print('comando invalido, tente novamente')
print('seu sexo é {}'.format(s))
'''

sexco = str(input('digite seu sexo [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
   sexo = str(input('comando invalido, digite seu sexo [M/F]')).strip().upper()[0]
print('o sexo é {}'.format(sexo))