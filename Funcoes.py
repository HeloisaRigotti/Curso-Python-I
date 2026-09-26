from os import system
system('cls')



def Somar(a,b):
    print(f'Soma: {a}+{b}={a+b}')

def Substrair(a,b):
    try:
        print(f'Substrair: {a}-{b}={a-b}')
    except: 
        print('Erro desconhecido')
def Multiplicar(a,b):
     try:
        print(f'Multiplicar: {a}x{b}={a*b}')
     except: 
        print('Erro desconhecido')

def Dividir(a,b):
    try: #tentar fazer
        print(f'Dividir: {a}/{b}={a/b}')
    except ZeroDivisionError as erro:
        print('Impossivel divisão por ZERO')
    except: 
        print('Erro desconhecido')



    #cadastrar um novo item em varias cadastro

opcao = ''

while opcao.upper() != 'X':
    system('cls')
    num1 = float(input('Informe o primeiro número: '))
    num2 = float(input('Informe o segundo número: '))

    opcao = int(input('''
    Opções:
    [1] - Somar
    [2] - Subtratir
    [3] - Multiplicar
    [4] - Dividir
    Escolha uma opção acima: '''))

    if opcao == 1:
        Somar(num1, num2)
    elif opcao == 2:
        Substrair(num1, num2)
    elif opcao == 3:
        Multiplicar(num1, num2)
    elif opcao == 4:
        Dividir(num1, num2)
    else:
        print('Opção inválida')

    opcao = input('Aperete X para finalizar  ou Enter para outro calculo: ')
