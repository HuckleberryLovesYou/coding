#############################################################
#   inspired by 'Tech wit Tim' on Youtube                   #
#   https://youtu.be/NpmFbWO6HPU?si=NUpQHy3AY0X9-qJh&t=4008 #
#############################################################

#Dependencies:
#os
#Password_Generator
#tkinter



# DO NOT USE IT TO STORE ANY IMPORTANT DATA
# NO ENCRYPTION HAPPENING HERE

import os
from PasswordGenerator import generate_password
from tkinter.filedialog import askopenfilename

global_filename: str = ""

def get_filepath():
    def check_for_file(filepath):
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
                view_list.append(f"{index}:\t\tTitle: {title}\tUsername: {username} Password: {password}\n")
            return view_list

def add(**kwargs):
    title = kwargs.get("title")
    username = kwargs.get("username")
    password = kwargs.get("password")
    password_length = kwargs.get("password_length")
    if password_length != None:
        password = generate_password(password_length)


    existing_indexes = []
    with open(global_filename, "r") as passwords_file:
        lines = passwords_file.readlines()
        for line in lines: #TODO: Starts at 1 after hitting index 10(9)
            existing_indexes.append(line[0])

    try:
        index = int(existing_indexes[-1]) + 1
    except IndexError:
        index = 1

    with open(global_filename, "a") as passwords_file:
        passwords_file.write(f"{index}:{title}:{username}:{password}\n")
    print(f"Entry added at index {index}")
    return index, password


def remove(index_to_remove: int):
    existing_indexes = []
    with open(global_filename, "r") as passwords_file:
        lines = passwords_file.readlines()
        for line in lines:
            existing_indexes.append(line[0])
    try:
        line_to_remove = existing_indexes.index(index_to_remove)
        del lines[line_to_remove]
        with open(global_filename, "w") as passwords_file:
            for line in lines:
                passwords_file.write(line)
    except ValueError:
        index_to_remove_error: str = "The index specified couldn't be found in the database"
        print(index_to_remove_error)
        return index_to_remove_error



def main():
    while True:
        filepath, file_found = get_filepath()
        if file_found:
            while True:
                mode = input("Choose mode [view/add/remove/q to quit] ").lower()
                if mode == "view":
                    view_list = view()
                    for line in view_list:
                        print(line)
                elif mode == "add":
                    title = input("Title: ")
                    username = input("Username: ")
                    password = input("Password ['G' to generate]: ")
                    if password == "G":
                        while True:
                            generate_password_length = input("Enter password length [8-inf]: ")
                            if generate_password_length.isdigit():
                                generate_password_length = int(generate_password_length)
                                if generate_password_length >= 8:
                                    index, generated_password = add(title=title, username=username, password_length=generate_password_length)
                                    break
                                else:
                                    print("Please enter a number between 8 and infinite")
                            else:
                                print("Please enter a valid number")
                    else:
                        index, generated_password = add(title=title, username=username, password=password)
                    print(f"Entry added at index {index}")
                    if generated_password != password:
                        print("Your password is set to ", generated_password)
                elif mode == "remove":
                    index_to_remove = input("Enter index to delete: ")
                    remove(index_to_remove)
                elif mode == "q":
                    exit("User ended the program")
                else:
                    print("Enter a valid mode")
                    continue



if __name__ == '__main__':
    main()