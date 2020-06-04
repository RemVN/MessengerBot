from os import system, name

import Main
from Commands.Command import Command


def print_title():
    print("MESSENGER BOT")
    print("type 'help' to show command list")


def input_command():
    command = input()
    args = command.split(" ")
    command_name = args[0]
    args = args[1::]
    # print("{} {}".format(command_name, args))
    command = Main.get_command(command_name)
    if command is None:
        print("command not found! type help to show command list")
        return
    command.handle_command(args)


def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def start_menu():
    print_title()
    while not Main.EXIT:
        input_command()
