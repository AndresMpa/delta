from getpass import getpass
import os


def greeter() -> tuple:
    os.system('clear')

    username = input("Username for username@username: ")
    password = getpass("Password for @username: ")

    return (username, password)


def conection_accepted() -> None:
    os.system('clear')
    print('''
     _    _      _                          _
    | |  | |    | |                        | |
    | |  | | ___| | ___ ___  _ __ ___   ___| |
    | |/\\| |/ _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ |
    \\  /\\  /  __/ | (_| (_) | | | | | |  __/_|
     \\/  \\/ \\___|_|\\___\\___/|_| |_| |_|\\___(_)
    ''')


def refuse_connection() -> None:
    os.system('clear')
    print('''
         ____ __ _      __   _     _   __             __      __           ____                      __
       _/_/ //_/(_)____/ /__| |   / | / /___     ____/ /___ _/ /_____ _   / __/___  __  ______  ____/ /
      / // ,<  / / ___/ //_// /  /  |/ / __ \\   / __  / __ `/ __/ __ `/  / /_/ __ \\/ / / / __ \\/ __  /
     / // /| |/ / /__/ ,<  / /  / /|  / /_/ /  / /_/ / /_/ / /_/ /_/ /  / __/ /_/ / /_/ / / / / /_/ /
    / //_/ |_/_/\\___/_/|_|/_/  /_/ |_/\\____/   \\__,_/\\__,_/\\__/\\__,_/  /_/  \\____/\\__,_/_/ /_/\\__,_/
    |_|                 /_/
    ''')
