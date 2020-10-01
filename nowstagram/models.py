# -*- encoding=UTF-8 -*-

from nowstagram import db
import random

class  Image(db.Model)
    id = db.Column(db.Integer, primary_key=True ,autoincrement=True)
    user_id =

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(80), unique=True)
    passWord = db.Column(db.String(32))
    head_url = db.Column(db.String(256))

    def __init__(self, userName, passWord):
        self.userName = userName
        self.passWord = passWord
        random_random = random.randint(0, 1000)
        self.head_url = 'https://image.nowcoder.com/head/' + str(random_random) + 'm.jpg'

    def __repr__(self):
        return '<User %d %s>' % (self.id, self.userName)
