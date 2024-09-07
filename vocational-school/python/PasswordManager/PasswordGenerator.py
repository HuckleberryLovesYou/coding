import random as r
from string import ascii_letters
from string import digits
from string import punctuation

#Dependencies:
#random
#string.ascii_letters
#string.digits
#string.punctuation

# DO NOT USE IT TO STORE ANY IMPORTANT DATA
# THIS IS JUST A FUN PROJECT NOT MEANT TO BE USED

LETTERS = ascii_letters #52 chars
NUMBERS = digits #10 chars
SPECIAL_CHARACTERS = punctuation.replace(":", "") #32 chars. Getting rid of the colon because it is the seperator in the password file

def generate_password(password_length, letters=True, numbers=True, special=True):
    if not letters and not numbers and not special:
        print("Can't generate a password without any characters")
        raise ValueError("Can't generate a password without any characters")

    password_length: int = round(password_length) #handles float inputs by rounding it to no decimal places
    password = []
    current_password_length: int = 0
    while password_length > current_password_length:
        list_choice = r.randint(0 , 2) #generates a value between 0 and 2. This is used to generate evenly often usage of letters, numbers and special characters
        if list_choice == 0: #LETTERS string has value 0
            if letters:
                character = LETTERS[r.randint(0, len(LETTERS)-1)]
                password.append(character)
                current_password_length += 1

        elif list_choice == 1: #NUMBERS string has value 1
            if numbers:
                character = NUMBERS[r.randint(0, len(NUMBERS)-1)]
                password.append(character)
                current_password_length += 1
        else:
            if special: #SPECIAL_CHARACTERS string has value 2
                character = SPECIAL_CHARACTERS[r.randint(0, len(SPECIAL_CHARACTERS)-1)]
                password.append(character)
                current_password_length += 1
    password_string = ""
    for i in password:
        password_string += i
    return password_stringdef main():

    print(generate_password(password_length=3, letters=True, numbers=False, special=True, characters_occurring_at_least_once=True))

if __name__ == "__main__":
    main()
