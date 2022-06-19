# desafio 107
def aumentar(num, taxa=10, f=False):
    t = taxa / 100
    r = num + (num * t)
    if f:
        return moeda(r)
    else:
        return r


def diminuir(num, taxa=10, f=False):
    t = taxa / 100
    r = num - (num * t)
    if f:
        return moeda(r)
    else:
        return r


def dobro(num, f=False):
    r = num * 2
    if f:
        return moeda(r)
    else:
        return r


def metade(num, f=False):
    r = num / 2
    if f:
        return moeda(r)
    else:
        return r


# desafio 108


def moeda(n):
    n = float(n)
    return f'R$:{n:.2f}'

#desafio 110

def resumo(P = 0, MAX=10, MIN=10):
    print('='*30)
    print(f'{"resumo de valores":^30}')
    print('='*30)
    print(f'valor analisado {moeda(P)}')
    print(f'aumento de {MAX}% = {aumentar(P,MAX,True)}')
    print(f'diminuição de {MIN}% = {diminuir(P,MIN,True)} ')
    print(f'ao dobro {dobro(P,True)}')
    print(f'a metade {metade(P,True)}')
    print('=' * 30)