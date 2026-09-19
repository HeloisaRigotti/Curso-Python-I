from os import system
system("cls")

numero = int(input("Digite um número: "))
# porcentagem em calculo, ele faz divisão e retorna o  RESTO do calculo
resto = numero % 2

# == para comparar valores
# != para comparar valores diferentes
# < para comparar valores menores
# <= para comparar valores menores ou iguais
# > para comparar valores maiores
# >= para comparar valores mmaiores ou iguais

if resto == 0:
    print( 'O numero {} é PAR!' . format(numero))
else:
    print( 'O numero {} é IMPAR!' . format(numero))