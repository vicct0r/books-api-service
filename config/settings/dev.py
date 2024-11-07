from .base import *
import os

SECRET_KEY = 'django-insecure-$%bid9zmx-)1nu!_6*3p0qsp*(qo(#y8@!7vq@w%l-0*@#!&pi'

DEBUG = True

ALLOWED_HOSTS = ['*']


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
