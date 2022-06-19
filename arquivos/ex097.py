# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~


def escreva(msg1, msg2, msg3):
    ms = n1 = n2 = n3 = 0
    mens = [msg1, msg2, msg3]
    lista = [len(msg1)+5, len(msg2)+5, len(msg3)+5]
    for c in range(0,3):
        print('~'*lista[c])
        print(f'{mens[c]:^{lista[c]}}')
        print('~'*lista[c])


m1 = str(input('frase 1 '))
m2 = str(input('frase 2 '))
m3 = str(input('frase 3 '))
escreva(m1, m2, m3)
