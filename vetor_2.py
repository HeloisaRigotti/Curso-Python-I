from os import system
system('cls')

nomes = [] #[]=pode manipular 
total = int(input("Quantos nomes deseja cadastrar? "))

for i in range(0,total):
    system('cls')
    nomes.append(input('Digite um nome: '))

for i in range(0,total):
    print(f'nome {i} - {nomes[i]}')