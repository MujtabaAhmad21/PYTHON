# Enter input - rock, paper or scissors

from random import randint

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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rand_num = randint(1,3)

if rand_num == 1:
    comp_move = rock
elif rand_num == 2:
    comp_move = paper
else:
    comp_move = scissors

user_move = input("Enter your move: ").lower()

if user_move == "rock":
    user_move = rock
elif user_move == "paper":
    user_move = paper
elif user_move == "scissors":
    user_move = scissors
else:
    print("I don't know that move")
    user_move = ""

print("Your move:- ")
print(user_move)

print("Computer move:- ")
print(comp_move)

if comp_move == user_move:
    print("It's a tie!")
elif user_move == rock and comp_move == scissors or user_move == scissors and comp_move == paper or user_move == paper and comp_move == rock:
    print("You win!")
elif user_move == "":
    print("You threw nothing. Throw rock, paper or scissors")
else:
    print("You lost")