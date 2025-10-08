 
import requests 


dados=requests.get('https://68e3f2d48e116898997a8bd0.mockapi.io/restaurante').json()

for item in dados:
    prato=item.get('Prato')
    id = item.get('id')

    if 'pizza' in prato:
        requests.delete(f'https://68e3f2d48e116898997a8bd0.mockapi.io/restaurante/{id}')