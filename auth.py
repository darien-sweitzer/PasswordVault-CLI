import bcrypt
import os


MASTER_PASSWORD_FILE = "master.hash"


def master_password_exists():
    """
    Checks if a master password already exists.
    """

    return os.path.exists(MASTER_PASSWORD_FILE)


def hash_password(password):
    """
    Hashes a password using bcrypt.
    """

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(
        password.encode(),
        salt
    )

    return hashed


def save_master_password(password):
    """
    Saves the hashed master password.
    """

    hashed = hash_password(password)

    with open(MASTER_PASSWORD_FILE, "wb") as file:
        file.write(hashed)


def verify_master_password(password):
    """
    Verifies entered password against stored hash.
    """

    with open(MASTER_PASSWORD_FILE, "rb") as file:
        stored_hash = file.read()

    return bcrypt.checkpw(
        password.encode(),
        stored_hash
    )