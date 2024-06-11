from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app as app

class User:
    def __init__(self, username, userid, password):
        self.username = username
        self.userid = userid
        self.password = generate_password_hash(password)

    def save(self):
        user_collection = app.mongo['users']
        user_collection.insert_one({
            "username": self.username,
            "userid": self.userid,
            "password": self.password
        })

    @staticmethod
    def login(userid, password):
        user_collection = app.mongo['users']
        user = user_collection.find_one({"userid": userid})
        if user and check_password_hash(user['password'], password):
            return user
        return None

    @staticmethod
    def sign_out():
        pass

    @staticmethod
    def get_user_list():
        user_collection = app.mongo['users']
        return list(user_collection.find({}, {"password": 0}))

