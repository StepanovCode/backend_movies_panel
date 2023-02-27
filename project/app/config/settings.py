from pathlib import Path
import os
from dotenv import load_dotenv
from split_settings.tools import include


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')

DEBUG = int(os.environ.get("DEBUG", default=1))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", '').split()

include(
    'components/database.py',
    'components/application.py',
    'components/pswd_validation.py',
    'components/internationalization.py',
)

INTERNAL_IPS = [
    os.environ.get('HOST'),
]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = BASE_DIR

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOCALE_PATHS = ['movies/locale']

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

PAGINATION_DEFAULT_PAGE_SIZE = 50
PAGINATION_MAX_PAGE_SIZE = 1000
PAGINATION_MIN_PAGE_SIZE = 5
