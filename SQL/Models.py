import Main


class User:
    def __init__(self, uid, name=""):
        self.uid = uid
        self.name = name
        self.permissions = []

    def insert_sql(self):
        sql = "insert into fb_user(uid,name) values (?,?)"
        param = (self.uid, self.name)
        cur = Main.sql_connection.cursor()
        cur.execute(sql, param)
        print("added user {} to sql ({})".format(self.uid, cur.lastrowid))
        Main.sql_connection.commit()
        return cur.lastrowid


class Group:
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name


class AutoReply:
    def __init__(self, uid, uid_group, uid_user, from_str, to_str):
        self.uid = uid
        self.uid_group = uid_group
        self.uid_user = uid_user
        self.from_str = from_str
        self.to_str = to_str
