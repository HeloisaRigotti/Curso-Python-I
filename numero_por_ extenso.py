from os import system
system('cls')

numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
dez = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
dezenas = ('','','vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')

#Pergunta ao usuário
numero = int(input("Informe um números de 0 a 99: "))

#regra
if numero >= 0 and numero <= 99:

#variaveis
    if numero < 10:
        print(numeros[numero])
    elif numero < 20:
        print(dez[numero-10])
    else:
        dezena = int(numero / 10)
        numeral = numero % 10

        if numeral == 0:
            print(dezenas[dezena])
        else:
            print(f'{dezenas[dezena]} e {numeros[numeral]}')

    
else:
    print("Numero inválido!")