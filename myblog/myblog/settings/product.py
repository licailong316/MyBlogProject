from .base import *  # NOQA


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.licailong.cn', 'licailong.cn', '114.55.128.123']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangomyblog',
        'USER': 'root',
        'PASSWORD': '316licailongLCL@',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'CONN_MAX_AGE': 60,
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}