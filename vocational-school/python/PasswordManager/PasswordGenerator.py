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


def generate_password(password_length: int, letters=True, numbers=True, special=True, characters_occurring_at_least_once=True):
    def is_character_occurring_at_least_once(password_to_check) -> bool:
        if letters:
            is_character_lower_letter = []
            is_character_upper_letter = []

            for i in password_to_check:
                if i.islower():
                    if i in LETTERS:
                        is_character_lower_letter.append(True)
                else:
                    if i in LETTERS:
                        is_character_upper_letter.append(True)

            if not True in is_character_lower_letter or not True in is_character_upper_letter:
                return False

        if numbers:
            is_character_number = []
            for i in password_to_check:
                if i in NUMBERS:
                    is_character_number.append(True)
            if not True in is_character_number:
                return False

        if special:
            is_character_special = []
            for i in password_to_check:
                if i in SPECIAL_CHARACTERS:
                    is_character_special.append(True)
            if not True in is_character_special:
                return False

        return True

    def generate() -> str:
        password = ""
        current_password_length: int = 0
        while password_length > current_password_length:
            list_choice = r.randint(0, 2)  # generates a value between 0 and 2. This is used to generate evenly often usage of letters, numbers and special characters
            if list_choice == 0:  # LETTERS string has value 0
                if letters:
                    character = LETTERS[r.randint(0, len(LETTERS) - 1)]
                    password += character
                    current_password_length += 1

            elif list_choice == 1:  # NUMBERS string has value 1
                if numbers:
                    character = NUMBERS[r.randint(0, len(NUMBERS) - 1)]
                    password += character
                    current_password_length += 1
            else:
                if special:  # SPECIAL_CHARACTERS string has value 2
                    character = SPECIAL_CHARACTERS[r.randint(0, len(SPECIAL_CHARACTERS) - 1)]
                    password += character
                    current_password_length += 1
        return password


    if not letters and not numbers and not special:
        print("Can't generate a password without any characters")
        raise Exception("Can't generate a password without any characters")

    if characters_occurring_at_least_once:
        min_password_length: int = 0
        if letters:
            min_password_length += 2 # is 2 because the password must contain at least one lowercase and one uppercase letter
        if numbers:
            min_password_length += 1
        if special:
            min_password_length += 1
    else:
        min_password_length: int = 1

    password_length: int = round(password_length)  # handles float inputs by rounding it to no decimal places
    if password_length < min_password_length:
        raise Exception(f"Password length must be at least {min_password_length}")

    password = generate()
    if characters_occurring_at_least_once:
        while True:
            if is_character_occurring_at_least_once(password):
                print("Characters are occurring at least once.")
                break
            else:
                print(f"Characters are not occurring at least once. Regenerating password. Password skipped: {password}")
                password = generate()
    return password


def main():

    print(generate_password(password_length=4, letters=True, numbers=False, special=True, characters_occurring_at_least_once=True))

if __name__ == "__main__":
    main()
