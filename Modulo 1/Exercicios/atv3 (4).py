
def validar_senha(senha_correta, senha_digitada):
    if senha_digitada == senha_correta:
        return ("senha correta! acesso permitido")
    else:
        return ("senha incorreta! acesso negado")
    
senha_correta = "1234"
senha_usuario = input("digite a senha: ")

print(validar_senha(senha_correta, senha_usuario))