import random
import sys

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """   
_______
---'   ____)____
          ______)
          _______)
         _______)
---.__________"""

scissors = """   
_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

choices = [rock,paper,scissors]

player_choice = int(input("type 0 for rock, 1 for paper, 2 for scissors: \n"))

if player_choice >= 0 and player_choice <= 2:
    print(choices[player_choice])
cpu = random.randint(0,2)
print(f"Computer chose: {choices[cpu]}")


if player_choice == 0 and cpu == 1:
    print("you lose")
elif player_choice == 0 and cpu == 2:
    print("you win")
elif player_choice == 1 and cpu == 0:
    print("you win")
elif player_choice == 1 and cpu == 2:
    print("you lose")
elif player_choice == 2 and cpu == 0:
    print("you lose")
elif player_choice == 2 and cpu == 1:
    print("you win")
else:
    print("it's a tie")
    