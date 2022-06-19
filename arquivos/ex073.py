#: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('corintians','palmeiras','santos','grêmio','cruzeiro','flamengo',
         'vasco','chapecoense','atletico','bota-fogo','atletico-pr','bahia',
         'sao paulo','fluminense','sport recife','ec vitoria','curitiba','avaí',
         'ponte preta','sei lá >:)')
print('-='*35)
print(times)
print('-='*35)
print('5 primeiros {}'.format(times[0:5]))
print('-='*35)
print('4 ultimos {}'.format(times[-4:]))
print('-='*35)
print(sorted(times))
print('-='*35)
print('o time chapecoense está na {}° posição'.format(times.index('chapecoense')+1))
print('-='*35)