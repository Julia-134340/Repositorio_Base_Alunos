def solicitar_inteiro():
    """Solicita um número inteiro ao usuário, tratando entradas inválidas."""
    while True:
        try:
            entrada = input("Por favor, digite um número inteiro: ")
            numero_inteiro = int(entrada)
            return numero_inteiro
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")


numero_valido = solicitar_inteiro()
print(f"Você digitou o número inteiro válido: {numero_valido}")

