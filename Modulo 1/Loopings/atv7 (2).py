senha_correta = "minhasenha"
while True:
    senha_digitada = input("digite a senha: ")
    if senha_digitada == senha_correta:
        print("senha correta, acesso concedido")
        break
    else:
        print("senha incorreta, tente novamente")