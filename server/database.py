import psycopg2
import os
from sympy import re
from werkzeug.security import generate_password_hash, check_password_hash


class Database:
    def __init__(self):
        self.db = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="123",
            host='127.0.0.1')
        self.cur = self.db.cursor()

    
    def signup(self, username, password, email):
        password_hash = generate_password_hash(password)
        try:
            self.cur.execute("INSERT INTO users VALUES(%(username)s, %(password)s, %(email)s, CURRENT_TIMESTAMP, 'default')",
            {
                'username': username,
                'password': password_hash,
                'email': email
            })
            self.db.commit()
        except:
            self.db.rollback()


    def is_valid_username(self, username):
        if self.cur.execute("SELECT * FROM users WHERE username = %(username)s",{'username': username}) == 0:
            return False
        else:
            return True


    def login(self, username, password):
        self.cur.execute("SELECT password FROM users WHERE username = %(username)s", {'username': username})
        stored_password = self.cur.fetchone()[0]
        return check_password_hash(stored_password, password)
