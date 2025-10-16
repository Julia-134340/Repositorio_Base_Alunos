import requests

url = 'https://68e3f2d48e116898997a8bd0.mockapi.io/SLAYANDDINE'

pedidos = requests.get(url).json()

# print(pedidos)

for pedido in pedidos:
    print(pedido.get('id'))


    if pedido.get('id') == '6':
        print('id certo')

    else:
        print('id errado')