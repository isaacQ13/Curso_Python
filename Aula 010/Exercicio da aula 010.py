"""
- Fazer um programa que determine se a pessoa é maior que 18 anos e menor que 34 anos
- determine se a mesma pessoa é igual a 18 anos ou igual a 34 anos
- Determine se essa mesma pessoa não se encaixa em nenhum parametro
"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
idade = int(idade)

if idade > 18 and idade < 34:
    print(f'{nome} Tem a idade entre 18 anos e 34 anos.')
    print(f'{nome} Não tem Exatos 18 ou 34 anos')
    print(f'{nome} Se encaixa nos parametros')
elif idade == 18 or idade == 34:
    print(f'{nome} não tem a idade maior que 18 e menor que 34 anos')
    print(f'{nome} tem Exatos {idade} anos')
    print(f'{nome} Se encaixa nos parametros')
else:
    print(f'{nome} Não se encaixa em nenhum parametro. ')
