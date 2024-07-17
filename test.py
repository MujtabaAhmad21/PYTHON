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

# def laugh_LOL():
#     print("HA" * 20)
#     print("LOL" * 20)
# laugh_LOL()

# def laugh(intensity):
#     print("HA!" * intensity)
    
# def divide(numerator, denominator):
#     if denominator == 0:
#         return "Cannot divide by zero!"
#     return numerator/denominator     
# # can have multiple return statements in a function but only one of them
# # will ever run and return keyword also marks the end of a function
# # so if we have a print statement after return, it won't be printed.

# num = divide(12,3)
# print(num)
# num = divide(4,0)
# print(num)

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False

# x = is_even(134326)
# print(x)

# def slugify(string):
#     string = string.replace(" ", "-").lower()
#     return string

# lol = slugify("Hello World I LOVE YOU")
# print(lol)

# def count_vowels(sentence):
#     count = 0
#     for word in sentence.lower():
#         if word in "aeiou":
#             count += 1
#     return count
    
# x = count_vowels("HELLO WORLD")
# print(x)

# def myfunc(def_para = 10):
#     print("HA" * def_para)
# myfunc()

# def updated_slugify(string, sep = "-"):
#     string = string.strip().lower().replace(" ", sep)
#     return string
# msg = "         I am Mujtaba and I am computer science student           "
# print(updated_slugify(msg, "_"))

# def greet(person = "stranger", msg = "Hi"):  # all default parameters should come at 
#     print(f"{msg}, {person}")   # the end of the parameter list
# greet("Tonya")
# greet()

# def get_total(price, qty=1, tax = 0.02, discount=0.0):
#     subtotal = price * qty * (1-discount)
#     print(subtotal * (1 + tax))

# # difference in keyword arguments is that order doesn't matter
# get_total(9.75, 5, 0.01, 0.5)
# get_total(qty = 5 ,price = 9.75, discount= 0.5, tax =  0.01) 

# # variables defined in a loop can be used outside the loop and anywhere.

# for char in "OCTOPUS":
#     color = "magenta"
#     print(char)

# if True:
#     animal = "OSPREY"

# print("AFTER LOOP:", color)
# print("AFTER CONDITIONAL", animal)

#   ENCLOSING SCOPE:- 
# def outside():
#     a = 10
#     def inside():
#         print("a is: ", a)
#     inside()
# outside()

# LEGB (Local - Enclosing - Global - Bult-in) scope precedence

# def outer():
#     global animal
#     animal = "Spider Crab"
# outer()

# print(animal)

# score = 100

# def double_score():
#     global score
#     score = score * 2

# double_score()
# print(score)


#    LISTS
#      |
#      |
#      |
#     \|/
#      -

# high_scores = [99, 78, 56, 50, 20, 12]
# print(high_scores)

# stuff = [4, 5.6, True, False, 'hi', []]
# print(stuff)

# new = list("hello")
# print(new)

# new_2 = list(range(3,10))
# print(new_2)

# waitlist = ['tom', 'arya', 'amir']
# for i in range(0,3):
#     print(waitlist[i])
# print(len(waitlist))

# nums = [7,3,9]
# nums[1] = 8
# print(nums)

# nums.append(5)
# print(nums)

# people = ['charlie', 'drew', 'emi']
# waitlist.extend(people)
# print(waitlist)

# nums.insert(1, 'hi')
# print(nums)

# waitlist.insert(0, 'jasmine')
# print(waitlist)

# print("superduper"[3:7])
# print("superduper"[3:7:2])

# another_list = ['c', 6, 'a', 9, 't', 6]
# print(stuff[0:2])
# print(stuff[0:5:2])

# nums = [4,5,6,7]
# nums[1:3] = ['a', 'b']
# print(nums)
# nums[1:3] = ['a', 'b', 'c', 'd']
# print(nums)
# nums[1:5] = []
# print(nums)

# langs = ["Python", "C++", "Javascript", "C"]
# langs.clear()
# print(langs)

