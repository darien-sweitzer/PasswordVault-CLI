# handles encryption and decryption of passwords

from cryptography.fernet import Fernet
import os


KEY_FILE = "secret.key"


def generate_key():
    """
    Generates and saves an encryption key.
    """

    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Loads the encryption key from file.
    """

    if not os.path.exists(KEY_FILE):
        generate_key()

    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


key = load_key()
cipher = Fernet(key)


def encrypt_password(password):
    """
    Encrypts a password string.
    """

    encrypted = cipher.encrypt(password.encode())
    return encrypted.decode()


def decrypt_password(encrypted_password):
    """
    Decrypts an encrypted password string.
    """

    decrypted = cipher.decrypt(encrypted_password.encode())
    return decrypted.decode()