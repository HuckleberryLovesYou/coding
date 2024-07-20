#############################################################
#   inspired by 'Tech wit Tim' on Youtube                   #
#   https://youtu.be/NpmFbWO6HPU?si=NUpQHy3AY0X9-qJh&t=4008 #
#############################################################

# DO NOT USE IT TO STORE ANY IMPORTANT DATA
# NO ENCRYPTION HAPPENING HERE

import os

global_filename: str = "passwords.txt"

def build_filepath():
    global global_filename
    current_dir: str = os.path.dirname(os.path.realpath(__file__))
    print(f"Please ensure that your database is in the following directory: '{current_dir}'")
    filename_input: str = input(f"Please enter your name of the database file [default:'{global_filename}'] ")
    if filename_input != "":
        global_filename = filename_input
    filepath: str = rf"{current_dir}\{global_filename}"
    return filepath


def check_for_file(filepath):
    if os.path.exists(filepath):
        print("Database found")
        return True
    else:
        print("No such database in directory")
        return False


def create_file(filepath):
    user_input_create_database = input("Do you want to create a new database instead [y/n]").lower()
    if user_input_create_database == "y":
        open(filepath, 'a').close()




def count_lines():
    with open(global_filename, "r") as passwords_file:
        amount_of_lines: int = 0
        for _ in passwords_file.readlines():
            amount_of_lines += 1
        return amount_of_lines


def view():
    if count_lines() == 0:
        print("There are no entries in your database")
    else:
        with open(global_filename, "r") as passwords_file:
            for line in passwords_file.readlines():
                index, title, username, password = line.split(":")
                print(f"{index}:\t\tTitle: {title}\tUsername: {username} Password: {password}\n")

def add():
    title = input("Title: ")
    username = input("Username: ")
    password = input("Password: ")

    existing_indexes = []
    with open(global_filename, "r") as passwords_file:
        lines = passwords_file.readlines()
        for line in lines:
            existing_indexes.append(line[0])
    try:
        index = int(existing_indexes[-1]) + 1
    except IndexError:
        index = 1

    with open(global_filename, "a") as passwords_file:
        passwords_file.write(f"{index}:{title}:{username}:{password}\n")
    print(f"Entry added at index {index}")


def remove(index_to_remove):
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
        print("The index specified couldn't be found in the database")



def main():
    while True:
        filepath = build_filepath()
        if check_for_file(filepath):
            while True:
                mode = input("Choose mode [view/add/remove] ").lower()
                if mode == "view":
                    view()
                elif mode == "add":
                    add()
                elif mode == "remove":
                    index_to_remove = input("Enter index to delete: ")
                    remove(index_to_remove)
                else:
                    print("Enter a valid mode")
                    continue
        else:
            create_file(filepath)
            break



if __name__ == '__main__':
    main()