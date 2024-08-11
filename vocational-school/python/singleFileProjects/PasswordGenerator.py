import random as r



LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SPECIAL_CHARACTERS = r"!#$%&'()*+,-./;<=>?@[]^_`{|}~"

#Dependencies:
#random

def generate_password(password_length):
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



def main():
    while True:
        password_length = input("Enter length of password: ")
        if password_length.isdigit():
            password_length = int(password_length)
            break
        else:
            print("Please enter a valid length")
    password = generate_password(password_length)
    print(password)
    return


if __name__ == '__main__':
    main()