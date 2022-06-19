#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

e = str(input('digite a expressao'))
abertos = e.count('(')
fechados = e.count(')')
if abertos == fechados:
    print (' a expressão está correta')
else:
    print('a expressão está errada')