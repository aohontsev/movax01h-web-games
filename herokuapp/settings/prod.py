from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECURITY WARNING: keep the secret key used in production secret!
print os.environ
SECRET_KEY = os.environ.get('_SECRET_KEY')
