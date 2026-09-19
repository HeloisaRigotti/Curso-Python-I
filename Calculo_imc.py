from os import system
system('cls')

# Calculadora de IMC
altura = input('Digite a sua altura em metros: ')

# Substitui virgula por ponto e converte em decimal
altura = float(altura.replace(',','.'))

# Pede para usuário digitar o peso,
# Substitui vírgula por ponto e coverte em decimal
peso = float(input('Digite a seu peso em kg: ').replace(',','.'))

# imc = peso / (altura * altura) pode ser assim tbem
imc = peso / (altura **2)

# print("Seu IMC: {} . format(imc))
print(f'Seu IMC: {imc:.2f}')

if imc < 18.5:
    print( 'Você está abaixo do peso')
elif imc < 25:
    print( 'Você está com o peso ideal')
elif imc < 29.9:
    print( 'Você está com excesso de peso')
elif imc < 34.9:
    print( 'Você está com Obesidade classe I')
elif imc < 39.9:
    print( 'Você está com Obesidade classe II')
elif imc < 40.0:
    print( 'Você está com Obesidade classe III')