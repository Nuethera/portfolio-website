from flask import Flask, jsonify, request, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from mydb.db import *
import uuid

M_users = mydb['users']


class User:

    def start_session(self, user):
        del user['password']
        del user['ObjectID']
        session['logged_in'] = True
        session['user'] = user

        return jsonify({'success': "authorisation successful"}), 200

    def signUp(self):
        user = {
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8),
            "totp_secret": "",
            "two_fac": False,
            "admin": False
        }

        if M_users.find_one({'email': user['email']}):
            return jsonify({"error": "email address already in use"}), 400

        if M_users.insert_one(user):
            return self.start_session(user)

        return jsonify({'error': "Signup failed"}), 400

    def signOut(self):
        session['logged_in'] = False
        session['user'] = {}

        return redirect('/')

    def logIn(self):
        u = M_users.find_one({'email': request.form.get('email')})
        if u and check_password_hash(u['password'], request.form.get('password')):
            return self.start_session(u)
        else:
            return jsonify({"error": "Invalid credentials"}), 401

