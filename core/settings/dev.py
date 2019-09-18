"""
Environment dependent settings: Development
"""

from . base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = 'SAME-ORIGIN'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'var/static')


# Media files (User uploaded content)
# https://docs.djangoproject.com/en/2.2/topics/files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'var/media')
