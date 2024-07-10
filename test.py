# AGE CALCULATOR

# question = input("How old are you? ")
# age = int(question)
# age_in_days = age * 365
# print(f"You are {age_in_days} days old")

# SHOPPING CART EXERCISE

# print('''WELCOME TO OUR USELESS STORE
# ****************************''')
# item = input("What item are you purchasing? ")
# price = float(input(f"What is the price of {item}? "))
# quantity = float(input(f"How many {item} are you buying? "))
# print('\n')
# print(f"Added {quantity} {item}(s) to shopping cart")
# print(f"Subtotal: ${price*quantity}")


# msg = "         Hi lol          "
# msg = msg.strip(' ')
# print(msg)

# replace = '3kilometers 5kilometers 10kilometers 15kilometers'
# print(replace.replace('kilometers', 'km', 2))

# email = 'TODD@gmail.com     '
# email = email.strip().lower()    # method chaining doesn't work always
# print(email)                     # on every method


# PRESS RELEASE EXERCISE

# press_release = """

# Doody Calls, a nation wide leader in dog poop removal
# services, is growing its footprint in the pooper scooper
# industry with the opening of an office in Orlando,
# Florida. Doody Calls currently cleans up dog poop in over
# 57 territories across 23 states and has been named the
# number-one dog poop removal franchise in the United States
# by Entrepreneur Magazine's annual Franchise 500 list.

# """

# press_release = press_release.strip().replace("dog poop", "pet waste").replace("Doody Calls", "DoodyCalls").upper()
# print(press_release)

# print(ord('A'))

# age = int(input("How old are you? "))
# if age >= 21:
#     print("Come on in!")
# else:
#     print("Go home kid.")

# color = "blue"

# if color == "green":
#     print("BEGINNER!")
# elif color == "blue":
#     print("INTERMEDIATE!")
# elif color == "black":
#     print("ADVANCED!")

# IF statements will only run if the above IF statements are false.
# if the above IF statement is true the ELIF statements below won't run.

# WEATHER ADVICE EXERCISE

# temp = int(input("What is the temperature today?(in celsius) "))

# if temp > 30:
#     print("It's hot outside! Stay hydrated.")
# elif 20 <= temp <= 30:
#     print("The weather is nice and warm.")
# elif 10 <= temp < 20:
#     print("It's a bit chilly. You might need a jacket")
# else:
#     print("It's cold outside. Dress warmly")
    

# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
# full_name = len(first_name + last_name)

# if full_name > 12:
#     print(f"{first_name} {last_name} is longer than average american name")
# elif full_name < 12:
#     print(f"{first_name} {last_name} is shorter than average american name")
# elif full_name == 12:
#     print(f"{first_name} {last_name} is exactly the average length for american names")

# TWEET CHECKER EXERCISE

# tweet = len(input("Enter your tweet: "))
# limit = 140
# if tweet > limit:
#     print(f"Your {tweet} char tweet is {tweet - limit} chars too long")
# else:
#     print(f"That {tweet} char tweet will work!")

# mood = 'happy'

# if mood == 'happy':
#     print('If you are happy then I am happy')
#     print(':) ' * 10)

# temp = 39
# unit = 'fahrenheit'

# if unit == 'fahrenheit':
#     if temp <=32:
#         print("It's freezing outside!")
#     else:
#         print("It's not freezing")
# else:
#     print("I'am really bad with celsius")

# # WATER BOILING EXERCISE

# unit = input("What unit are you using? ")
# temp = int(input("What is the temperature of water? "))

# if unit == 'f':
#     if temp == 212:
#         print("WATER IS BOILING")
#     else:
#         print("WATER IS NOT BOILING. MUST HIT 212F")
# elif unit == 'c':
#     if temp == 100:
#         print("WATER IS BOILING")
#     else:
#         print("WATER IS NOT BOILING. MUST HIT 100C")
# elif unit == 'k':
#     if temp == 373:
#         print("WATER IS BOILING")
#     else:
#         print("WATER IS NOT BOILING. MUST HIT 373K")
# else:
#     print("I don't know this unit!!!")

