from .base import *
from .base import env, ROOT_DIR

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default="django-insecure-%rj_-9(*y^jsn(*pr&i6i314s*)_n@0p&$i&j(g_b@ig!-uaxg")

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ROOT_DIR / 'db.sqlite3',
    }
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
