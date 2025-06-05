# ------------- PRACTICE -------------------
# # ALIEN AGE CONVERTER

# user_age = float(input("What is your age: "))
# user_age = round(user_age, 1)

# dog_years = user_age * 7

# martian_years = user_age / 1.88

# jupyter_years = user_age / 11.86

# if martian_years > 30:
#     print("You are a wise martian elder!")
# else:
#     print("You are still young on Mars!")

# # DISCOUNT DETERCTOR 3000

# total_price = float(input("How much did you spent: "))
# code = input("Do you have a discount code: (Y/N)")
# if (code.upper() == 'Y'):
#     discount_percentage = float(input("What is the percentage: "))
#     discount_percentage = discount_percentage/100
#     discount_price = discount_percentage * total_price
#     final_price = total_price - discount_price
#     if (final_price > 100):
#         print("Big Spender Alert!")
#     elif 50 <= final_price <= 100:
#         print("Moderate shopper vibes")
#     else:
#         print("Frugel and proud")
# else:
#     print("No discount...")

# TWEET ANALYZER V2.0

# user_input = str(input("Enter your tweet: "))
# print("Number of characters in your tweet are: ", len(user_input))
# if (len(user_input) > 280):
#     print("Warning! your tweet limit is exceeded")

#     # final_tweet = user_input[:280] can use built in feature 

#     count = 0
#     final_tweet = ''
#     for index in user_input:
#         final_tweet += index
#         if (count > 280):
#             break
#         count += 1
#     print(final_tweet)

#     # forgot to do this bonus part to count number of hashtags in tweet
#     # hashtags = user_input.count("#")
#     # mentions = user_input.count("@")    
# else:
#     print("Nice and concise")

