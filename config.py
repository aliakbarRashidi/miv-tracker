import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_BROKER_BACKEND = 'redis://127.0.0.1:6379'

FEED_CONFIG = os.path.join(basedir, 'feeder/feed.json')

# miscellaneous
APP_VERSION = "v.1.0.0-beta"
