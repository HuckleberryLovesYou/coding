import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet



def convert_master_password_to_key(user_master_password: str): #TODO: Do some research
    """Generates a key out of master_password and salt"""
    user_master_password = user_master_password.encode()
    salt = b'\xba\x80\xa0\xfe#\xd59\xe7\xe0\rD\xecU\xa2\xe1\x80' #I guess it makes no sense to use salt, since this application is open-source anyway. Need to do some research

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(user_master_password))
    return key


def encrypt_database(filename, key):
    try:
        cipher = Fernet(key)

        with open(filename, "rb") as file:
            file_to_encrypt = file.read()

        encrpyted_file = cipher.encrypt(file_to_encrypt)


        with open(filename, "wb") as file:
            file.write(encrpyted_file)

        return True
    except:
        print("Database already encrypted or invalid Key")
        return False

def decrypt_database(filename, key):
    try:
        cipher = Fernet(key)

        with open(filename, "rb") as file:
            file_to_decrypt = file.read()

        decrypted_file = cipher.decrypt(file_to_decrypt)


        with open(filename, "wb") as file:
            file.write(decrypted_file)
        return True
    except:
        print("Database already decrypted or invalid Key")
        return False


#DEBUG
#encrypt_database("passwords.txt", convert_master_password_to_key("password"))