# create and store encrypted password vaults and retrieve them when needed
# cli interface, real encryption, sqlite databases

# main: user interaction, menus, cli

from database import create_table, add_password, get_passwords
from getpass import getpass


def menu():
    print("\n=== SecurePass CLI ===")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Exit")


def main():
    create_table()

    while True:
        menu()

        choice = input("Choose an option: ")

        if choice == "1":
            website = input("Website: ")
            username = input("Username: ")

            password = getpass("Password: ")

            add_password(website, username, password)

            print("Password stored securely.")

        elif choice == "2":
            passwords = get_passwords()

            print("\nStored Passwords:\n")

            for website, username, password in passwords:
                print(f"Website: {website}")
                print(f"Username: {username}")
                print(f"Password: {password}")
                print("-" * 30)

        elif choice == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()