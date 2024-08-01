import customtkinter
import PasswordManager

# DO NOT USE IT TO STORE ANY IMPORTANT DATA
# NO ENCRYPTION HAPPENING HERE

WIDTH, HEIGHT = 1000, 750
FILE_SELECTED: bool = False

customtkinter.set_appearance_mode("dark") #might be changed to "system" later
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry(f"{WIDTH}x{HEIGHT}")

def root_gui():
    def select_file_gui(): #File selection handled through PasswortManager.get_filepath() which uses tkinter.filedialog.askopenfilename
        def back_to_root():
            select_file_frame.destroy()
            root_gui()

        def call_get_filepath(): #if file is found, it automatically goes back to root, to check if constant changed and goes further in root_gui()
            _, file_found = PasswordManager.get_filepath()
            if file_found:
                global FILE_SELECTED
                FILE_SELECTED = True
                back_to_root()
            else:
                database_not_found_error_label = customtkinter.CTkLabel(master=select_file_frame, text="Database not found", font=("Ariel", 28))
                database_not_found_error_label.pack(side="bottom", pady=30, padx=10)


        select_file_frame = customtkinter.CTkFrame(master=root)
        select_file_frame.pack(pady=20, padx=20, fill="both", expand=True)

        select_file_button = customtkinter.CTkButton(master=select_file_frame, text="Select File...", command=call_get_filepath)
        select_file_button.pack(pady=50, padx=5)

    def remove_gui(): #TODO: Implement the entire removing feature
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



        add_title_label = customtkinter.CTkLabel(master=add_frame, text="Password Manger", font=("Ariel", 28))
        add_title_label.pack(pady=20, padx=20)

        title_entry = customtkinter.CTkEntry(master=add_frame, placeholder_text="Title", width=300)
        title_entry.pack(padx=10, pady=10)

        username_entry = customtkinter.CTkEntry(master=add_frame, placeholder_text="Username", width=300)
        username_entry.pack(padx=10, pady=10)

        password_entry = customtkinter.CTkEntry(master=add_frame, placeholder_text="Password / G to generate", width=300)
        password_entry.pack(padx=10, pady=10)




        def check_for_generate():
            def call_add_with_generate():
                password_length: int = round(password_length_slider.get())

                password_length_slider.destroy()
                password_length_slider_value_label.destroy()
                password_length_slider_intro_label.destroy()
                generate_and_add_button.destroy()

                index, password = PasswordManager.add(title=title_entry.get(), username=username_entry.get(), password_length=password_length)
                index_label = customtkinter.CTkLabel(master=add_frame, text=f"Added password at index {index}, with password {password}")
                index_label.pack(side="bottom", padx=10, pady=30)
                index_label.after(5000, index_label.destroy)
                add_entry_button.pack(padx=10, pady=10)

            def call_add():
                index, password = PasswordManager.add(title=title_entry.get(), username=username_entry.get(), password=password_entry.get())
                index_label = customtkinter.CTkLabel(master=add_frame, text=f"Added password at index {index}")
                index_label.pack(side="bottom", padx=10, pady=30)
                index_label.after(5000, index_label.destroy)


            password_to_check = password_entry.get()
            if password_to_check[0] == "G":
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


        add_entry_button = customtkinter.CTkButton(master=add_frame, text="Add Entry", command=check_for_generate)
        add_entry_button.pack()

    if FILE_SELECTED:
        root_frame = customtkinter.CTkFrame(master=root)
        root_frame.pack(pady=20, padx=20, fill="both", expand=True)

        quit_button = customtkinter.CTkButton(master=root_frame, text="Quit", command=quit)
        quit_button.pack(anchor="nw", padx=5, pady=5)

        title_label = customtkinter.CTkLabel(master=root_frame, text="Password Manger", font=("Ariel", 28))
        title_label.pack(pady=20, padx=20)

        view_button = customtkinter.CTkButton(root_frame, text="View", command=view_gui) #leads to view_gui()
        add_button = customtkinter.CTkButton(root_frame, text="Add", command=add_gui) #leads to add_gui()
        remove_button = customtkinter.CTkButton(root_frame, text="Remove", command=remove_gui) #leads to remove_gui()

        view_button.pack(side="left", expand=True, padx=10)
        add_button.pack(side="left", expand=True, padx=10)
        remove_button.pack(side="left", expand=True, padx=10)
    else:
        select_file_gui()


root_gui() # calls the root_gui(), which leads to all other guis using other buttons, created in root_gui()

root.mainloop()