# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
produto = float(input('qual é o valor do produto?'))
pagamento = int(input('''
qual será a forma de pagamento?
[ 1 ] á vista em dinheiro ou cheque -10 % Off
[ 2 ] á vista no cartão -5% off
[ 3 ] em 2x no credito (sem juros)
[ 4 ] 3 ou mais vezes no credito +20% de taxa 
'''))
if pagamento == 1:
    preço = (produto - produto*10/100)
    print('a compra que custava R${:.2f} passa a custar R${:.2f}'.format(produto,preço))
elif pagamento == 2:
    preço = (produto - produto*5/100)
    print('a compra que custaca R${:.2f} passa a custar R%{:.2f}'.format(produto,preço))
elif pagamento == 3:
    preço = produto
    print('a compra de R${:.2f} será parcelada em 2 vezes de R${:.2f}'.format(produto,produto/2))
elif pagamento == 4:
    parcelas = int(input('em quantas vezes você desaja parcelar?'))
    preço = (produto + produto*10/100)
    print('a compra de R${:.2f} será parcelada em {} vezes de R${:.2f} (20% de taxa)'.format(produto,parcelas,preço/parcelas))
else:
    print('comando invalido')