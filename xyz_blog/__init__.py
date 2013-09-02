from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
import os
app = Flask(__name__)


#import sqlite3
#import psycopg2
#import urlparse

app.secret_key = 'rloterh key'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/blog'
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres://pkvakvqzimvxsx:qNW4pR7UQvvGN73o7puEFFKZy4@ec2-54-221-199-33.compute-1.amazonaws.com:5432/d7uhseqbcn6te6')


from models import db
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

import xyz_blog.routes
'''
engine = create_engine('postgresql://postgres:admin@localhost:5432/blog')
Base.metadata.create_all(engine)

from models import sa
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


Session = sessionmaker(bind=engine)
session = Session()

article1 = Entries(topic=u'First article', article=u'This is the first article')
article2 = Entries(topic=u'Second article', article=u'This is the second article')

session.add(article1)
session.add(article2)
session.commit()

import xyz_blog.routes
'''
