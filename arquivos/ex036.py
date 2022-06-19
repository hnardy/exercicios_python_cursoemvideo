#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
v = float(input('qual é o valor da casa? R$:'))
s = float(input('qual é o valor do salario do comprador? R$:'))
a = int(input('em quantos anos a casa vai ser paga?'))

m = a*12 # numero de prestaçoes
p = v/m  # valor das prestaçoes

if p < s*30/100:
    print('emprestimo \033[32maprovado\033[m')
    print('serão {} prestações de R$:{:.2f} cada '.format(m,p))
else:
    print(' emprestimo \033[31mnegado\033[m')
    print("o valor da parcela ({:.2f}) excedeu 30% do seu salario (R$:{:.2f})".format(p,s*30/100))
