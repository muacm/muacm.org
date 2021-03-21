import os
from .base import *

SECRET_KEY = "jahg48r8tw8v4ylr84n9cywrtv3_cv35650"
DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']


EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"  # for gmail
EMAIL_HOST_USER = "mymail@gmail.com"  # TODO change it
EMAIL_HOST_PASSWORD = "password"
EMAIL_PORT = 587  # for gmail

# Also remember if you are using gmail, you need to allow less secure apps option, in privacy setting,
