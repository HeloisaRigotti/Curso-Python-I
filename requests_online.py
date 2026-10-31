from os import system
system('cls')

# usar teste> https://fakestoreapi.com/

import requests

# Trazer informações via API da loja FakeStote
produtos = requests.get('https://fakestoreapi.com/products')
# Converter informações pra JSON
produtos = produtos.json()


print(f'{'ID':<3} | {'PRODUTO':<97} | {'PREÇO':<6}')
print('=' * 112)

for produto in produtos:
    # Recuperar informações do produto
    id = produto["id"]
    title = produto["title"]
    price = produto["price"]
    # Exibir informações dem lista

    print(f'{id:<3} | {title:<97} | {price:<6}')
    print('-' * 112)
