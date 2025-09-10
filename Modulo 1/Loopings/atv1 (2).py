palavra = input("digite uma palavra: ")
vogais = "aeiouAEIOU"
contador = 0

for letra in palavra:
    if letra in vogais:
       contador += 1


print("a palavra tem", contador, "vogais.")