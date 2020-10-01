# -*- encoding=UTF-8 -*-


from nowstagram import app, db
from flask_script import Manager
import random
from nowstagram.models import User, Image, Comment

manager = Manager(app)


def get_image_url():
    return 'http://images.nowcoder.com/head' + str(random.randint(0, 1000)) + 'm.jpg'


@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0, 100):
        db.session.add(User('User' + str(i), 'a' + str(i)))
        for j in range(0, 3):
            db.session.add(Image(get_image_url(), i + 1))
            for k in range(0, 3):
                db.session.add(Comment('Tis is a comment' + str(k), 1 + 3 * i + j, i + 1))
    db.session.commit()

    # for i in range(0, 100):
    #     db.session.add(User('牛客' +str(i), 'a'+str(i)))
    #
    #     for j in range(0, 3): #每人发三张图
    #         db.session.add(Image(get_image_url(), i + 1))
    #         for k in range(0, 3):
    #             db.session.add(Comment('这是一条评论'+str(k), 1+3*i+j, i+1))
    # db.session.commit()

if __name__ == '__main__':
        manager.run()
