class Command:
    def __init__(self, command_name):
        self.command_name = command_name

    def get_usage(self):
        return []

    def print_all_usage(self):
        for str in self.get_usage():
            print(str)

    def print_usage(self, index):
        print("usage: {}".format(self.get_usage()[index]))

    def handle_command(self, args):
        return
