# Adapte o código do desafio # 107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.
import moeda

n = float(input('insira um valor R$:'))

print(f'o dobro de {moeda.moeda(n)} é  {moeda.moeda(moeda.dobro(n))}')
print(f'a metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')