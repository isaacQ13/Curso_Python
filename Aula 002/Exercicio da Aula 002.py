"""
O exercicio que o professor mandou nessa aula
foi para pegar um cpf que ele gerou na internet automaticamente,
e colocar os separadores de acordo com o cpf no print,
usando os comandos aprendidos do print.

824.176.070-18 -> Exercicio
"""

print('824', '176', '070', sep='.', end='-')
print('18')
# Ou podemos fazer de outras formas como

print('824', end='.')
print('176', end='.')
print('070', end='-')
print('18')

# Ou podemos fazer assim

print('824', '176', sep='.', end='.')
print('070', '18', sep='-')