# nums = [2,4,6,8,2,4]
# nums.remove(4)      # only removes the first match of 4
# print(nums)

# print(waitlist.pop())
# print(waitlist)

# waitlist.pop(0)
# print(waitlist)

# del nums[2]
# print(nums)

# del nums[2:]
# print(nums)

# langs = ["Python", "C", "Javascript", "C++"]
# for lang in langs:
#     print(lang)

# emails = ['jimbo@gmail.com', 'daisy@yahoo.com', 'ds32z@princess.net', 
#          'anika.345@gmail.com', 'prettyinpink@pink.com', 'otter@facebook.com'
#          , 'elton@disney.com', 'jessica@gmail.com', 'wang3@gmail.com']

# for email in emails:
#     print("******** SENDING EMAIL TO **********")
#     print(email)

# lando_2021_results = [4,3,5,8,3,5,5,5,3,4,14,10,2,7,7,8,10,10,9,10,7]
# def average(nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total/len(nums)

# print(average(lando_2021_results))

# drivers = ["Charles", "Pierre", "Valterri", "Lewis", "Geroge", "Lando"]

# drivers[2] = "Valtteri"
# print(drivers)

# drivers.append("Esteban")
# print(drivers)

# others = ["Blue", "Elton", "Colt"]
# drivers.extend(others)
# print(drivers)

# drivers.pop()
# print(drivers)

# drivers.pop(0)
# print(drivers)

# last = drivers.pop(0)
# drivers.append(last)
# print(drivers)

# drivers.remove("Blue")
# print(drivers)

# drivers.remove("Elton")
# drivers.insert(2, "Elton")
# print(drivers)

# podium = drivers[:3]
# print(podium)

# index = 0
# position = 1
# while index < len(drivers):
#     print(f"{position}. {drivers[index]}")
#     position += 1
#     index += 1 

# NESTED LISTS
#      |
#      |
#      |
#     \|/
#      -

# nums = [1,2,3,4,[5,6]]
# print(nums[4])
# print(nums[4][1])

# couples = [
#     ["Beyonce", "Jay-Z"],
#     ["Johnny", "June"],
#     ["John", "Yoko"],
#     ["Will", "Jada"]
# ]

# print(len(couples))
# print(couples[1])
# print(couples[1][0])

# for couple in couples:
#     for person in couple:
#         print(f"Sending invite to {person}")

# evens = [2,4,6]
# both = odds = [1,3,5]
# print(both)

# print(evens * 3)
# print(4 in evens)
# print(5 in evens)

# flavors = ["chocolate", "vanilla", "mango", "strawberry"]
# response = input("What flavor would you like? ")
# while response.lower() not in flavors:
#     response = input("I don't know that flavor! Try again: ")
# print(f"Ok, {response} ice cream coming right up!")

# nums = [3,4,6,7,9,0,2,3,4,5,6,7,8,1,2,3]
# print(nums.count(2))

# nums = [1,2,3,4,5]
# nums.reverse()
# print(f"Numbers reversed: {nums}")

# nums = [2,8,1,9,3]
# nums.sort()
# print(f"Numbers sorted in ascending order: {nums}")
# nums.sort(reverse=True)
# print(f"Numers sorted in descending order: {nums}")

# colors = ["red", "orange", "purple", "green"]
# colors.sort()   # uppercase and lowercase alphabet matters in sorting
# print(f"Colors sorted from a-z: {colors}") 

# print([1,2,3] == [1,2,3])
# print([1,2,3] is [1,2,3])

# evens = [2,4,6]
# evens2 = evens
# print(evens is evens2)
# print(id(evens))
# print(id(evens2))

# birthday = "03/27/2020"
# birthdaylist = birthday.split("/")
# print(birthdaylist)

# fullname = "Teddy Richard Smith"
# fullnamelist = fullname.split(" ")
# print(fullnamelist)

# fruits = ["Apple", "Kiwi", "Pear"]
# fruitslist = " ".join(fruits)
# print(fruitslist)

# newfruitslist = "!!!".join(fruits)
# print(newfruitslist)

