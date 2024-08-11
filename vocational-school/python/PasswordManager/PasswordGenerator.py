import random as r

#Dependencies:
#random

# DO NOT USE IT TO STORE ANY IMPORTANT DATA
# THIS IS JUST A FUN PROJECT NOT MEANT TO BE USED

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SPECIAL_CHARACTERS = r"!#$%&'()*+,-./;<=>?@[]^_`{|}~"

def generate_password(password_length: int):
    password_length = round(password_length)
    password = []
    for i in range(password_length):
        list_choice = r.randint(0 , 2)
        if list_choice == 0:
            character = LETTERS[r.randint(0, len(LETTERS)-1)]
            password.append(character)

        elif list_choice == 1:
            character = NUMBERS[r.randint(0, len(NUMBERS)-1)]
            password.append(character)
        else:
            character = SPECIAL_CHARACTERS[r.randint(0, len(SPECIAL_CHARACTERS)-1)]
            password.append(character)
    password_string = ""
    for i in password:
        password_string += i
    return password_string