import peewee

db = peewee.sqlite3('data.db')

class User(peewee.Model):
    pass