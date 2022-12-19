from .base import *
from .base import env


DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-_2&)=(+khr^x2%%vv!%gf#hx%1u3#6(v2wovgg)1i7q*ob-7m9",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]