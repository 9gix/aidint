# Local settings for aidint project.
LOCAL_SETTINGS = True
from settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Fabric Configuration
FAB_CONFIGS = {
    'prod': {
        'SSH_KEY':'', # /home/user/.ssh/key.pem
        'HOST':'', # eugene-yeo.me
        'BRANCH':'', # master
        'USER':'', # ec2-user
        'PATH':'', # /home/ec2-user/projectpath
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# Email Configuration
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ''

if DEBUG:
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
