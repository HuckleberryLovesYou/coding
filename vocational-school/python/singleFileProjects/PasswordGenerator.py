import random as r
from string import ascii_letters, digits, punctuation
import argparse

#Dependencies:
#random
#string.ascii_letters, digits, punctuation
#argparse

LETTERS = ascii_letters #52 chars
NUMBERS = digits #10 chars
SPECIAL_CHARACTERS = punctuation #32 chars

def generate_password(password_length, letters=True, numbers=True, special=True, characters_occurring_at_least_once=True):
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
        print(f"Password length must be at least {min_password_length}")
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
    parser = argparse.ArgumentParser(description="This is a Password Generator using a PRNG to generate Password with/without letters, with/without numbers or with/without special charaters\n\n\t©timmatheis-de")
    parser.add_argument("-l", "--length", required=True, action="store", dest="password_length", help="Define the length of your generated password", type=int)
    parser.add_argument("-gl", "--generate-letters", required=False, default=False, action="store_true", dest="generate_letters_boolean", help="Enable the generation of letters. [Default: True]")
    parser.add_argument("-gn", "--generate-numbers", required=False, default=False, action="store_true", dest="generate_numbers_boolean", help="Enable the generation of numbers. [Default: True]")
    parser.add_argument("-gs", "--generate-special", required=False, default=False, action="store_true", dest="generate_special_boolean", help="Enable the generation of special character. [Default: True]")
    parser.add_argument("-moo", "--must-occur-once", required=False, default=False, action="store_true", dest="must_occur_once_boolean", help="Force the password generation to generate a password in which every above defined character must occure at least once. [Default: True]")
    args = parser.parse_args()
    password = generate_password(args.password_length, letters=args.generate_letters_boolean, numbers=args.generate_numbers_boolean, special=args.generate_special_boolean, characters_occurring_at_least_once=args.must_occur_once_boolean)
    print(password)


if __name__ == '__main__':
    main()