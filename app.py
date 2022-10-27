import random
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, abort, jsonify
import os
import datetime as dt
import pytz

# constants
app = Flask(__name__)
IST = pytz.timezone('Asia/Kolkata')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# database
from mydb.db import *

# routes
from user import routes


# decorators
def loggedin(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session['logged_in']:
            return f(*args, *kwargs)
        else:
            print('Log in please')
            return redirect('/')

    return wrap


def admin_only(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session['logged_in']:
            if session['user']['admin']:
                return f(*args, *kwargs)
            else:
                return abort(403)
        else:
            print('Log in please')
            return redirect('/')

    return wrap


@app.route('/')
def home():
    projs = list(M_pf_pro.find())
    random.shuffle(projs)

    return render_template('index.html', projs=projs[:6])


@app.route('/ele/')
def elements():
    return render_template('elements.html')


@app.route('/contact-responses/')
@admin_only
def contact_responses():
    res = list(M_contact_form.find().sort([
        ('date', pymongo.DESCENDING),
        ('time', pymongo.DESCENDING)
    ]))

    return render_template('contact_me_res.html', responses=res, c=len(res))


@app.route('/contact/', methods=['POST'])
def contact_form():
    d = session.get('ctf', '')
    today = dt.datetime.now()
    print(d)
    time = today.strftime('%H:%M:%S')
    date = today.strftime('%d/%m/%Y')

    def send_message():
        e = contact_me(
            name=request.form.get('name'),
            email=request.form.get('email'),
            message=request.form.get('message'),
            time=time,
            date=date
        )
        M_contact_form.insert_one(e)

    if len(d) > 0:
        d = dt.datetime.strptime(d, '%H:%M:%S - %d/%m/%Y')
        delta = today - d
        if delta.seconds > 12 * 3600:
            send_message()
            session['ctf'] = today.strftime('%H:%M:%S - %d/%m/%Y')
            return jsonify({'msg': "message sent"}), 200
        else:
            return jsonify({'error': "You can send message once every 12 hour"}), 400

    else:
        send_message()
        session['ctf'] = today.strftime('%H:%M:%S - %d/%m/%Y')
        return jsonify({'msg': "message sent"}), 200


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/signup/')
def signupf():
    return render_template('signup.html')


@app.route('/dashboard/')
@loggedin
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
