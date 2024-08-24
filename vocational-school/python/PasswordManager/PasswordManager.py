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

from os.path import exists
from PasswordGenerator import generate_password
from tkinter.filedialog import askopenfilename
import PasswordManagerCryptography
import argparse

global_filename: str = ""

def get_filepath(): #let the user select a .txt-file and writes it into global_filename
    def check_for_file(filepath, set_global_filename=False): #checks if file actually exists (might not be needed)
        if exists(filepath):
            print("Database found")
            return True
        else:
            print("No such database in directory")
            return False
    global global_filename
    global_filename = askopenfilename(title="Select database or create a new one and use debug mode after that:", filetypes=[("Text files" , "*.txt")])
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
        line_to_remove = existing_indexes.index(str(index_to_remove))
        del lines[line_to_remove]
        with open(global_filename, "w") as passwords_file:
            for line in lines:
                passwords_file.write(line)

        print("Index removed successfully")
    except ValueError:
        print("The index specified couldn't be found in the database")



def main():
    def encrypt_and_quit():
        PasswordManagerCryptography.encrypt_database(global_filename, PasswordManagerCryptography.convert_master_password_to_key(master_password))
        print("Database encrypted")
        exit("User ended the program")


    cli_args_given: bool = False
    try:
        parser = argparse.ArgumentParser(description="Password Manager shortcuts\nCommand example: python PasswordManager.py --master-password password --add --title test --username test --length 8")
        parser.add_argument("-m", "--master-password", required=True, action="store", dest="master_password", type=str, help="Enter Master Password for password database")
        parser.add_argument("-v", "--view", action="store_true", dest="view_boolean", help="Used to set the mode to view and view database [Needs --master-password]", required=False)
        parser.add_argument("-a", "--add", action="store_true", dest="add_boolean", help="Used to set the mode to add and add a new entry from database [Needs --master-password]", required=False)
        parser.add_argument("-r", "--remove", action="store_true", dest="remove_boolean", help="Used to set the mode to remove and remove a entry from database [Needs --master-password]", required=False)
        parser.add_argument("-i", "--index", action="store", dest="index", help="Set index in database to delete [Needs --remove]", type=int, required=False)
        parser.add_argument("-t", "--title", action="store", dest="title", help="Set title of new entry [Needs --add]", type=str, required=False)
        parser.add_argument("-u", "--username", action="store", dest="username", help="Set username of new entry [Needs --add]", type=str, required=False)
        parser.add_argument("-p", "--password", action="store", dest="password", help="Set password of new entry [Needs --add, except --generate-password is specified]", type=str, required=False)
        parser.add_argument("-g", "--generate-password", action="store_true", dest="generate_password_boolean", help="Specify this to enable password generation [Needs --add]", required=False)
        parser.add_argument("-l", "--length", action="store", dest="length", help="Set the length for password generation for new entry [Needs --generate-password]", type=str, required=False)
        parser.add_argument("-d", "--debug", action="store_true", dest="debug", help="Specify this to enable debug mode [Needs --master-password]", required=False)

        args = parser.parse_args()

        cli_args_given = True
        print(args)

    except:
        print("No arguments found\nUsing interactiv mode instead")
    while True:
        filepath, file_found = get_filepath()
        if file_found:
            while True:
                if cli_args_given:
                    master_password = args.master_password
                else:
                    master_password = input("Enter Master Password ['d' to enable debug]: ").lower()
                key = PasswordManagerCryptography.convert_master_password_to_key(master_password)
                if cli_args_given:
                    if args.debug:
                        print("Enabling Debug Mode")
                        key = PasswordManagerCryptography.convert_master_password_to_key(args.master_password)  # needed because of new password entry
                        PasswordManagerCryptography.encrypt_database(global_filename, key)
                        print("File encrypted")
                        print("Disabling debug mode")
                        encrypt_and_quit()
                else:
                    if master_password == "d":
                        print("Enabling Debug Mode")
                        print("Enter password to encrypt the file with")
                        master_password = input("Enter Master Password: ")
                        key = PasswordManagerCryptography.convert_master_password_to_key(master_password) #needed because of new password entry
                        PasswordManagerCryptography.encrypt_database(global_filename, key)
                        print("File encrypted")
                        print("Disabling debug mode")
                if PasswordManagerCryptography.decrypt_database(global_filename, key):
                    break
            print("Database decrypted")
            if not cli_args_given:
                print("If program is now closed without the use of 'q to quit', the database needs to be repaired in debug mode!")
            while True:
                if cli_args_given:
                    if args.view_boolean:
                        mode = "view"
                    elif args.add_boolean:
                        mode = "add"
                    elif args.remove_boolean:
                        mode = "remove"
                    else:
                        print("No mode specified")
                        quit()
                else:
                    mode = input("Choose mode [view/add/remove/q to quit]: ").lower()

                if mode == "view":
                    view_list = view()
                    for line in view_list:
                        print(line)
                    if cli_args_given:
                        encrypt_and_quit()
                elif mode == "add":
                    if cli_args_given:
                        if args.generate_password_boolean:
                            title = args.title
                            username = args.username
                            password = "G" #spoof that the password input was "G" to enter password generation, so fewer code changes needed
                        else:
                            title = args.title
                            username = args.username
                            password = args.password
                    else:
                        title = input("Title: ")
                        username = input("Username: ")
                        password = input("Password ['G' to generate]: ")
                    if password == "G":
                        if cli_args_given:
                            configure_password_generation = "n" #spoof that there is no configuration for password generation wanted
                        else:
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
                                if cli_args_given:
                                    generate_password_length = args.length
                                else:
                                    generate_password_length = input("Enter password length [8-inf]: ")

                                index, generated_password = add(title=title, username=username, password_length=generate_password_length)
                                break


                    else:
                        index, generated_password = add(title=title, username=username, password=password)
                    if generated_password != password:
                        print("Your password is set to ", generated_password)
                    if cli_args_given:
                        encrypt_and_quit()

                elif mode == "remove":
                    if cli_args_given:
                        index_to_remove = str(args.index)
                    else:
                        index_to_remove = input("Enter index to delete: ")

                    if index_to_remove.isdigit():
                        index_to_remove = int(index_to_remove)
                        remove(index_to_remove)
                    else:
                        print("Please enter a valid number")

                    if cli_args_given:
                        encrypt_and_quit()

                elif mode == "q":
                    encrypt_and_quit()

                else:
                    print("Enter a valid mode")
                    if cli_args_given:
                        encrypt_and_quit()
                    else:
                        continue



if __name__ == '__main__':
    main()