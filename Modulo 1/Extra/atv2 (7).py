nome = input("digite o nome: ")
email = input("digite o email: ")
telefone = int(input("digite o telefone: "))


arquivo = open("contatos.txt", "a")
arquivo.write(f'{nome}, {email}, {telefone}\n')
arquivo.close()

conteudo = open('contatos.txt', 'a')

print(conteudo.read())

conteudo.close()