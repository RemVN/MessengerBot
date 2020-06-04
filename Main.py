import Config
import Menu

from SQL import SqlHelper
from Commands.CommandChat import CommandChat
from Commands.CommandExit import CommandExit
from Commands.CommandHelp import CommandHelp
from Commands.CommandTest import CommandTest
from EchoBot import EchoBot
from SQL.Models import *

EXIT = False
# client = EchoBot(Config.email, Config.pwd)
sql_connection = SqlHelper.create_connection("messenger_bot.db")


def init_commands():
    commands = Config.commands
    commands.append(CommandHelp())
    commands.append(CommandExit())
    commands.append(CommandChat())
    commands.append(CommandTest())


def get_command(command_name):
    for cmd in Config.commands:
        if cmd.command_name == command_name: return cmd
    return None


# def start_bot():
#     client.listening()

def main():
    init_commands()
    SqlHelper.fetch_data()
    # start_bot()
    Menu.start_menu()


def exit_program():
    global EXIT
    EXIT = True


if __name__ == "__main__":
    main()
