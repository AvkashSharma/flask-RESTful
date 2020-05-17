class User:
    def __init__(self, _id, username, password):
        self.id = _id     # used _id because id is a keyword in python
        self.username = username
        self.password = password
