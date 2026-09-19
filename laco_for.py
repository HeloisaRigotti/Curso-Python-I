from os import system
import time
system('cls')

#Laço For
# contar de 0 até 10 (até numero que a pessoa digitou)
numero = int(input('Infome um número maior que 0: '))

# Verificar se o número é positivo
if numero <= 0:
    print('Número inválido!')
else:
    # Inicinafo Laço For
    for i in range(numero):
        print(f'Valor da variáveo i: {i}')
        time.sleep(2) # dorme por 2 segundos