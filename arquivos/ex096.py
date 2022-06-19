# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(a, b):
    c = a*b
    print(f' um terreno com {a}m por {b}m tem uma area total de {c}m^2')


largura = float(input('largura do terreno(m):'))
comprimento = float(input('comprimento do terreno(m):'))
area(largura, comprimento)
