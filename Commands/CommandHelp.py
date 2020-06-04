import Config
from Commands.Command import Command


class CommandHelp(Command):
    def __init__(self):
        super().__init__("help")

    def get_usage(self):
        return ["help - show help"]

    def handle_command(self, args):
        for command in Config.commands:
            command.print_all_usage()
