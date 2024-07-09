from random import randint

num_of_dice = int(input("How many dice are we rolling? "))
dice_sides = int(input("How many sides on each die? "))

while True:
    result = "|"
    for i in range(num_of_dice):
        rand = randint(1,dice_sides)
        result += f"{rand}|"
    print(result)
    reply = input("Roll again? ('q' to quit) ")
    if reply == "q":
        print("Thanks!")
        break