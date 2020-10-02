# -*- encoding=UTF-8 -*-


from nowstagram import app, db
from flask_script import Manager
from sqlalchemy import or_, and_
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
        db.session.add(User('User' + str(i + 1), 'a' + str(i)))
        for j in range(0, 3):
            db.session.add(Image(get_image_url(), i + 1))
            for k in range(0, 3):
                db.session.add(Comment('Tis is a comment' + str(k), 1 + 3 * i + j, i + 1))
    db.session.commit()

    print 1, User.query.all()
    print 2, User.query.get(3)
    print 3, User.query.filter_by(id=5).first()
    print 4, User.query.order_by(User.id.desc()).offset(1).limit(2).all()
    print 5, User.query.filter(User.userName.endswith('0')).limit(3).all()
    print 6, User.query.filter(or_(User.id == 88, User.id == 99)).all()
    print 7, User.query.filter(or_(User.id == 88, User.id == 99))
    print 8, User.query.filter(or_(User.id == 88, User.id == 99)).first_or_404()
    print 9, User.query.order_by(User.id.desc()).paginate(page=1, per_page=10).items
    user = User.query.get(1)
    print 10, user.images
    image = Image.query.get(1)
    print 11, image, image.user

    for i in range(50, 100, 2):
        user = User.query.get(i)
        user.userName = '[New]' + user.userName
    # for i in range(51,100,2):
    #     User.query.filter_by(User.id>50).update({'userName':'[New2]'})
    User.query.filter_by(id=51).update({'userName': '[New2]'})
    db.session.commit()

    for i in range(50, 100, 2):
        comment = Comment.query.get(i + 1)
        db.session.delete(comment)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
