import pymongo
import os

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient.portfolio_website

M_pf_pro = mydb['pf_pro']
M_contact_form = mydb['contact_form']
M_users = mydb['users']


def portfolio_schema(name, desc, repo_link, img_link):
    return {'name': name, 'desc': desc, 'repo_link': repo_link, 'img_link': img_link}


def contact_me(name, email, message, date, time, status='Pending'):
    return {'name': name, 'email': email, 'message': message, 'date': date, 'time': time,
            'status': status}
