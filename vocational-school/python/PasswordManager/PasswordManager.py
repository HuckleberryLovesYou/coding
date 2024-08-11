#############################################################
#   inspired by 'Tech wit Tim' on Youtube                   #
#   https://youtu.be/NpmFbWO6HPU?si=NUpQHy3AY0X9-qJh&t=4008 #
#############################################################

#Dependencies:
#os
#PasswordGenerator.py
#PasswordManagerCryptography.py
#tkinter

# DO NOT USE IT TO STORE ANY IMPORTANT DATA
# NO ENCRYPTION HAPPENING HERE

import os
from PasswordGenerator import generate_password
from tkinter.filedialog import askopenfilename
import PasswordManagerCryptography

global_filename: str = ""

def get_filepath(): #let the user select a .txt-file and writes it into global_filename
    def check_for_file(filepath): #checks if file actually exists (might not be needed)
        if os.path.exists(filepath):
            print("Database found")
            return True
        else:
            print("No such database in directory")
            return False
    global global_filename
    global_filename = askopenfilename(filetypes=[("Text files" , "*.txt")])
    return global_filename, check_for_file(global_filename)



def count_lines():
    with open(global_filename, "r") as passwords_file:
        amount_of_lines: int = 0
        for _ in passwords_file.readlines():
            amount_of_lines += 1
        return amount_of_lines


def view():
    view_list = []
    if count_lines() == 0:
        view_list.append("There are no entries in your database")
        return view_list
    else:
        with open(global_filename, "r") as passwords_file:
            for line in passwords_file.readlines():
                index, title, username, password = line.split(":")
                view_list.append(f"{index}:\t\tTitle: {title}\tUsername: {username} \tPassword: {password}\n")
            return view_list


def add(letters=True, numbers=True, special=True, **kwargs):
    """If password_length is specified password is overwritten"""
    title: str = kwargs.get("title")
    title_column_count = title.count(":")
    username = kwargs.get("username")
    username_column_count = title.count(":")
    password = kwargs.get("password")
    password_column_count = title.count(":")
    if title_column_count == 0 and username_column_count == 0 and password_column_count == 0:
        password_length = kwargs.get("password_length")
        if password_length != None:
            if password_length.isdigit():
                password_length = int(password_length)
                password = generate_password(password_length, letters=letters, numbers=numbers, special=special)
            else:
                raise TypeError(f"expected type int, got {type(password_length)} in password_length instead")


        existing_indexes = []
        with open(global_filename, "r") as passwords_file:
            lines = passwords_file.readlines()
            for line in lines: #TODO: Find a better way to make more indexes possible (current solution goes up to index 9999)
                index_to_append: str = ""
                index_to_append += f"{line[0]}"
                if line[1].isdigit():
                    index_to_append += f"{line[1]}"
                    if line[2].isdigit():
                        index_to_append += f"{line[2]}"
                        if line[3].isdigit():
                            index_to_append += f"{line[3]}"
                existing_indexes.append(index_to_append)
        try:
            index = int(existing_indexes[-1]) + 1
        except IndexError:
            index = 1
        with open(global_filename, "a") as passwords_file:
            passwords_file.write(f"{index}:{title}:{username}:{password}\n")
        print(f"Entry added at index {index}")
        return index, password
    else:
        raise TypeError("Found column in string")



def remove(index_to_remove: int): #TODO: Find a better way to make more indexes possible (current solution goes up to index 9999)
    existing_indexes = []
    with open(global_filename, "r") as passwords_file:
        lines = passwords_file.readlines()
        for line in lines:
            index_to_append: str = ""
            index_to_append += f"{line[0]}"
            if line[1].isdigit():
                index_to_append += f"{line[1]}"
                if line[2].isdigit():
                    index_to_append += f"{line[2]}"
            existing_indexes.append(index_to_append)
    try:
        line_to_remove = existing_indexes.index(index_to_remove)
        del lines[line_to_remove]
        with open(global_filename, "w") as passwords_file:
            for line in lines:
                passwords_file.write(line)
    except ValueError:
        print("The index specified couldn't be found in the database")




def main():
    while True:
        filepath, file_found = get_filepath()
        if file_found:
            while True:
                master_password = input("Enter Master Password ['d' to enable debug]: ").lower()
                key = PasswordManagerCryptography.convert_master_password_to_key(master_password)
                if master_password == "d":
                    print("Enabling Debug Mode")
                    print("Enter password to encrypt the file with")
                    master_password = input("Enter Master Password: ")
                    key = PasswordManagerCryptography.convert_master_password_to_key(master_password)
                    PasswordManagerCryptography.encrypt_database(global_filename, key)
                    print("File encrypted")
                    print("Disabling debug mode")
                if PasswordManagerCryptography.decrypt_database(global_filename, key):
                    break
            print("Database decrypted")
            print("If program is now closed without the use of 'q to quit', the database needs to be repaired in debug mode!")
            while True:
                mode = input("Choose mode [view/add/remove/q to quit]: ").lower()
                if mode == "view":
                    view_list = view()
                    for line in view_list:
                        print(line)
                elif mode == "add":
                    title = input("Title: ")
                    username = input("Username: ")
                    password = input("Password ['G' to generate]: ")
                    if password == "G":
                        configure_password_generation = input("Configure password generation? [y/n]: ").lower()
                        if configure_password_generation == "y":
                            generate_letters = input("Enable the generation of letters? [y/n]: ").lower()
                            generate_numbers = input("Enable the generation of numbers? [y/n]: ").lower()
                            generate_special_characters = input("Enable the generation of special characters? [y/n]: ").lower()

                            generate_letters_bool: bool = False
                            generate_numbers_bool: bool = False
                            generate_special_characters_bool: bool = False

                            while not generate_letters_bool or not generate_numbers_bool or not generate_special_characters_bool:
                                if generate_letters == "y":
                                    generate_letters_bool = True
                                if generate_numbers == "y":
                                    generate_numbers_bool = True
                                if generate_special_characters == "y":
                                    generate_special_characters_bool = True
                                break

                            while True:
                                generate_password_length = input("Enter password length [8-inf]: ")
                                index, generated_password = add(title=title, username=username, password_length=generate_password_length, letters=generate_letters_bool, numbers=generate_numbers_bool, special=generate_special_characters_bool)
                                break

                        else:
                            while True:
                                generate_password_length = input("Enter password length [8-inf]: ")
                                index, generated_password = add(title=title, username=username, password_length=generate_password_length)
                                break

                    else:
                        index, generated_password = add(title=title, username=username, password=password)
                    print(f"Entry added at index {index}")
                    if generated_password != password:
                        print("Your password is set to ", generated_password)
                elif mode == "remove":
                    while True:
                        index_to_remove = input("Enter index to delete: ")
                        if index_to_remove.isdigit():
                            index_to_remove = int(index_to_remove)
                            remove(index_to_remove)
                            break
                        else:
                            print("Please enter a valid number")
                elif mode == "q":
                    PasswordManagerCryptography.encrypt_database(global_filename, PasswordManagerCryptography.convert_master_password_to_key(master_password))
                    print("Database encrypted")
                    exit("User ended the program")
                else:
                    print("Enter a valid mode")
                    continue



if __name__ == '__main__':
    main()