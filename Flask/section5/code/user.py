import sqlite3


class User:
    def __init__(self, _id, username, password):
        self.id = _id     # used _id because id is a keyword in python
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        # cls means current class which is user as opposed to hard coding the class name
        # set-up a connection
        connection = sqlite3.connect('data.db')
        # set up curson required to run the command
        cursor = connection.cursor()

        query = "SELECT * from users where username = ?"
        result = cursor.execute(query, (username,))
        # get the first row
        row = result.fetchone()
        if row:
            # if row is not null the create a user object with the data from that row
            user = cls(*row)  # same as user = cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users where id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user