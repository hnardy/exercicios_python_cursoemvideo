# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

t = 22
n = 1
print(f' {n} mais 10% fica {moeda.aumentar(n,taxa= t)}')
print(f' {n} menos 10% fica {moeda.diminuir(n,taxa=t)}' )
print(f' o dobro de {n} é {moeda.dobro(n)}')
print(f' a metade de {n} é {moeda.metade(n)}')