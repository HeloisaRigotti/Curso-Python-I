from os import system
system('cls')
#append>inserir lago dentro

clientes = []
telefones = []

opcao = ''

while opcao.upper() != 'X':
    system('cls')
    nome = input('Digite o nome do cliente: ')
    telefone = input('Digite o telefone do cliente: ')

    clientes.append(nome)
    telefones.append(telefone)

    system('cls')
    print(' -- Cadastro realizado com sucesso -- ')
    opcao = input('Aperete X para finalizar  ou qualquer outra tecla para continuar: ')

#Exercicos:
# Limpa a tela
system('cls')
# Listar registro -> Nome: Heloisa - Telefone: 123456789
for i in range(len(clientes)):
    print(f'Nome: {clientes[i]: <10} - telefone: {telefones[i]}')


