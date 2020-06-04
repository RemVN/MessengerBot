import sqlite3
import Main
from sqlite3 import Error
from SQL.Models import *

users = []
groups = []
auto_replies = []


def fetch_data():
    fetch_all_users()
    fetch_all_groups()
    fetch_all_auto_reply()


def fetch_all_users():
    global users
    user_sql = "select * from fb_user"
    user_cur = Main.sql_connection.cursor()
    user_cur.execute(user_sql)
    for user_row in user_cur.fetchall():
        user = User(user_row[0], user_row[1])
        perm_sql = "select permission from permission where uid = ?"
        perm_param = ([user.uid])
        perm_cur = Main.sql_connection.cursor()
        perm_cur.execute(perm_sql, perm_param)
        for perm_row in perm_cur.fetchall():
            user.permissions.append(perm_row[0])
        users.append(user)
    print("{} users loaded from sql".format(len(users)))


def fetch_all_groups():
    global groups
    group_sql = "select * from fb_group"
    group_cur = Main.sql_connection.cursor()
    group_cur.execute(group_sql)
    for group_row in group_cur.fetchall():
        group = Group(group_row[0], group_row[1])
        groups.append(group)
    print("{} groups loaded from sql".format(len(groups)))


def fetch_all_auto_reply():
    global auto_replies
    auto_sql = "select * from auto_reply"
    auto_cur = Main.sql_connection.cursor()
    auto_cur.execute(auto_sql)
    for auto_row in auto_cur.fetchall():
        auto_reply = AutoReply(auto_row[0], auto_row[1], auto_row[2], auto_row[3], auto_row[4])
        auto_replies.append(auto_reply)
    print("{} auto reply loaded from sql".format(len(auto_replies)))


"""
SQL CONNECTION
"""


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


"""
END SQL CONNECTION
"""


def get_user(uid):
    for user in users:
        if user.uid == uid: return user
    return None


def get_group(uid):
    for group in groups:
        if group.uid == uid: return group
    return None


def get_auto_reply(from_str):
    for auto_reply in auto_replies:
        if auto_reply.from_str == from_str:
            return auto_reply
    return None


def get_auto_reply(uid):
    for auto_reply in auto_replies:
        if auto_reply.uid == uid: return auto_reply
    return None
