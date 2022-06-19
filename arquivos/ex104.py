# Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt (a):
    b = str(input(a))
    while True:
        if b.isnumeric():
            return int(b)
        else:
            print('\033[31m valor invalido \033[m ')
            b = str(input(a))


# programa principal
n = leiaInt('digite um valor numérico:')
print(f'você digitou o número: {n}')
