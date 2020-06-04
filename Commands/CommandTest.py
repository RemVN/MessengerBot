import _thread

import Config
from Commands.Command import Command
from SQL.Models import *


def test_case_1():
    user = User("12312", "Test")
    user.insert_sql()


def test_case_2():
    _thread.start_new_thread(lambda: {
    }, ())


class CommandTest(Command):
    def __init__(self):
        super().__init__("test")

    def get_usage(self):
        return ["test <test-case> - run a test case"]

    def handle_command(self, args):
        test_case = args[0]
        if test_case == "1": test_case_1()
        if test_case == "2": test_case_2()
