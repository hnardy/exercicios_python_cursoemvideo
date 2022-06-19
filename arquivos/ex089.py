# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.No final,
# mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []
indiv = []
while True:

    indiv.append(str(input('nome')).strip().capitalize())
    indiv.append(int(input('nota 1:')))
    indiv.append(int(input('nota 2:')))
    indiv.append((indiv[1] + indiv[2]) / 2)
    print('cadastro realizado')
    alunos.append(indiv[:])
    indiv.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('adicionar cadastro? [S/N]')).strip().upper()
    if resp in 'N':
        break
print('=' * 20, 'boletim', '=' * 20)

print(f'{"NO.":^3}{"NOME":^30}{"MÉDIA":^10}')
for pos, a in enumerate(alunos):
    print(f'{pos} {alunos[pos][0]:^30} {alunos[pos][3]:^10}')

print('=' * 10, 'MAIS DETALHES', '=' * 10)
while True:
    det = int(input('de qual aluno deseja ter mais informações? NO. [999 para parar]'))
    if det <= len(alunos) - 1:
        print(
            f' nome: {alunos[det][0]}\n nota 1: {alunos[det][1]}\n'
            f' nota 2: {alunos[det][2]}\n média: {alunos[det][3]}\n ')

    if det == 999:
        print('programa finalizado...')
        break
