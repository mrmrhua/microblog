from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
# app.config['SECRET_KEY']='I WILL NEVER'

db = SQLAlchemy(app)  #初始化数据库

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app,os.path.join(basedir,'tmp'))
print('oid get')

# from app import views
from app import views, models