from importlib import import_module
from imagens import rock
from imagens import paper
from imagens import scissors
import os

fim_jogo = False
while fim_jogo == False:
    escolha = int(input("\nO que você escolhe? Digite \n0 para Pedra, \n1 para Papel ou \n2 para Tesoura. \n= "))
    game = [rock, paper, scissors]
    if escolha > 3 or escolha < 0:
        print("você escolheu um número inválido. Você perdeu!")
    else: print(game[escolha])

    import random
    cpu = random.randint(0,2)
    print(f"Computador escolheu: \n {game[cpu]} ")


    if escolha == 0:
        if cpu == 1:
            print("Você perdeu")
        elif cpu == 2:
            print("Você ganhou")
        else: print("Empatou")
    elif escolha == 1:
        if cpu == 0:
            print("Você ganhou!")
        elif cpu == 2:
            print("Você perdeu!")
        else: print("Empatou!")
    elif escolha == 2:
        if cpu == 0:
            print("Você perdeu!")
        elif cpu == 1:
            print("Você ganhou!")
        else: print("Empatou!")
    novamente = input("Tentar novamente? S o N: \n").lower()
    if novamente == "n":
        print("Ok, até uma próxima!")
        fim_jogo = True
    else: os.system("cls")