# letters = ['M', 'A', 'S', 'H']
# newletters = "".join(letters)
# print(newletters)

# stringlist = "!".join("hello")
# print(stringlist)

# #      LIST UNPACKING:- 
# RGBlist = [255,43,19]
# red, green, blue = RGBlist
# print("Red is ", red)
# print("Blue is: ", blue)
# print("Green is:", green)

# race_results = ['bill', 'ted', 'tammy', 'jimbo', 'billybob', 'pierre']
# gold, silver, bronze, *losers = race_results
# print("Gold winner: ", gold)
# print("Silver winner: ", silver) 
# print("Bronze winner: ", bronze)
# print("Losers are: ", *losers)

# list1 = [12,9,3,7]
# list2 = list1.copy()  # this method returns a shallow copy of this list
# if it had some nested data structures, those would not have been copied.

# another way to copy is using a slice

# list2 = list1[:]
# print(list2)

# if wanted to deepcopy means the nested data structure also to be copied
# then :-
# import copy
# list1 = [2,9,['a', 'b'], 7]
# list2 = copy.deepcopy(list1)

# import pyfiglet
# ascii_banner = pyfiglet.figlet_format("Hello!!")
# print(ascii_banner)


#  DICTIONARIES
#      |
#      |
#      |
#     \|/
#      -

# cannot use a list in a dictionary because it is mutable and dictionaries
# only hold immutable types.

# to access a value :- dict[key]
# movie = {
#     "title":"Amadeus",
#     "imdb_score": 8.3
# }
# print(movie["title"])

# movie["title"] = "Blade Runner"
# print(movie["title"])

# movie["imdb_score"] += 0.5
# print(movie["imdb_score"])

# movie["rating"] = "R"
# print(movie)

# prices = {
#     "arugala": 1.10,
#     "basil": 2.54,
#     "blackberries": 4.93,
#     "blueberries": 2.88,
#     "coconut": 7.15,
#     "fennel": 3.36
# }

# product = input("What product are you buying? ")
# if product in prices:
#     price = prices[product]
#     print(f"{product} is ${price}")
# else:
#     print("I don't have that today, sorry!")

# another way to do the same thing

# product = input("What product are you buying? ")
# price = prices.get(product)
# if price:
#     print(f"{product} is ${price}")
# else:
#     print("I don't have that today, sorry!")

# prices.pop("coconut")
# print(prices)

# dict_1 = {"a": 1, "b": 2, "c": 3}
# pop_item = dict_1.popitem()
# print(pop_item)

# test_scores = {
#     "Marsha": 78,
#     "Baker": 69,
#     "Rosa": 92,
#     "Leif": 97,
#     "Peng": 61,
#     "Juan": 73,
#     "Esteban": 84,
#     "Amir": 91,
#     "Sakura": 99
# }

# for student in test_scores.keys():
#     print(student)

# total = 0
# for score in test_scores.values():
#     total += score
# print("The average is = ", total/len(test_scores))

# for items in test_scores.items():
#     print(items)

# # You can also unpack the items like this :-

# for k,v in test_scores.items():
#     print(k, v)

# max_score = 0
# best_student = ""
# for student, score in test_scores.items():
#     if score > max_score:
#         max_score = score
#         best_student = student
# print(f"Highest score was {max_score} by {best_student}")

# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4, 'e': 5, 'a':'apple'}
# d1.update(d2)
# print(d1)

# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# dict3 = {**dict1, **dict2}
# print(dict3)

# another way to perform the same thing and it is a newer version

# dict3 = dict1 | dict2       # this is called a dict union
# print(dict3)

# produce = {
#     "aragula": {
#         "price": 1.10,
#         "qty": 61,
#         "organic": True,
#         "producer": "Blue Kitty Farms"
#     },
#     "coconut": {
#         "price": 7.15,
#         "qty": 12,
#         "organic": False,
#         "producer": "Tropical Dream Farm"
#     }
# }

# print(produce["coconut"]["price"])

# test_scores = {
#     "Marsha": [78, 80, 89],
#     "Baker": [69, 65, 52]
# }

