lista = [10, 20, 30]

try:
    indice_str = input("Digite um indice para acessar um elemento da lista: ")
    indice = int(indice_str)  
    elemento = lista[indice]  
    print(f"O elemento no indice {indice} é: {elemento}")

except ValueError:
    print("Erro: tente novamente.")

except IndexError:
    print("Erro: o indice nao esta na lista.")



