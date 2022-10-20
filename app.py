from flask import Flask, render_template, request, redirect, url_for
import os
import datetime as dt
import pytz
import pymongo

# constants
app = Flask(__name__)
IST = pytz.timezone('Asia/Kolkata')
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# routes

from user import routes
#
mydb = myclient['portfolio_website']
M_pf_pro = mydb['pf_pro']
M_contact_form = mydb['contact_form']


def portfolio_schema(name, desc, repo_link, img_link):
    return {'name': name, 'desc': desc, 'repo_link': repo_link, 'img_link': img_link}


def contact_me(name, email, message, date, time, status='Pending'):
    return {'name': name, 'email': email, 'message': message, 'date': date, 'time': time,
            'status': status}


@app.route('/')
def home():
    projs = list(M_pf_pro.find())
    return render_template('index.html', projs=projs)


@app.route('/ele')
def elements():
    return render_template('elements.html')


@app.route('/contact-responses')
def contact_responses():
    res = list(M_contact_form.find().sort([
        ('date', pymongo.DESCENDING),
        ('time', pymongo.DESCENDING)
    ]))
    print(res)

    return render_template('contact_me_res.html', responses=res, c=len(res))


@app.route('/contact', methods=['POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        today = dt.datetime.now(IST)
        time = today.strftime('%H:%M:%S')
        date = today.strftime('%d/%m/%Y')

        d = contact_me(
            name=name,
            email=email,
            message=message,
            time=time,
            date=date
        )
        M_contact_form.insert_one(d)

        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
