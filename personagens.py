from os import system
from datetime import datetime
import random

system('cls')

class Personagem:
    def __init__(self, nome, energia, dano):
        self.nome = nome
        self.energia = energia
        self.dano = dano

    def atacar(self, inimigo):
        energia_anterior = inimigo.energia
        inimigo.energia -= self.dano
        # Evita energia negativa
        inimigo.energia = max(inimigo.energia, 0) 
        print(f'{self.nome} atacou {inimigo.nome} causando {self.dano} de dano!')
        print(f'{inimigo.nome} tinha {energia_anterior} e agora tem {inimigo.energia} de energia restante.\n')

        if inimigo.energia == 0:
            print(f'{inimigo.nome} foi derrotado por {self.nome}\n')
            return True

print("="*50)
print("Bem-vindo ao jogo de batalha!")
print("="*50)

# Criação dos personagens
mago = Personagem("Mago", 100, 20)
guerreiro = Personagem("Guerreiro", 120, 15)
personagem_random = Personagem("Random", random.randint(80, 150), random.randint(10,25))

while True:
    atacar = random.choice([mago, guerreiro, personagem_random])
    if atacar == mago:
        atacado = random.choice([guerreiro, personagem_random])
    elif atacar == guerreiro:
        atacado = random.choice([mago, personagem_random])
    else:
        atacado = random.choice([mago, guerreiro])

    if atacar.atacar(atacado) == True:
        break # Sai do loop se um personagem for derrotado

# mago.atacar(guerreiro)
# guerreiro.atacar(random)
# random.atacar(mago)




