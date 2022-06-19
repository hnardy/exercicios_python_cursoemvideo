# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

grupo = dict()
grupo['aluno'] = str(input('aluno:')).strip().capitalize()
grupo['media'] = float(input('média:'))


if grupo['media'] <=4.9:
    grupo['estado'] = 'reprovado'
elif grupo['media'] <= 6.9:
    grupo['estado'] = 'recuperação'
else:
    grupo['estado'] = 'aprovado'

for p, r in grupo.items():
    print(f'{p} = {r}')

