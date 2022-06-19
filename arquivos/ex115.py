# crie um pequeno sistema modularizado que permita cadastrar pessoas
# pelo seu nome e idade em arquivos de texto simples
# o sistema só vai ter duas opções: cadastrar uma nova pessoa
# e listar todas as pessoas cadastradas
import ex115modulo

ex115modulo.criararq()
while True:
    try:
        resp = ex115modulo.menu()
    except KeyboardInterrupt:
        print('programa finalizado')
        break
    if resp == 3:
        break
