# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

def ajuda(msg):
    print('\033[;30;47m',end='')
    help(msg)
    print('\033[m', end='')


while True:
    h = str(input('\033[32mdigite um comando para ver seu manual\033[m')).strip()
    if h.upper() == 'FIM':
        print(f' \033[0;41m OBRIDAGO, ATÉ LOGO\033[m')
        break
    else:
        ajuda(h)
