"""
Tipos de dados Primitivos (4 tipos)
"""
"""
Tipos de dados

str - string -> textos "assim" 'assim'
int - inteiro -> 123456 -12 -30 15000000 -4532 1500
float - real/ponto flutuante -> 10.4 -123.42 1230000.0 -24012.33
bool - booleano/logico -> true/false
"""

print('string ->', type('string'))
print(123456, '->', type(123456))
print(12.3, '->', type(12.3))
print(12.3==12.3, '->', type(12.3==12.3))

#Type casting

print(bool(0))
print(bool(1))
print(bool(''))
print("luiz", type("luiz"), bool("luiz"))
print("10", type("10"), type(int("10")), int("10"))
print(10, type(10), type(float(10)), float(10))
# print(10.0, type(10.0), type(int(10.0))) (não pode transformar um float em um inteiro

