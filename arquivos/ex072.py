#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

while True:
    escolha = int(input('digite um número para ve-lo por extenso [ 0 a 20 ]'))
    while  escolha < 0 or escolha > 20:
            escolha = int(input('digite um número para ve-lo por extenso [ 0 a 20 ]'))

    lista = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
    print(lista[escolha])