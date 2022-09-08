"""
Fazer um mini sistema de usuario e senha com python
"""

usuario = input("Nome de Usuário: ")
senha = input("Senha do Usuário: ")

usuario_bd = "isaac"
senha_bd = "123456"

if usuario_bd == usuario and senha_bd == senha:
    print("Vocês está logado no sistema. ")
else:
    print("Usuario ou senha Invalidos. ")