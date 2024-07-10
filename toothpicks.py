num_toothpicks = 13

player_1 = input("Enter player 1 name: ")
player_2 = input("Enter player 2 name: ")
current_player = player_1
toothpick_design = " | "

while num_toothpicks > 0:
    print(toothpick_design * num_toothpicks)
    print(f"There are {num_toothpicks} toothpicks left")
    answer = int(input(f"How many do you take, {current_player}\n"))
    while answer != 1 and answer != 2 and answer != 3:
        answer = int(input("You can only choose 1,2 and 3: "))

    num_toothpicks -= answer

    if num_toothpicks <= 0:
        print(f"{current_player} wins!")
        print("GAME OVER!!!")
        break
    if current_player == player_1:
        current_player = player_2
    else:
        current_player = player_1