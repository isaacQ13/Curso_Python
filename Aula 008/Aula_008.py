"""
input - Entrada de dados do usuario
"""
'''
nome = input("Qual o seu nome? ")
print(f'O usuario digitou "{nome}", e o tipo da variavel é {type(nome)}')
# input retorna como uma string
'''
nome = input('Qual o seu nome? ')
idade = input('Qual sua idade? ')
ano_nascimento = input("Qual o ano atual? ")
ano_nascimento  = int(ano_nascimento) - int(idade)

print()
print(f"{nome} tem {idade} anos e nasceu em {ano_nascimento}")



