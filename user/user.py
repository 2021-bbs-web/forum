class User:
    max_id = 0

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.email = ""
        self.uid = User.max_id
        User.max_id += 1
        self.token = ""
