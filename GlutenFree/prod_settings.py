# coding=utf-8
import os


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'GlutenFreeDB',
        'USER': 'Serov',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



