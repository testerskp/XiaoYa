#!/usr/bin/python  
# -*-coding:utf-8-*-
from app import db


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), unique=False)
    phone = db.Column(db.Integer, unique=False)
    nickname = db.Column(db.String(80), unique=False)

    def __repr__(self):
        user = ''
        user += 'name: {name}, password: {password}, phone: {phone}'.format(name=self.name, password=self.password,
                                                                            phone=self.phone)
        return user


def create_user(name, password, phone="", nickname=""):
    user = User(name=name, password=password, phone=phone, nickname=nickname)
    db.session.add(user)
    try:
        db.session.commit()
    except BaseException:
        return 0
    else:
        return user.id


def query_user(name):
    user_msg = User.query.filter_by(name=name).first()
    return user_msg


if __name__ == "__main__":

    # print(create_user('1', 1, "123", "123"))
    login("222","123")


