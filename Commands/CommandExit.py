from Commands.Command import Command
import Main

class CommandExit(Command):
    def __init__(self):
        super().__init__("exit")

    def get_usage(self):
        return ["exit - terminate bot"]

    def handle_command(self, args):
        Main.exit_program()