# waitlist = [
#     {
#         "email": "tiff@gmail.com",
#         "location": "USA",
#         "first_name": "Tiffany"
#     },
#     {
#         "email": "bob123@yahoo.com",
#         "location": "california",
#         "first_name": "Bobby"
#     }
# ]

#  DICTIONARY PEAK EXERCISE :-

# peak = {
#     "name": "Castle Peak",
#     "height": "14264",
#     "summit_log": [],
#     "call_reception": {
#         "AT&T": "no reception",
#         "T-Mobile": "poor"
#     }
# }

# h1 = {"height": 14265}

# peak["range"] = "Elk Mountains"
# peak["first_climbed"] = 1873
# peak.update(h1)

# peak["call_reception"]["verizon"] = "good"

# peak["summit_log"].append("Mujtaba")

# heightvar = peak.pop("height")
# peak["elevation"] = heightvar

# for values in peak.values():
#     print(values)

# for k,v in peak.items():
#     print(f"{k} -> {v}")

# peak.clear()

# print(peak)

#  TUPLES & SETS
#      |
#      |
#      |
#     \|/
#      -

# tuples are immutable

# single_tuple = ("First") --> wrong
# single_tuple = ("first",)  #--> right
# single_tuple = "First",    #--> right

# evens = {2,4,6,8,2,4}    # only unique values are stored in sets which 
# print(evens)      # are immutable, can't add a list in it and are unoredered
# evens.add(10)
# evens.add(7)      # they also don't have indexes
# evens.remove(7)

# webdev = {'SQL', 'CSS', 'HTML', 'JS', 'PYTHON'}
# datasci = {'R', 'SQL', 'PYTHON'}

# print(webdev & datasci)
# print(webdev | datasci)
# print(webdev - datasci)
# print(datasci - webdev)

#  RETURNING TO FUNCTIONS
#      |
#      |
#      |
#     \|/
#      -

# def average(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total/len(args)
# print("The average is = ", average(1,2,3,4,5,6,7,8,8))

# def count_stuff(*args):  # collects the remaining arguments in a tuple
#     print(f"You passed me {len(args)} arguments")
# print(count_stuff(1,2,6,8,9,5,30,1,34,6))

# def sum(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
# print("The sum is = ", sum(9,9,9,9,99,9,9,9,9,9,9,9,9))

# def print_ages(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k} is {v} years old")
# print_ages(Mujtaba=19 , Taha=18 , Zohaib=15)

# when defining functions, the order of the parameters matters:
# paramters - *args - default parameters - **kwargs

# def display_info(person, *args, status = "single", **kwargs):
#     print(f"person is: {person}")
#     print(f"status is: {status}")
#     print(f"args is: {args}")
#     print(f"kwargs is: {kwargs}")

# display_info("colt", "purple", 4,5,6,7,8,9)
# display_info("colt", "purple", 24,5,6,7, status="married")
# display_info("colt", "purple", 24,5,6,7, status="married", age=87, mood="thrilled")

# def add_thrice(val, lst = None):
#     if lst is None:
#         lst = []
#     lst.append(val)
#     lst.append(val)
#     lst.append(val)
#     return lst
# print(add_thrice(7, [1,2,3]))
# print(add_thrice(99))
# print(add_thrice(0))

# you can also unpack when calling a function to pass a list in *args

# ARGSKWARGS problem set

def contains_pickle(*args):
    if "pickle" in args:
        return True
    else:
        return False
    
print(contains_pickle(1,2, 'blue', 23))

def count_fails(*args):
    count = 0
    for num in args:
        if num <= 50:
            count += 1
    return count

print(count_fails(50, 41, 47, 74, 76, 81))

def get_top_students(**kwargs):
    top_students = []
    for student, score in kwargs.items():
        if score >= 90:
            top_students.append(student)
    return top_students

print(get_top_students(tim=91, stacy=83, carlos=97, jim=69))
print(get_top_students(colt=61, elton=76))
print(get_top_students(kitty=80, blue=95, toad=91, ))