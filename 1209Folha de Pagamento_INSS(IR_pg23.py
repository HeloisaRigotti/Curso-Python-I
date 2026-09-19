from os import system
system('cls')

Salario = float(input('Digite seu salário:R$ ').replace(',','.'))

if Salario <= 1621.00:
    Aliquota = 0.075
    Parcela = 0
    Desconto = Salario * Aliquota - Parcela

elif Salario <= 2902.84:
    Aliquota = 0.09
    Parcela = 24.32
    Desconto = Salario * Aliquota - Parcela

elif Salario <= 4354.27:
    Aliquota = 0.12
    Parcela = 111.41
    Desconto = Salario * Aliquota - Parcela

elif Salario <= 8475.55:
    Aliquota = 0.14
    Parcela = 198.50
    Desconto = Salario * Aliquota - Parcela

else:
    Aliquota = 0
    Parcela = 0
    Desconto = 988.07

print('Seu desconto será: R$ {:.2f}' . format(Desconto))
print('Seu salário liquido é: R$ {:.2f}' .format(Salario-Desconto))




if Salario <= 2428.80:
    Aliquota = 0
    Deducao = 0
    Desconto = 0

elif Salario <= 2826.65:
    Aliquota = 0.075
    Deducao = 182.16
    Desconto = Salario * Aliquota - Deducao

elif Salario <= 3751.05:
    Aliquota = 0.15
    Deducao = 394.16
    Desconto = Salario * Aliquota - Deducao

elif Salario <= 4664.68:
    Aliquota = 0.225
    Deducao = 675.49
    Desconto = Salario * Aliquota - Deducao

elif Salario >4664.69:
    Aliquota = 0.275
    Deducao = 908.73
    Desconto = Salario * Aliquota - Deducao


print('Seu Salário Bruto é:R$ {}' .format(Salario-Desconto))