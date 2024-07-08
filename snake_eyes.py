# When both dices roll number 1 at same time

import random 

roll_1 = random.randint(1,6)
roll_2 = random.randint(1,6)
roll_count = 1

while roll_1 != 1 or roll_2 != 1:
    print(roll_1, " - " , roll_2)
    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)
    roll_count += 1

print(roll_1, " - ", roll_2)
print("Snake eyes detected!")
print(f"It took {roll_count} rolls")