def dividir():
    try:
        a = int(input("Digite o valor de a: "))
        b = int(input("Digite o valor de b: "))
        
        if b == 0:
            print("Erro: Divisão por zero não é permitida.")
            return None
        
        resultado = a / b
        print(f"O resultado de {a} dividido por {b} é: {resultado}")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite números.")

dividir()

