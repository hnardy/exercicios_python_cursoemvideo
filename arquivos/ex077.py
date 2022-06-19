# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
lista = ('arroz','livro','antitese','lata','ceu','aluminio','feijao','som',
         'pneumoultramicroscopicosilicovulcanoconiotico',
         'balao','queijo','sono','amor','peixe ','batata')

print('='*60)
for c in lista:

    print(c,end=' ')
    j = len(c)
    for l in range(0,j):
        if c[l] in 'aeiou':
            print(c[l], end=' ')
    print(' ')
print('='*60)

