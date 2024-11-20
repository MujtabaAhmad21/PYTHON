# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

from random import randint

def encode(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    rand3chars_at_start = []
    rand3chars_at_end = []

    for i in range(3):
        random_alphabet = randint(0, 26)
        rand3chars_at_start.append(alphabet[random_alphabet])
        random_alphabet = randint(0, 26)
        rand3chars_at_end.append(alphabet[random_alphabet])

    if len(message) > 3:
        last = message.pop(0)
        message.append(last)
        message = rand3chars_at_start + message
        message = message + rand3chars_at_end
    else:
        message = message[::-1]

    encodedmsg = ''.join(message)
    print(f"Your encoded message is: {encodedmsg}")
    return message

def decode(string):
    if len(string) < 3:
        string = string[::-1]
    else:
        string = string[3:-3]
        start = string.pop(-1)
        string.insert(0, start)

    print(f"Your decoded message is: {string}")

msg = input("Enter your message: ")
listmsg = list(msg)
message_encoded = encode(listmsg)
decode(message_encoded)