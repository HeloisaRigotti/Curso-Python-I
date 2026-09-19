from os import system
system('cls')
import time

#Inicia a contagem do "multiplicando"
for i in range(1,11):
    # Limpa a variavel "linha"
    linha = "" 
    for ii in range(1,11):
       # Vai armazenando toda a tabuada
       linha += f'{i*ii: >4} ' #: >4 = totaliza 04  caracteres, completando com espaço vazio à esquerda
    # Mostra os resultados da tabuada do "multiplcado"
    print(linha)
    time.sleep(0.2)