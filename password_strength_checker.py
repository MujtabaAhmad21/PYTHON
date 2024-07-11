# Not only does this function checks the strength of password 
# but it also counts the number of digits and lowercase, uppercase,
# special characters if needed to use. As well as the criteria can
# be altered in any way you want if there is an intermediate
# strength of password required because of conditional statements used.

# The password length should be at least 8 characters.
# The password should contain at least one uppercase letter.
# The password should contain at least one lowercase letter.
# The password should contain at least one digit.
# The password should contain at least one special character from the set !@#$%^&*()-_.

def check_password_strength(password):
# to check length of password
    if len(password) < 8:
        check_length = True
    else:
        check_length = False

# to check uppercase letters
    uppercase_count = 0
    for word in password:
        if word in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercase_count += 1

# to check lowercase letters
    lowercase_count = 0
    for word in password:
        if word in "abcdefghijklmnopqrstuvwxyz":
            lowercase_count += 1

# to check digits
    digit_count = 0
    for word in password:
        if word in "0123456789":
            digit_count += 1

# to check special characters
    special_char_count = 0
    for word in password:
        if word in "!@#$%^&*()-_":
            special_char_count += 1

    if check_length or uppercase_count < 0 or lowercase_count < 0 or digit_count < 0 or special_char_count < 0:
        return "Your password is weak"
    else:
        return "Your password is strong"
    
user_pass = input("Enter your password: ")
strength_pass = check_password_strength(user_pass)
print(strength_pass)