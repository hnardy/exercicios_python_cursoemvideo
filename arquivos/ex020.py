#o mesmo professor do desafio anterior quer sortear a ordem de apresentação de um trabalho
#dos alunis, faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle
a1 = str(input('aluno 1'))
a2 = str(input('aluno 2'))
a3 = str(input('aluno 3'))
a4 = str(input('aluno 4'))
lista = [a1,a2,a3,a4]
print ("alunos",lista)
shuffle(lista)
print ("ordem de apresnetação",lista)