# BMI EXERCISE

# height = float(input("What is your height?(in inches) "))
# weight = float(input("What is your weight?(in pounds) "))

# BMI = (weight * 703)/(height**2)
# BMI = round(BMI, 1)
# if BMI < 16.0:
#     category = 'Severely Underweight'
# elif 16.0 == BMI <= 18.4:
#     category = 'Underweight'
# elif 18.4 < BMI <= 24.9:
#     category = 'Normal'
# elif 24.9 < BMI <= 29.9:
#     category = 'Overweight'
# elif 29.9 < BMI <= 34.9:
#     category = 'Moderately Obese'
# elif 34.9 < BMI <= 39.9:
#     category = 'Severely Obese'
# elif BMI > 39.9:
#     category = 'Morbidly Obese'

# print(f"Your BMI of {BMI} makes you {category}")

# day = input("What day is today? ")
# if day == "Sunday" or day == "Saturday":
#     print("YAYYY! It's a weekday :)")
# else:
#     print("UGHH! It's a workday :(")

# year = input("What year were you born in? ")

# if not year.isnumeric():
#     year = input("That's not a number! Please try again.")

# year = int(year)
# print(f"You were born {2024-year} years ago")

# color = input("Enter your favourite color: ")
# if color:   # if user just presses enters in input it is an empty string. If string is empty it means it is false so if condition won't run. 
#     print(f"{color} is my favourite color too")

# answer = input("Please say hi ")

# while answer != "hi":
#     answer = input("Rude. Say hi... ")

# print("Thank you. Hi to you too!")

# count = 1
# while count <= 5:
#     print("*" * count)
#     count += 1

# num = 10
# while num > 0:
#     print(f"Number is: {num}")
#     num -= 1

# word = 'Hello'
# for char in word:
#     print(char)

# for letter in 'Pop tart':
#     print(letter)

# for num in range(-10, 10):  # doesn't include 10 (the stopping point)
#     print(num)

# for num in range(10):
#     print("HELLO WORLD!!")

# for num in range(0,100,2):
#     print(num)

# for num in range(10,0,-1):  # in order to count backwards
#     print(num)



# LOOPS PROBLEM SET

# word = "supercalifragilisticexpialidocious"

# for w in word:
#     print(w)

# index = 0
# length = len(word)
# while index != length:
#     print(word[index])
#     index += 1

# start = 100
# while start <= 140:
#     print(start)
#     start += 2

# for num in range(100,142,2):
#     print(num)

# passphrase = 'sillygoose'
# user_input = input("Please say the word: 'sillygoose' -->   ").lower()
# while user_input != passphrase:
#     user_input = input("Hey that's not nice. Please say it: ").lower()
# print("Thanks for saying it! :)")

# for char in 'pickelface':
#     if char == 'f':
#         break
#     print(char)

# print("After loop")

# message = input("say hi: ").lower()
# while True:
#     if message == "hi":
#         print("Thank you. Hi to you too!")
#         break
#     else:
#         message = input("That's rude. Please say hi.. ").lower()

# for char in "FATCAT":
#     if char == "A":
#         continue
#     print(char)


# for letter in "supercalifragilisticexpialidocious":
#     if letter in "aeiou":
#         continue
#     print(letter)

# for outer in range(1,5):
#     print(outer)
#     for inner in range(1,5):
#         print("\t", inner)

def laugh_LOL():
    print("HA" * 20)
    print("LOL" * 20)
laugh_LOL()

def laugh(intensity):
    print("HA!" * intensity)
    
def divide(numerator, denominator):
    if denominator == 0:
        return "Cannot divide by zero!"
    return numerator/denominator     
# can have multiple return statements in a function but only one of them
# will ever run and return keyword also marks the end of a function
# so if we have a print statement after return, it won't be printed.

num = divide(12,3)
print(num)
num = divide(4,0)
print(num)

def is_even(num):
    if num % 2 == 0:
        return True
    return False

x = is_even(134326)
print(x)

def slugify(string):
    string = string.replace(" ", "-").lower()
    return string

lol = slugify("Hello World I LOVE YOU")
print(lol)