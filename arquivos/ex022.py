#crie um programa que leia o nome completo de uma pessoa e mostre
# o nome com todas as letras maiusculas, quantas letras ao (exceto o espaços)
#quantas letras tem o primeiro nome
frase = str(input('qual é seu nome completo?')).strip()



print ('seu nome somente com letras maiusculas:{}'.format(frase.upper()))
print('seu nome somente com letras minusculas: {}'.format(frase.lower()))


print('ao todo possui {} letras'.format(len(frase)-frase.count(' ')))

tp = frase.split() #cria uma lista com os subjacentes do nome
print('o seu primeiro nome é {} e possui {} letras '.format(tp[0],len(tp[0])))#conta a quantidade de caracteres no primeiro item da lista
