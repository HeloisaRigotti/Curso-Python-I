from os import system
import random # random = utilizar escolha aleatório
system('cls')
set
continua = 'S'

# while > enquanto

while continua =='S':

    computador = random.randint(0,2)
    jogador = int(input('''Opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura
    Escolha uma opção:'''))

    system('cls')


    if jogador >= 0 and jogador <=2:
        peças = ('Pedra', 'Papel', 'Tesoura')
        print(f'Computador escolheu {peças[computador]}')
        print(f'Você escolheu {peças[jogador]}')

        tabela = ((0 , 1 , -1 ) , (-1 , 0 , 1) , (1 , -1 , 0))  #opções de jogada
        jogada = tabela[computador][jogador]

        if  jogador == -1:
            print('Você perdeu!')
        elif jogada == 0:
            print('Empate!')
        else:
            print('Você venceu a Máquina')

                

    else:
        print("Jogados escolheu uma opção inválida")

    continua = input('Digite [S] para jogar novamente: ').upper()