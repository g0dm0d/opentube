#nothing ¯\_(ツ)_/¯
import psycopg2
db = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="123",
            host='127.0.0.1')
cur = db.cursor()

username = 'test'
password_hash = 'test'
email = 'test'

cur.execute("INSERT INTO users VALUES(%(username)s, %(password)s, %(email)s, CURRENT_TIMESTAMP, 'default')",
{
    'username': username,
    'password': password_hash,
    'email': email
})
db.commit()