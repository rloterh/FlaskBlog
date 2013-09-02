from flask.ext.sqlalchemy import SQLAlchemy
#from werkzeug import generate_password_hash, check_password_hash
import datetime


#import sqlalchemy as sa
#from sqlalchemy.ext.declarative import declarative_base

#from sqlalchemy_searchable import Searchable
#from sqlalchemy_utils.types import TSVectorType

db = SQLAlchemy()

ROLE_USER = 0
ROLE_ADMIN = 1

#USERS MODEL
class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pwd = db.Column(db.String(100))
    role = db.Column(db.Integer, default = 0)

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.pwd = password

    def check_password(self, password):
        if self.pwd == password:
            return True

    def is_authenticated(self):
        return True
    '''
    def get_id(self):
        return unicode(self.uid)'''

    def __repr__(self):
        return '<User %r>' % (self.email)

    def get_id(uid):
        for user in User:
            if user[0] == uid:
                return user(user[0], [1])
        return None
'''
    def is_active(self):
        return True '''

'''
    def is_anonymous(self):
        return False  '''


# POST ENTRIES MODEL
class Entries(db.Model):
    __tablename__ = 'published'
    pub_id = db.Column(db.Integer, primary_key = True)
    topic = db.Column(db.String(100))
    article = db.Column(db.String(100))
    email = db.Column(db.String(100))
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    pub_date = db.Column(db.DateTime, default = datetime.datetime.now() )

    def __init__(self, topic, article, email, firstname, lastname, pub_date):
        self.topic = topic.title()
        self.article = article.title()
        self.email = email.lower()
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.pub_date = datetime.datetime.now()



'''
#USERS MODEL
class User(Base, Searchable):
    __tablename__ = 'users'
    __searchable_columns = []
    uid = sa.Column(db.Integer, primary_key = True)
    firstname = sa.Column(db.String(100))
    lastname = sa.Column(db.String(100))
    email = sa.Column(db.String(120), unique=True)
    pwd = sa.Column(db.String(100))
    role = sa.Column(db.Integer, default = 0)
    search_vector = sa.Column(TSVectorType)

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.pwd = password

    def check_password(self, password):
        if self.pwd == password:
            return True

    def is_authenticated(self):
        return True


    def get_id(self):
        return unicode(self.uid)

    def __repr__(self):
        return '<User %r>' % (self.email)

    def get_id(uid):
        for user in User:
            if user[0] == uid:
                return user(user[0], [1])
        return None

    def is_active(self):
        return True


    def is_anonymous(self):
        return False
'''

'''
# POST ENTRIES MODEL
class Entries(Base, Searchable):
    __tablename__ = 'published'
    __searchable_columns = ['topic', 'article']
    pub_id = sa.Column(db.Integer, primary_key = True)
    topic = sa.Column(db.String(100))
    article = sa.Column(db.String(100))
    email = sa.Column(db.String(100))
    firstname = sa.Column(db.String(20))
    lastname = sa.Column(db.String(20))
    pub_date = sa.Column(db.DateTime, default = datetime.datetime.now() )
    search_vector = sa.Column(TSVectorType)

    def __init__(self, topic, article, email, firstname, lastname, pub_date):
        self.topic = topic.title()
        self.article = article.title()
        self.email = email.lower()
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.pub_date = datetime.datetime.now()
'''
