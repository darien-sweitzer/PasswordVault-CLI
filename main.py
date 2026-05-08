# create and store encrypted password vaults and retrieve them when needed
# cli interface, real encryption, sqlite databases

# main: user interaction, menus, cli

from database import (
    create_table,
    add_password,
    get_passwords,
    delete_password,
    search_password
)

from auth import (
    master_password_exists,
    save_master_password,
    verify_master_password
)

from colorama import init, Fore
import pyperclip

from utils import (
    generate_password,
    check_password_strength
)
from getpass import getpass
from logger import log_action

init(autoreset=True)

def menu():
    print("\n=== SecurePass CLI ===")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Generate Password")
    print("6. Exit")


def add_password_flow():
    website = input("Website: ")
    username = input("Username: ")

    choice = input(
        "Generate secure password? (y/n): "
    ).lower()

    if choice == "y":
        password = generate_password()
        print(f"Generated Password: {password}")
    else:
        password = getpass("Password: ")
        strength = check_password_strength(password)
        print(
            Fore.CYAN +
            f"Password Strength: {strength}"
        )
        

    add_password(website, username, password)
    log_action(f"Added password for {website}")

    print("Password stored securely.")


def view_passwords_flow():
    passwords = get_passwords()

    if not passwords:
        print(Fore.YELLOW + "No passwords stored.")
        return

    print(Fore.CYAN + "\nStored Passwords:\n")

    for website, username, password in passwords:
        print(Fore.GREEN + f"Website: {website}")
        print(Fore.WHITE + f"Username: {username}")
        print(Fore.MAGENTA + f"Password: {password}")
        print(Fore.BLUE + "-" * 30)


def search_password_flow():
    website = input("Enter website to search: ")

    result = search_password(website)

    if result:
        website, username, password = result

        print("\nPassword Found:")
        print(f"Website: {website}")
        print(f"Username: {username}")
        print(f"Password: {password}")

        copy_choice = input(
            "Copy password to clipboard? (y/n): "
        ).lower()

        if copy_choice == "y":
            pyperclip.copy(password)

            print(
                Fore.GREEN +
                "Password copied to clipboard."
            )

    else:
        print("No matching password found.")


def delete_password_flow():
    website = input("Enter website to delete: ")

    delete_password(website)
    log_action(f"Deleted password for {website}")

    print("Password deleted if it existed.")

def authenticate():
    """
    Handles master password setup and login.
    """

    if not master_password_exists():
        print("No master password found.")
        print("Create a new master password.")

        while True:
            password = getpass("New master password: ")
            confirm = getpass("Confirm password: ")

            if password != confirm:
                print("Passwords do not match.")
                continue

            if len(password) < 8:
                print(
                    "Password must be at least 8 characters."
                )
                continue

            save_master_password(password)

            print("Master password created.")
            return

    attempts = 3

    while attempts > 0:
        password = getpass("Enter master password: ")

        if verify_master_password(password):
            print("Access granted.")
            return

        attempts -= 1

        print(
            f"Incorrect password. "
            f"{attempts} attempts remaining."
        )

    print("Too many failed attempts.")
    exit()


def main():
    create_table()
    authenticate()

    while True:
        menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_password_flow()

        elif choice == "2":
            view_passwords_flow()

        elif choice == "3":
            search_password_flow()

        elif choice == "4":
            delete_password_flow()

        elif choice == "5":
            password = generate_password()

            print(f"\nGenerated Password:\n{password}")

        elif choice == "6":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()