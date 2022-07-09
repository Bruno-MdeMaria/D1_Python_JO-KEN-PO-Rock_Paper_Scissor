from importlib import import_module


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
escolha = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura. \n= "))
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


