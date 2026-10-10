from os import system
import math                         
system('cls')

# Uma loja precisa armazenar seus produtos em caixas.
# Cada caixa pode conter no maximo 10 produtos.

num_produtos = int(input("Informe o número de produto: "))
produtos_caixa = int(input("Informe a qtde produtos por caixa: "))

qtde_caixas = math.ceil(num_produtos / produtos_caixa)
print(f'Caixas necessárias: {qtde_caixas}')
      