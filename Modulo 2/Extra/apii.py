import requests

dados = requests.get('https://68e3f2d48e116898997a8bd0.mockapi.io/restaurante')

result = dados.json()

prato = input(' escolha o seu prato: ')
bebida = input(' escolha a sua bebida: ')
mesa = input(' escolha a sua mesa: ')

pedido = {
    'Prato':prato,
    'Bebida':bebida,
    'Mesa': mesa
}

requests.post('https://68e3f2d48e116898997a8bd0.mockapi.io/restaurante', pedido)
