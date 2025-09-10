lista = [10, 20, 30, 40, 50]

lista.insert(5, 60)
print("apos insert:", lista)

lista[1] = 15
print("apos modificaçao:", lista)

removido =  lista.pop(2)
print(f'Após pop (removido)' '{removido}', lista)

ultimo = lista.pop()

print('lista apos remoção: ', lista)
print("elemento guardado na variavel 'ultimo': ", ultimo)