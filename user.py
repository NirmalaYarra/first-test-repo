import sqlite3

class User:
    def __init__(self,_id,username,password):
        self._id = _id
        self.username = username
        self.password = password
    @classmethod
    def find_user_by_name(cls,username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "select * from users where username=?"
        result = cursor.execute(query,(username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            return None
        return user

    @classmethod
    def find_user_by_id(cls, _id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "select * from users where id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            return None
        return user

