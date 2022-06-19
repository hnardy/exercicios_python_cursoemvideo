from uu import Error


def menu():
    while True:
        print('=' * 30)
        print('\033[33m \t1 \033[m', ' \033[36m  \tnovo cadastro \033[m')
        print('\033[33m \t2 \033[m', ' \033[36m \tmostrar cadastros \033[m')
        print('\033[33m \t3 \033[m', '\033[36m \tencerrar programa \033[m')
        print('=' * 30)

        try:
            resp = int(input('\033[32m sua opção:\033[m'))
        except(TypeError, ValueError):
            print('\033[31m comando não aceito, tente novamente \033[m')
            continue
        else:
            if 0 < resp < 4:
                cabeçario(f'escolhida função: {resp}')
                if resp == 1:
                    cadastrar()
                if resp == 2:
                    mostrar()
                if resp == 3:
                    return 3
            else:
                print('\033[31mcomando fora de escopo, digite um número entre 1 e 3\033[m')
                continue


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mvalor inconsistente\033[m')
            continue
        else:
            return n


def cabeçario(msg, a=30):
    print('=' * a)
    print(msg.center(a))
    print('=' * a)


def cadastrar():
    indiv = dict()
    indiv['nome:'] = str(input('nome:')).strip().capitalize()
    indiv['idade:'] = str(leiaint('idade:')).strip()
    arq = arquivoescrever()
    for x, y in indiv.items():
        arq.write(x)
        arq.write(y)
        if x =='idade:':
            arq.write(' anos')
        arq.write(' ')
    arq.write('\n')


def mostrar():
    cabeçario('cadastros')
    arq = arquivoler()
    l = arq.readlines()
    for x in l:
        print(x)


def arquivoescrever():
    a = open("cadastros.txt", 'a')
    return a


def arquivoler():
    a = open('cadastros.txt', 'r+')
    return a

def criararq():
    try:
        a = arquivoler()
    except FileNotFoundError:
        print('arquivo criado')
        arg = arquivoescrever()
        arg.write(' ')
    else:
        print('arquivo encontrado')
