from flask import Flask, jsonify


class User:

    def signUp(self):
        user = {
            "_id": "",
            "name": "",
            "email": "",
            "password": "",
            "totp_secret": "",
            "two_fac": False,
            "admin": False
        }

        return jsonify(user), 200
