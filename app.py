from flask import Flask, render_template
import os
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient['portfolio_website']
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

pf_pro = mydb['pf_pro']


def portfolio_schema(name, desc, repo_link, img_link):
    return {'name': name, 'desc': desc, 'repo_link': repo_link, 'img_link': img_link}


@app.route('/')
def hello_world():
    projs = list(pf_pro.find())

    return render_template('index.html',projs=projs)


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
