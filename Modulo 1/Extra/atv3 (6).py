while True:
    opcao = input("\nDigite 0 para sair ou qualquer tecla para cadastrar um aluno: ")

    if opcao == "0":
        print("Sistema encerrado.")
        break

    nome = input("Nome do aluno: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))

    media = (n1 + n2 + n3) / 3
    situacao = "Aprovado" if media >= 7 else "Reprovado"

    print(f"{nome} - Media: {media:.2f} - {situacao}")

    with open("alunos.txt", "a") as f:
        f.write(f"{nome} - Media: {media:.2f} - {situacao}\n")
