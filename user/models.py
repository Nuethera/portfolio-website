from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from app import mydb
import uuid

M_users = mydb['users']


class User:

    def signUp(self):
        user = {
            "_id": uuid.uuid4().hex,
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
            return jsonify(user), 200

        return jsonify({'error': "Signup failed"}), 400
