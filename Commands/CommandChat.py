from fbchat.models import *

import Main
from Commands.Command import Command
from Util import StringUtil


class CommandChat(Command):
    def __init__(self):
        super().__init__("chat")

    def get_usage(self):
        return ["chat <thread-id> <message> - send a message to the thread"]

    def handle_command(self, args):
        if len(args) < 2:
            self.print_all_usage()
            return
        thread_id = args[0]
        message = StringUtil.args_to_string(args, 1)
        client = Main.client
        print(thread_id + " - " + message)
        client.sendMessage(message, thread_id, ThreadType.USER)
        print("message sent")