# coding=utf-8
import os
# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = 'microblogmli' # enter your MS translator app id here
MS_TRANSLATOR_CLIENT_SECRET = 'cx9DV4QWohpRTqA/NtYMvuDVxliHzx9hX0FRMcQdGqQ=' # enter your MS translator app secret here
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

basedir = os.path.abspath(os.path.dirname(__file__))

#database config
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#fulltext search config
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

# mail server settings
# MAIL_SERVER = 'localhost'
# MAIL_PORT = 2555
# MAIL_USERNAME = None
# MAIL_PASSWORD = None

# pagination
POSTS_PER_PAGE = 3

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['li.mingxyz@gmail.com']

# -*- coding: utf-8 -*-
# ...
# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

