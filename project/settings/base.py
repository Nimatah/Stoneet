from pathlib import Path

from django.utils.translation import ugettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'he1r&ba+b!+*vcav!63=s-6sz^3ge#9$t^4d7c141x$j_!#d*g'

DEBUG = True

ALLOWED_HOSTS = ['*']

PREREQUISITE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'rest_framework',
    'mptt',
    'django_extensions',
    'widget_tweaks',
    'django_filters',
    'huey.contrib.djhuey',
]

PROJECT_APPS = [
    'apps.core.static_app.MadanStaticfilesConfig',
    'apps.locations.apps.LocationsConfig',
    'apps.home.apps.HomeConfig',
    'apps.users.apps.UsersConfig',
    'apps.products.apps.ProductsConfig',
    'apps.orders.apps.OrdersConfig',
    'apps.invoices.apps.InvoicesConfig',
    'apps.auction.apps.AuctionConfig',
    'apps.moderation.apps.ModerationConfig'
]

INSTALLED_APPS = PREREQUISITE_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = False

USE_TZ = False

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'assets'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'apps.core.static_app.NodeModulesFinder'
]

NODE_MODULES_ROOT = BASE_DIR / 'node_modules'

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'apps.core.authentication.CsrfExemptSessionAuthentication',
    ),
}

LOCALE_PATHS = (
    BASE_DIR / 'locale',
)

LANGUAGES = (
    ('en-US', _('english'),),
    ('fa-IR', _('persian'),),
)


HUEY = {
    'huey_class': 'huey.RedisHuey',
    'name': "plantask",
    'results': True,
    'store_none': False,
    'immediate': False,
    'utc': False,
    'blocking': True,
    'connection': {
        'host': 'localhost',
        'port': 6379,
        'db': 1,
        'connection_pool': None,
        'read_timeout': 1,
    },
    'consumer': {
        'workers': 1,
        'worker_type': 'thread',
        'initial_delay': 0.1,
        'backoff': 1.15,
        'max_delay': 10.0,
        'scheduler_interval': 1,
        'periodic': True,
        'check_worker_health': True,
        'health_check_interval': 1,
    },
}

EMAIL_HOST = 'mail.stoneet.com'
EMAIL_HOST_USER = 'info@stoneet.com'
EMAIL_HOST_PASSWORD = 'Stoneet@123'
EMAIL_USE_TLS = False
EMAIL_TIMEOUT = 10
EMAIL_PORT = 587

MAX_UPLOAD_SIZE = 10485760
