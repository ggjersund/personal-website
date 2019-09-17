from . base import *
from . dev import *
from . prod import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
