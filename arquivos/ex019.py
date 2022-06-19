# um professor quer sortear um de seus quatro alunos para apagar o quadro, faça um programa que ajude ele
# lendo o nome deles e escrevendo o nome do sorteado
import random
a1 = str(input('aluno 1'))
a2 = str(input("aluno 2"))
a3 = str(input("aluno 3"))
a4 = str(input("aluno 4"))
lista = [a1,a2,a3,a4]
print(random.choice(lista))