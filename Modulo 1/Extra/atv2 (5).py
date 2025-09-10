def saudacao(nome, horario):
    if horario == "manha":
        return f"olá {nome}, bom dia!"
    elif horario == "tarde":
        return f"olá {nome}, boa tarde!"
    elif horario == "noite":
        return f"olá {nome}, boa noite!"
    
nome_usuario = input("digite seu nome: ")

horario_usuario = input("digite o horario: ")

print(saudacao(nome_usuario, horario_usuario))