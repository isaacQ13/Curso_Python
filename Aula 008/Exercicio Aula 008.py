"""
Fazer uma calculadora que mostre a soma, subtração, divisão e multiplicação entre dois numeros
"""

numero_1 = input("Digite um numero: ")
numero_2 = input("Digite mais um numero: ")

soma = int(numero_1) + int(numero_2)
subtracao = int(numero_1) - int(numero_2)
divisao = int(numero_1) / int(numero_2)
multiplicacao = int(numero_1) * int(numero_2)

print(f'A soma é: {soma}', type(soma))
print(f'A subtração é: {subtracao}', type(subtracao))
print(f'A divisão é: {divisao}', type(divisao))
print(f'A multiplicação é: {multiplicacao}', type(multiplicacao))