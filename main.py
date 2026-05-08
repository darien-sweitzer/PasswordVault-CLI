# create and store encrypted password vaults and retrieve them when needed
# cli interface, real encryption, sqlite databases

# main: user interaction, menus, cli

from database import create_table


def main():
    create_table()
    print("Database initialized successfully.")


if __name__ == "__main__":
    main()