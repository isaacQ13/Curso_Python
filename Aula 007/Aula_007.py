"""
Introdução a formatação de strings
"""

# Usaremos como exemplo o exercicio anterior

nome = "Isaac Bastos"
idade = 20
altura = 1.87
peso = 89
imc = peso / (altura * altura)

print(nome, "tem", idade, "Anos de idade e seu IMC é", imc)

print(f"{nome} tem {idade} anos de idade e seu imc é {imc:.2f}")
print("{} tem {} anos de idade e seu imc é {:.2f}".format(nome, idade, imc))
print("{0} tem {1} anos de idade e seu imc é {2}".format(nome, idade, imc))
print("{2} tem {1} anos de idade e seu imc é {0}".format(nome, idade, imc))
print("{n} tem {i} anos de idade e seu imc é {im}".format(n=nome, i=idade, im=imc))

