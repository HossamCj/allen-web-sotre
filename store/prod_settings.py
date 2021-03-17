import os

from .settings import *


SECRET_KEY = os.environ('SECRET_KEY')

ALLOWED_HOSTS = ['allen-web-store.herokuapp.com']