#escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
n = float(input('qual é o salario atual'))
if n > 1250.00:
    sn = (n+(n*10/100))
    a = '10'
else:
    sn = (n +(n*15/100))
    a = '15'
print('o salario de {:.2f} com um ajuste de {}% passa a valer {:.2f}'.format(n,a,sn))