try:
    with open('arquivo.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

except FileNotFoundError:
    with open ('arquivo.txt', 'w') as arquivo:
        arquivo.write('arquivo criado')