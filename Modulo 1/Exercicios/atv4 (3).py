estoque = 50 

while True:
    print("\n controle de estoque")
    print("(1) adicionar unidades ao estoque")
    print("(2) remover unidades do estoque")
    print("(3) verificar estoque atual")
    print("(4) sair")

    opcao = input("opção: ")
   
    if opcao == "1":
      qtd = int(input("quantidade para adicionar: "))
      estoque += qtd
      print("unidades adicionadas com sucesso")

      
    elif opcao == "2":
        qtd = int(input("quantidade para remover: "))
        if qtd < estoque:
         print(f"{qtd} unidades removidas com sucesso")
        
        else:
           estoque += qtd
           print("nao é possivel remover")

    elif opcao == "3":
      print (f"estoque atuais: {estoque} unidades")

    elif opcao == "4":
      print("encenrrando o programa!")
      break
   
    else:
        print("opção invalida! tente novamente.")
