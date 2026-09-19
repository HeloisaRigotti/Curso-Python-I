from os import system
system('cls')
import time

# Feito por mim
# numero = 1
#for i in range(0, 10):
#        numero = numero + 1
#        for i in range(1, 11):
#            print(f'{numero} x {i} = {numero*(i)}')



#Feito pelo Professor:
# Inicia contagem do "multiplicando"
for i in range(1,11):
    print(f'Tabuada do {i}')
    # Inicia contagem do "multiplicados"
    for ii in range(1,11):
        # Monta a expressão de multiplicaçao  - Ex: 1 x 1 = 1
        print(f'{i} x {ii} = {i*ii}')   
        time.sleep(0.5)
    print('')