import random
import string


def generate_password(length=16):
    """
    Generates a secure random password.
    """

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(
        random.choice(characters)
        for _ in range(length)
    )

    return password