import requests

while True:
   print("\n pizzaria")
   print("(1) fazer pedido")
   print("(2) mudar pedido")
   print("(3) deletar pedido")
   print("(4) sair")

   opcao = input("opção: ")

   if opcao == '1':

      dados = requests.get('https://68e3f2d48e116898997a8bd0.mockapi.io/restaurante').json()

      cardapio = print('🍕 Pizza Margherita' \
     ' preço: R$ 30  ' \
     ' 🍔 Hambúrguer Suculento ' \
     'Preço: R$ 25' \
     ' 🍲 Feijoada Tradicional ' \
     'Preço: R$ 40'
     '🥤 Coca-Cola' \
     ' preço: R$ 5  ' \
     ' 🍊 Suco de Laranja ' \
     'Preço: R$ 7.5' \
     ' 💧 Água Mineral ' \
     'Preço: R$ 3')
      
      prato = input(' escolha o seu prato: ')
      bebida = input(' escolha a sua bebida: ')
      mesa = input(' escolha a sua mesa: ')

      pedido = {
       'Prato':prato,
       'Bebida':bebida,
       'Mesa': mesa
     }
      
      requests.post('https://68e3f2d48e116898997a8bd0.mockapi.io/restaurante', pedido)
   elif opcao == '2':
       import requests


       dados = requests.get('https://68e3f2d48e116898997a8bd0.mockapi.io/restaurante')
       result = dados.json()


       for item in result:
            print(item.get('id'))

       id = input('digite o numero do id para alteramos o seu pedido')


       print('vi que voce pediu errado por favor insira o novo pedido')
       prato =  input('escolha seu prato: ')
       bebida =  input('escolha a sua bebida: ')
       mesa =  input('escolha a sau mesa: ')

       novoObjeto={
            'Prato':prato,
            'Bebida':bebida,
            'Mesa':mesa
        }
       requests.put(f'https://68e3f2d48e116898997a8bd0.mockapi.io/restaurante/{id}',novoObjeto)
   elif opcao== '3':

        dados=requests.get('https://68e3f2d48e116898997a8bd0.mockapi.io/restaurante').json()
        for item in dados:
         
         prato=item.get('Prato')
         id = item.get('id')

        if 'feijoada' in prato:
            requests.delete(f'https://68e3f2d48e116898997a8bd0.mockapi.io/restaurante/{id}')

   elif opcao == '4':
         print("obrigado por usar nossos serviços!")
         break

      


