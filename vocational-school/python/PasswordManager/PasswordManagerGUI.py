#############################################################
#   inspired by 'NeuralNine' on Youtube                     #
#   https://youtu.be/iM3kjbbKHQU?si=5JzFwVoErJ51FYlz        #
#############################################################


#Dependencies:
#PasswordGenerator.py
#PasswordManagerCryptography.py
#customtkinter # can be installed using 'pip install customtkinter'

# DO NOT USE IT TO STORE ANY IMPORTANT DATA
# THIS IS JUST A FUN PROJECT NOT MEANT TO BE USED
from time import sleep
import customtkinter
import PasswordManager
import PasswordManagerCryptography

WIDTH, HEIGHT = 1000, 750
FILE_SELECTED: bool = False
DECRYPTED: bool = False
KEY = b""

FILENAME = ""

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry(f"{WIDTH}x{HEIGHT}")

def root_gui():
    def select_file_gui(): #File selection handled through PasswortManager.get_filepath() which uses tkinter.filedialog.askopenfilename
        def back_to_root():
            select_file_frame.destroy()
            master_password_gui()

        def call_get_filepath(): #if file is found, it automatically goes back to root, to check if constant changed and goes further in root_gui()
            global FILENAME
            global_filename, file_found = PasswordManager.get_filepath()
            FILENAME = global_filename
            if file_found:
                global FILE_SELECTED
                FILE_SELECTED = True
                back_to_root()
            else:
                database_not_found_error_label = customtkinter.CTkLabel(master=select_file_frame, text="Database not found", font=("Ariel", 28))
                database_not_found_error_label.pack(side="bottom", pady=30, padx=10)

        select_file_frame = customtkinter.CTkFrame(master=root)
        select_file_frame.pack(pady=20, padx=20, fill="both", expand=True)

        title_label = customtkinter.CTkLabel(master=select_file_frame, text="Password Manger", font=("Ariel", 28))
        title_label.pack(pady=20, padx=20)

        select_file_button = customtkinter.CTkButton(master=select_file_frame, text="Select File...", command=call_get_filepath)
        select_file_button.pack(pady=50, padx=5)



    def master_password_gui():
        def debug():
            print("Enabled Debug Mode")
            master_password_frame.destroy()
            debug_frame = customtkinter.CTkFrame(master=root)
            debug_frame.pack(pady=20, padx=20, fill="both", expand=True)

            def call_debug_encrypt():
                global KEY
                KEY = PasswordManagerCryptography.convert_master_password_to_key(first_encrypt_password_password_entry.get())
                PasswordManagerCryptography.encrypt_database(FILENAME, KEY)
                back_to_master_password()


            def back_to_master_password():
                debug_frame.destroy()
                master_password_gui()

            def check_passwords(*args):
                first_password = first_encrypt_password_password_entry.get()
                second_password = second_encrypt_password_password_entry.get()
                if first_password != "" and second_password != "":
                    if first_password == second_password:
                        encrypt_button_debug.configure(state="normal")
                    else:
                        encrypt_button_debug.configure(state="disabled")
                debug_frame.after(100, check_passwords)

            back_debug_button = customtkinter.CTkButton(master=debug_frame, text="< Back", command=back_to_master_password)
            back_debug_button.pack(anchor="nw", pady=5, padx=5)

            title_debug_label = customtkinter.CTkLabel(master=debug_frame, text="Password Manger", font=("Ariel", 28))
            title_debug_label.pack(pady=20, padx=20)

            first_encrypt_password_password_entry = customtkinter.CTkEntry(master=debug_frame, placeholder_text="Encryption Password", show="*")
            first_encrypt_password_password_entry.pack(padx=10, pady=10)

            second_encrypt_password_password_entry = customtkinter.CTkEntry(master=debug_frame, placeholder_text="Retype Password", show="*")
            second_encrypt_password_password_entry.pack(padx=10, pady=10)

            encrypt_button_debug = customtkinter.CTkButton(master=debug_frame, text="Encrypt", state="disabled", command=call_debug_encrypt)
            encrypt_button_debug.pack(padx=10, pady=10)

            debug_warning_label = customtkinter.CTkLabel(master=debug_frame, text="Only use debug, if you closed the program without the use of quit. Otherwise your database will be corrupted")
            debug_warning_label.pack(side="bottom", padx=10, pady=30)
            debug_warning_label.after(15000, debug_warning_label.destroy)

            check_passwords()





        def back_to_root():
            master_password_frame.destroy()
            select_file_gui()
            global FILE_SELECTED
            FILE_SELECTED = False

        def call_decrypt():
            global KEY
            KEY = PasswordManagerCryptography.convert_master_password_to_key(master_password_entry.get())
            if PasswordManagerCryptography.decrypt_database(FILENAME, KEY):
                global DECRYPTED
                DECRYPTED = True
                master_password_frame.destroy()
                root_gui()
            else: #TODO: Get the debug_button at the same height as back_button
                master_password_entry.forget()
                decrypt_button.forget()
                title_label_master_password.forget()
                back_button_master_password.forget()

                back_button = customtkinter.CTkButton(master=master_password_frame, text="< Back", command=back_to_root)
                back_button.pack(side="left", padx=5, pady=5, anchor="n")

                encrypt_database_instead_button = customtkinter.CTkButton(master=master_password_frame, text="Debug", command=debug)
                encrypt_database_instead_button.pack(side="right", padx=5, pady=5, anchor="n")


                title_label_master_password.pack(pady=20, padx=20)
                master_password_entry.pack(padx=10, pady=10)
                decrypt_button.pack(padx=10, pady=10)


                decrypt_error_label = customtkinter.CTkLabel(master=master_password_frame, text="Error:\nDatabase already decrypted or invalid Key")
                decrypt_error_label.pack(side="bottom", padx=10, pady=30)
                decrypt_error_label.after(1500, decrypt_error_label.destroy)

        master_password_frame = customtkinter.CTkFrame(master=root)
        master_password_frame.pack(pady=20, padx=20, fill="both", expand=True)

        back_button_master_password = customtkinter.CTkButton(master=master_password_frame, text="< Back", command=back_to_root)
        back_button_master_password.pack(anchor="nw", padx=5, pady=5)

        title_label_master_password = customtkinter.CTkLabel(master=master_password_frame, text="Password Manger", font=("Ariel", 28))
        title_label_master_password.pack(pady=20, padx=20)

        master_password_entry = customtkinter.CTkEntry(master=master_password_frame, placeholder_text="Master password", show="*")
        master_password_entry.pack(padx=10, pady=10)

        decrypt_button = customtkinter.CTkButton(master=master_password_frame, text="Decrypt", command=call_decrypt)
        decrypt_button.pack(padx=10, pady=10)



    def remove_gui():
        def call_remove():
            try:
                index_to_remove: int = index_to_remove_entry.get()
                remove_response = PasswordManager.remove(index_to_remove)
                if remove_response != None:
                    index_remove_error_label = customtkinter.CTkLabel(master=remove_frame, text=f"{remove_response}")
                    index_remove_error_label.pack(side="bottom", padx=10, pady=30)
                    index_remove_error_label.after(1500, index_remove_error_label.destroy)
                else:
                    index_to_remove_label = customtkinter.CTkLabel(master=remove_frame, text=f"Removed index: {index_to_remove}")
                    index_to_remove_label.pack(side="bottom", padx=10, pady=30)
                    index_to_remove_label.after(1500, index_to_remove_label.destroy)
            except:
                pass

        root_frame.destroy()
        remove_frame = customtkinter.CTkFrame(master=root)
        remove_frame.pack(pady=20, padx=20, fill="both", expand=True)

        def back_to_root():
            remove_frame.destroy()
            root_gui()

        back_add_button = customtkinter.CTkButton(master=remove_frame, text="< Back", command=back_to_root)
        back_add_button.pack(anchor="nw", pady=5, padx=5)

        remove_title_label = customtkinter.CTkLabel(master=remove_frame, text="Password Manger", font=("Ariel", 28))
        remove_title_label.pack(pady=20, padx=20)

        index_to_remove_entry = customtkinter.CTkEntry(master=remove_frame, placeholder_text="Index to remove")
        index_to_remove_entry.pack(padx=10, pady=10)

        remove_index_button = customtkinter.CTkButton(master=remove_frame, text="Remove Index", command=call_remove)
        remove_index_button.pack(padx=10, pady=10)


    def view_gui():
        root_frame.destroy()
        view_frame = customtkinter.CTkScrollableFrame(master=root)
        view_frame.pack(pady=20, padx=20, fill="both", expand=True)

        def back_to_root():
            view_frame.pack_forget() #doesn't use .destroy(), because there is a bug, which makes using .destroy method on scrollable frames useless
            root_gui()

        back_add_button = customtkinter.CTkButton(master=view_frame, text="< Back", command=back_to_root)
        back_add_button.pack(anchor="nw", pady=5, padx=5)

        view_title_label = customtkinter.CTkLabel(master=view_frame, text="Password Manger", font=("Ariel", 28))
        view_title_label.pack(pady=20, padx=20)

        lines = len(PasswordManager.get_all_indices())
        show_total_lines_label = customtkinter.CTkLabel(master=view_frame, text=f"Total lines: {lines}", fg_color="transparent")
        show_total_lines_label.pack(anchor="ne", pady=30, padx=20)

        view_list = PasswordManager.view()

        for element in view_list:
            element_label = customtkinter.CTkLabel(master=view_frame, text=f"{element}")
            element_label.pack(anchor="nw", padx=8, pady=8)

    def add_gui():
        root_frame.destroy()
        add_frame = customtkinter.CTkFrame(master=root)
        add_frame.pack(pady=20, padx=20, fill="both", expand=True)

        def back_to_root():
            add_frame.destroy()
            root_gui()

        back_add_button = customtkinter.CTkButton(master=add_frame, text="< Back", command=back_to_root)
        back_add_button.pack(anchor="nw", pady=5, padx=5)


        def check_for_generate():
            def call_add_with_generate():
                # is used to add a new entry with password generation
                password_length: int = round(password_length_slider.get())

                password_length_slider.destroy()
                password_length_slider_value_label.destroy()
                password_length_slider_intro_label.destroy()
                generate_and_add_button.destroy()

                index, password = PasswordManager.add(title=title_entry.get(), username=username_entry.get(), password_length=password_length)
                index_label = customtkinter.CTkLabel(master=add_frame, text=f"Added password at index {index}, with password {password}")
                index_label.pack(side="bottom", padx=10, pady=30)
                index_label.after(5000, index_label.destroy)

                sleep(2)
                back_to_root()

            def call_add():
                # is used to add a new entry without password generation
                index, password = PasswordManager.add(title=title_entry.get(), username=username_entry.get(), password=password_entry.get())
                index_label = customtkinter.CTkLabel(master=add_frame, text=f"Added password at index {index}")
                index_label.pack(side="bottom", padx=10, pady=30)
                index_label.after(5000, index_label.destroy)


            password_to_check = password_entry.get()
            if password_to_check[0] == "G":
                password_entry.destroy()
                add_entry_button.pack_forget()
                password_length_slider_value = customtkinter.IntVar()
                password_length_slider_intro_label = customtkinter.CTkLabel(master=add_frame, text="Password Length:")
                password_length_slider_intro_label.pack(padx=10, pady=2)
                password_length_slider_value_label = customtkinter.CTkLabel(master=add_frame, textvariable=password_length_slider_value)
                password_length_slider_value_label.pack(padx=10, pady=10)
                password_length_slider = customtkinter.CTkSlider(master=add_frame, from_=8, to=50, variable=password_length_slider_value)
                password_length_slider.pack(padx=10, pady=10)
                password_length_slider.set(20)

                generate_and_add_button = customtkinter.CTkButton(master=add_frame, text="Generate and add entry", command=call_add_with_generate)
                generate_and_add_button.pack()
            else:
                call_add()

        add_title_label = customtkinter.CTkLabel(master=add_frame, text="Password Manger", font=("Ariel", 28))
        add_title_label.pack(pady=20, padx=20)

        title_entry = customtkinter.CTkEntry(master=add_frame, placeholder_text="Title", width=300)
        title_entry.pack(padx=10, pady=10)

        username_entry = customtkinter.CTkEntry(master=add_frame, placeholder_text="Username", width=300)
        username_entry.pack(padx=10, pady=10)

        password_entry = customtkinter.CTkEntry(master=add_frame, placeholder_text="Password / G to generate", width=300)
        password_entry.pack(padx=10, pady=10)

        add_entry_button = customtkinter.CTkButton(master=add_frame, text="Add Entry", command=check_for_generate)
        add_entry_button.pack()


    if FILE_SELECTED:
        if DECRYPTED:
            def call_quit():
                PasswordManagerCryptography.encrypt_database(FILENAME, KEY)
                print("Database encrypted")
                exit("User ended the program")

            root_frame = customtkinter.CTkFrame(master=root)
            root_frame.pack(pady=20, padx=20, fill="both", expand=True)

            quit_button = customtkinter.CTkButton(master=root_frame, text="Quit", command=call_quit)
            quit_button.pack(anchor="nw", padx=5, pady=5)

            title_label = customtkinter.CTkLabel(master=root_frame, text="Password Manger", font=("Ariel", 28))
            title_label.pack(pady=20, padx=20)

            view_button = customtkinter.CTkButton(root_frame, text="View", command=view_gui)  # leads to view_gui()
            add_button = customtkinter.CTkButton(root_frame, text="Add", command=add_gui)  # leads to add_gui()
            remove_button = customtkinter.CTkButton(root_frame, text="Remove", command=remove_gui)  # leads to remove_gui()

            view_button.pack(side="left", expand=True, padx=10)
            add_button.pack(side="left", expand=True, padx=10)
            remove_button.pack(side="left", expand=True, padx=10)
    else:
        select_file_gui()


root_gui() # calls the root_gui(), which leads to all other guis using other buttons, created in root_gui()

root.mainloop()