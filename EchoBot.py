import _thread
import time

from fbchat import Client
from fbchat.models import *


class EchoBot(Client):
    # def __init__(self, email, password):
    #     self.email = email;
    #     self.password = password;
    def onMessage(
            self,
            mid=None,
            author_id=None,
            message=None,
            message_object=None,
            thread_id=None,
            thread_type=None,
            ts=None,
            metadata=None,
            msg=None,
            **kwargs
    ):
        # self.markAsDelivered(thread_id, message_object.uid)
        # self.markAsRead(thread_id)
        # print(message_object)

        # if(thread_id == self.uid) return
        if thread_type == ThreadType.USER:
            print("{} -> Bot: {}".format(message_object.author, message_object.text))
        else:
            print("{} -> {}: {}".format(message_object.author, thread_id, message_object.text))

    # def start(self):
    #     super().__init__(self.email, self.password)

    def listening(self):
        print("EchoBot listening")
        _thread.start_new_thread(self.listen, ())
