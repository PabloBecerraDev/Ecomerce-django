from .base import *
import os
from applications.Users.functions import *



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'E-comerce',
        'USER': 'pablo',
        'PASSWORD': 'pablo123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')



# email settings 
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = obtener_contenido_variable("email")
EMAIL_HOST_PASSWORD = obtener_contenido_variable("password")
EMAIL_PORT = 587
