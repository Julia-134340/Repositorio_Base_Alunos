 
import requests 


dados=requests.get('https://68c941b9ceef5a150f641654.mockapi.io/Restaurante').json()

for item in dados:
    prato=item.get('Prato')
    id = item.get('id')

    if 'pizza' in prato:
        requests.delete(f'https://68c941b9ceef5a150f641654.mockapi.io/Restaurante/{id}')