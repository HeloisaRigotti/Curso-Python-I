from os import system
system('cls')

# Funçoes para trabalhar com textos
nomecompleto = input('Digite seu nome completo: ')

#len = length - conta o número de caracteres
print('- Fução para contar caracteres: ', len(nomecompleto))
# nomecompleto.upper >colocar em maiusculo
print('- Função para texto maísculo:', nomecompleto.upper())
# nomecompleto.lower >colocar em minúsculo
print('- Função para texto minúsculo:', nomecompleto.lower())
# nomecompleto.capitalize >colocar primeira letra em maisuculo
print('- Função para primeiro maísculo:', nomecompleto.capitalize())
# nomecompleto.title >primeiro  letra de cada palavra maiuscula
print('- Função para primeiro  letra de cada palavra maiuscula:', nomecompleto.title())
# strip = remove espaços em branco antes e depois do texto
print('- Função para remover espaços antes e depois do texto:', nomecompleto.strip())
# find = encontra a posição do caractere
espaço = nomecompleto.find(' ')
print('- Primeiro nome: ', nomecompleto[0:espaço])
# replace = busca e substitui texto
print(' - Remover espaços vazio:' , nomecompleto.replace(" ",""))
# len + replace = não conta espaços
print(' - Contar letras sem espaços:' , len(nomecompleto.replace(" ","")))