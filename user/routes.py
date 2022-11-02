from flask import Flask
from app import app
from user.models import User


@app.route('/user/signup/', methods=['POST'])
def signUp():
    return User().signUp()


@app.route('/user/signout/')
def signOut():
    return User().signOut()


@app.route('/user/login/', methods=['POST'])
def logIn():
    return User().logIn()


