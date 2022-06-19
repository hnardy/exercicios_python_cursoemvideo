# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda
n = float(input('digite um valor R$:'))
print(f'o valor {moeda.moeda(n)} mais 10% vale {moeda.aumentar(n,10,f=True)}')
print(f' o valor {moeda.moeda(n)} menos 10% vale {moeda.diminuir(n,10,f=True)}')
print(f' o dobro de {moeda.moeda(n)} vale {moeda.dobro(n,f=True)}')
print(f' a metade de {moeda.moeda(n)} é {moeda.metade(n,f=True)}')
print('\n\n\n')
#print(f' a metade de {moeda.moeda(n)} é {moeda.metade(n,f=False)}')
