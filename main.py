import asyncio

from checker import check_server


def main():
    host = input("Host: ")
    username = input("Username: ")
    password = input("Password: ")

    asyncio.run(check_server(host, username, password))


if __name__ == "__main__":
    main()