# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('-='*30)
print(f'{"LISTA DE PREÇOS":^60}')
print('-='*30)
'''
lista = ('lapis','borracha','cataputa','dente','elefante','fusca',1.00,2.10,3.20,4.30,5.40,100.50)
e = int(len(lista)/2)
print('='*60)
for n in range(0,e):
    print(f'{lista[n]:.<50} R$:{lista[n+e]:.2f}')
print('='*60)
'''

lista=('lapis', 1.00, 'b', 2.00, 'c', 300.00,'banana',3.00)

for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<50}',end='')
    else:
        print(f'{lista[pos]:.2f}')