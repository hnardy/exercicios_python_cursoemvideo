#crie um programa que disseque as informaçoes de uma variavel
n = input('digite algo')
print ("o tipo da variavel é ",type(n))
print('{} é numero? {}'.format(n,n.isnumeric()))
print('{} é alphanumerico? {}'.format(n,n.isalnum()))
print('{} é alfabetico?: {}'.format(n,n.isalpha()))
