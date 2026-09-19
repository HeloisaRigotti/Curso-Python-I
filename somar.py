# Receber 2 números do usuário, realizar a soma entre eles e exibir
# int = transforma texto em número inteiro
num1 = int(input('Informe um número: '))
num2 = int(input( 'Informe outro número: '))
soma = num1 + num2
# print('A soma entre', num1 , 'e' , num2 , 'é de' , soma)
print('A soma entre {} e {} é de {}' . format (num1, num2, soma))
