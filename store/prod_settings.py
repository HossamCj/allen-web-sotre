# import os
# import dj_database_url
#
# from .settings import *
#
# SECRET_KEY = os.environ.get('SECRET_KEY')
#
# # DEBUG = False
#
#
# DATABASES = {
#     'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
# }
#
# ALLOWED_HOSTS = ['allen-web-store.herokuapp.com']
#

import os
from .settings import *
import dj_database_url



SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['web-store1.herokuapp.com',]

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}