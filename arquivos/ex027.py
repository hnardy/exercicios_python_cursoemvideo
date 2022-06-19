# faça um programa que leia o nome completo de uma pessoa
# mostrando em seguida o primeiro e o ultimo nome separadamente

n = str(input(' digite seu nome')).strip()
n = n.split()
print ('seu primeiro nome é: {}'.format(n[0]))
f = len(n) -1  # é contado o numero de itens da lista e subtraido um para encaixar no formato de posição
print('seu ultimo sobrenome é {}'.format(n[f]))

