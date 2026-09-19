# Converter Temperatura
from os import system
system('cls')

celsius = float(input('Digite a Temperatura em Celsius: '))

print('Escolha a Temperatura em Celsius: ')
print('1 - Fahrenheit')
print('2 - Kelvin')
opcao = int(input('Opção: '))

if opcao == 1:
    Fahrenheit = celsius * 1.8 + 32
    print('{:.2f}°C equivale a {:.2f}°F' . format(celsius, Fahrenheit))
elif opcao == 2:
    Kelvin = celsius + 273.15
    print('{:.2f}°C equivale a {:.2f} Kelvin' . format(celsius, Kelvin))
else:
    print(' Opção inválido!')