# Dentro do pacote utilidadesCeV que criamos no desafio 111,
# temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
# que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.
from utilidadesCeV import dados, moeda

x = dados.leiaDinheiro('digite um valor R$:')
moeda.resumo(x, 10, 10)
