# Password Manager
## Usage
It can be used with GUI or only CLI. The main file is PasswordManager.py, is the file, which is producing the CLI-output and so need to be run if CLI is the wanted Output method.
The PasswordManagerGUI.py file is needed you would like to use the GUI variant. The PasswordManager.py file doesn't need the PasswordManagerGUI file if run as CLI variant, but the PasswordManagerGUI.py file indeed needs the PasswordManager.py file.

**If you don't have a .txt-database yet, you can create one by creating a .txt file in the Select File popup.
On the first time after creation you need to enter the debug mode.
After that enter the password that you want to set as a master password. After that decrypt it with the just set master password, and you will be good to go.**
# Features
## View
This is the most basic feature in a Password Manager. This is the Section you can view your database.
If the database is empty, the program will tell you.
## Add
The next feature is the add feature.
It can be used to create new passwords.
It is capable to set the title, the username, the password for each entry.
Currently, the amount of entries is limited to 10000. After that it will start overwriting existing entries.

A special feature is, that you can also generate passwords. To utilize this function, enter a 'G' into the password entry and hit enter.
After that you can enter the password length of the password to generate (8-inf).
Until now, it is not possible to specify which character it should be using and so it generates a pretty strong password.
If a password_length is specified it's going to ignore any entries in the password field (mostly exploitable in the GUI).
It will always put a new entry at the highest index + 1 and will not fill up indexes already deleted.

## Remove
The next feature is the remove feature.
It can be used to delete an entire entry specified by its index viewable in View mode.
It will not ask for a conformation.
The index will be deleted and will never be given to any entry ever again as already mentioned in the Add feature.