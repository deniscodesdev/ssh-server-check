import argparse
import asyncio

from checker import check_server


def main():
    parser = argparse.ArgumentParser(description="SSH Server Check")

    parser.add_argument("--host", help="Server IP or hostname")
    parser.add_argument("--user", help="SSH username")
    parser.add_argument("--password", help="SSH password")

    args = parser.parse_args()

    host = args.host or input("Host: ")
    username = args.user or input("Username: ")
    password = args.password or input("Password: ")

    asyncio.run(check_server(host, username, password))


if __name__ == "__main__":
    main()