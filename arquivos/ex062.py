#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

i = int(input('qual é o termo inicial?')) #começo
r = int(input('qual é a razão da pa?')) #razão
res = i
cont = 0
t = 10 #termos
while t !=0:
    for c in range (t,0,-1):
        print(res,end=' ')
        res += r
        cont += 1

    t = int(input('\nquantos mais termos você quer ver?'))
print('a progressão foi finalizada com {} termos mostrados'.format(cont))