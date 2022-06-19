# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
b = item = 0
for c in range(0, 5):
    item = int(input(f'digite o {c} valor'))
    a = b = 0
    if c == 0:
        print(f'valor {item} adicionado no começo da lista')
        lista.append(item)
        print(lista)
    else:
        maior = max(lista)

        if item >= maior:
            lista.append(item)
            print(f'o valor {item} foi adicionado ao final da lista')
            print(lista)
        else:
            while True:
                if item < lista[b]:
                    lista.insert(b, item)
                    print(f' o valor {item} foi adicionado na posição {b}')
                    print(lista)
                    break
                else:
                    b += 1
print(f'a lista ficou {lista}')
