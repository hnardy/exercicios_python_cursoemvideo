 # Crie um programa que leia duas notas de um aluno e calcule sua média,
 # mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
n1 = float(input('digite a nota 1'))
n2 = float(input('digite a nota 2'))
m = (n1+n2)/2
if m < 5.0:
    print(' a média é {:.1f} portanto o aluno está \033[31mREPROVADO\033[m'.format(m))
elif m >= 5.0 and m <= 6.9:     #  (6.9 <= m >= 5.0) também funciona
    print(' a média é {:.1f} portanto o aluno está \033[33m EM RECUPERAÇÃO\033[m'.format(m))
else:
    print(' a média é {:.1f} portanto o aluno está \033[32m APROVADO \033[m'.format(m))
