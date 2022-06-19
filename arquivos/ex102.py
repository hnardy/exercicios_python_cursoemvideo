# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(a,show=False):
    """
    calcula o faltoral de um número
    :param a: numero a ser faturado
    :param show: True para mostrar o processo da conta
    :return: sem return
    """
    soma = 1
    for x in range (a, 0, -1):
        soma *= x
        if show == True:
            print(x, end=' *  ' )
    print('=', soma)

while True:
    fatorial(int(input('digite um numero para ver seu fatorial')), show=True)

