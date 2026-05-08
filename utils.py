import random
import string
import re


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

def check_password_strength(password):
    """
    Evaluates password strength.
    """

    score = 0

    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Moderate"

    return "Strong"