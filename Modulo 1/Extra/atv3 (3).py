saldo = 1000

while True:
   print("\n caixa eletronico")
   print("(1) sacar")
   print("(2) depositar")
   print("(3) ver saldo")
   print("(4) sair")

   opcao = input("opção: ")
   
   if opcao == "1":
      valor = int(input("Valor para sacar: "))
      if valor < saldo:
         print("saldo insuficiente")

      else:
       saldo -=valor 
      print(f"saque de {valor} realizado com sucesso")

   elif opcao == "2":
        valor = int(input("valor para depositar: "))
        saldo += valor
        print(f"deposito de {valor} reais")

   elif opcao == "3":
      print (f"seu saldo atual é: {saldo} reais")

   elif opcao == "4":
      print("obrigado por usar nossos serviços!")
      break
   
   else:
      print("opção invalida! tente novamente.")


   