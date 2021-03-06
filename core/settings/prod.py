"""
Environment dependent settings: Production
"""

# Deployment checklist
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

from . base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['gjersund.com', 'www.gjersund.com']

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_SSL_REDIRECT = False

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False

X_FRAME_OPTIONS = 'SAME-ORIGIN'

ENVIRONMENT_NAME = 'Production'

ENVIRONMENT_COLOR = 'red'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'var/static')


# Media files (User uploaded content)
# https://docs.djangoproject.com/en/2.2/topics/files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'var/media')
