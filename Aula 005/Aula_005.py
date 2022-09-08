"""
Aula de Operadores Aritméticos
"""
"""
+ -> Adição
- -> Subtração
* -> Multiplicação
/ -> Divisão
// -> Divisão inteira (numero arredondado)
** -> Exponenciação
% -> Resto da divisão
() -> Altera a Prescedencia das contas
"""

print("10 * 10 = ", 10 * 10)  # Multiplicação
print("10 + 10 = ", 10 + 10)  # Adição
print("10 - 5 = ", 10 - 5)    # Subtração
print("10 / 2 = ", 10 / 2)    # Divisão

print(10 * "10")
# Multiplicar uma string por um inteiro faz a string Repetir a quantidade de vezes do numero multiplicado.

print("5" + "5")
# Ao Somar duas strings você obtem a junção dos dois numeros, o exemplo em questão daria 55 por exemplo.

print(10.5 // 3)  # Divide e arredonda o valor
print(2 ** 2)     # Eleva um numero ao outro
print(10 % 3)     # Obtem o resto da divisção

# As () Fazem muita diferença na hora do calculo matematico, abaixo está um exemplo do como ela pode ser usada.
print(5+2*10)
print((5+2)*10)
