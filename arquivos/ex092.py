# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
ano = datetime.now().year
cadastro = dict()

cadastro['nome'] = str(input('nome'))
cadastro['idade'] = ano - int(input('ano de nascimento'))
cadastro['ctps'] = int(input('ctps: (0 não tem)'))

if cadastro['ctps'] == 0:
    cadastro['ctps'] = 'não tem'
    for k, v in cadastro.items():
        print(f'{k} - {v}')
else:
    cadastro['contrato'] = int(input('ano de contratação:'))
    cadastro['salario'] = int(input('salario:'))
    cadastro['aposentadoria'] =  cadastro['idade'] + (cadastro['contrato'] + 35) - ano

    for k,v in cadastro.items():
        print(f'{k} {v}')