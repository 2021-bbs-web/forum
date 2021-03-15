import User


class UserManager(object):

    def __init__(self):
        self.user_num = 0
        self.users = dict()

    def get_user_num(self):
        return self.user_num

    def add_user(self, user: User):
        self.users[user.uid] = user
        self.user_num += 1
