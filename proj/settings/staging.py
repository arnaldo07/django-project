# Settings modifications for staging environment
import os

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

TEMPLATE_DEBUG= False

ALLOWED_HOSTS = [
    "localhost",
    ".herokuapp.com"
]

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static File Storage Credentials
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = "django_proj_static_staging"

# django-storages file storage backend adapters
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Static files (CSS, JavaScript, Images)

STATIC_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME