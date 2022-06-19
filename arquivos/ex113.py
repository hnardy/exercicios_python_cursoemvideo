#  Reescreva a função leiaInt() que fizemos no desafio 104,
#  incluindo agora a possibilidade da digitação de um número de tipo inválido.
#  Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mvalor inconsistente\033[m')
            continue
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(str(input(msg)).strip().replace(',','.'))
        except(ValueError, TypeError):
            print('\033[31mvalor inconsistente\033[m')
        else:
            return n


print('o numero digitado foi', leiaint('digite um numero inteiro'))
print('o numero digitado foi', leiafloat('digite um numero decimal'))