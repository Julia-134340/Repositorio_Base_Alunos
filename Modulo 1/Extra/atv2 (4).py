numero = int(input('quantos numeros voce vai digitar?  '))

positivos = 0
negativos = 0 
zeros = 0

for i in range(numero):
    n = int(input(f"digite o {i + 1}° numero: ")) 

    if n > 0:
        print(F"{n} é positivo")
        positivos += 1  
   
    elif n < 0:
        print(f"{n} é negativo")
        negativos += 1

else:
    print(f'{n} é zero')
    zeros += 1

    print("\nRelatório:")
    print(F"positivos: {positivos}")
    print(f"negativos: {negativos}")
    print(f"zeros: {zeros}")

