"""
* Criar variaveis para nome (str), idade (int),
* Altura (float), e peso (float) de uma pessoa
* Criar variavel com o ano atual (int)
* obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-strings (Com as chaves)
"""

nome = "isaac"
idade = 20
altura = 1.87
peso = 89.4
ano_atual = 2021
ano_de_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f"{nome} tem {idade} anos, {altura} de altura e pesa {peso}Kg.")
print(f"o IMC de {nome} é {imc:.2f}.")
print(f"{nome} nasceu em {ano_de_nascimento}.")

