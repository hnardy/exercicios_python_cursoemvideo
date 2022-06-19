# Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A situação (opcional)

def notas(*n, sit=False):
    """
    -> agrupa notas de alunos, destaca a maior, a menor, a média geral e a situação da classe
    :param n: notas (podem háver varias)
    :param sit: True para ver a situação da classe
    :return: dicionario contendo quantidade, maior nota, menor nota, média e situação
    """
    alunos = dict()
    alunos['quantidade'] = len(n)
    alunos['maior'] = max(n)
    alunos['menor'] = min(n)
    alunos['média'] = sum(n) / len(n)
    if sit == True:
        if alunos['média'] >= 7:
            alunos['situacao'] = 'otima'
        elif alunos['média'] >= 5:
            alunos['situacao'] = 'regular'
        else:
            alunos['média'] = 'ruim'
    return alunos


# código principal
x = notas(7, 4, 9, 6, sit=True)
for a, b in x.items():
    print(f' {a} {b}')
