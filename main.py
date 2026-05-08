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

from utils import generate_password
from getpass import getpass


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

    add_password(website, username, password)

    print("Password stored securely.")


def view_passwords_flow():
    passwords = get_passwords()

    if not passwords:
        print("No passwords stored.")
        return

    print("\nStored Passwords:\n")

    for website, username, password in passwords:
        print(f"Website: {website}")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print("-" * 30)


def search_password_flow():
    website = input("Enter website to search: ")

    result = search_password(website)

    if result:
        website, username, password = result

        print("\nPassword Found:")
        print(f"Website: {website}")
        print(f"Username: {username}")
        print(f"Password: {password}")

    else:
        print("No matching password found.")


def delete_password_flow():
    website = input("Enter website to delete: ")

    delete_password(website)

    print("Password deleted if it existed.")


def main():
    create_table()

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