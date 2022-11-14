'''Dev Settings, customised settings for our development envirenment

The import *,  is used just for django
don't do that in other place, always specify the modules to import
for best practice
 '''
from .base import *


# We no longer need to check if we are in DEBUG or PRODUCTION mode
DEBUG = True


# Specific database for developments
# make sure that, Databases are similair in Both Dev and Production
# if you are using SQLite in Dev, use it also for Production
# for best practice
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR.child("db.sqlite3"),
    }
}

# add other usefull libraries for development
# INSTALLED_APPS += ('debug_toolbar',)

''' Custom Developer Settings 

Ex: For me Tidjini ;)
'''


# short cahche timout
CACHE_TIMEOUT = 30
