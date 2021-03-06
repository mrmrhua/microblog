import os

#配置文件
CSRF_ENABLED = True #CSRF保护

SECRET_KEY = 'you-will-never-guess'
#open-id提供者
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')  #数据库文件的路径
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')  #数据文件存储地址