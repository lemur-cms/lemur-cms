
from lemur_cms.base import default
import os

EMAIL = {
    'HOST': 'mail.domain.com',
    'PORT': '25',
    'USER': 'username',
    'PASSWORD': 'pwd',
    'SECURITY': True,
}

RAVEN_CONFIG = {}

ALLOWED_HOSTS = ['*']

USE_TZ = True

DEBUG = True

ADMINS = (
    ('admin', 'mail@lemur-cms.cz'),
)

# month
LEMURCMS_CACHE_TIMEOUT = 60 * 60 * 24 * 31

DEFAULT_CHARSET = 'utf-8'

MANAGERS = ADMINS

SITE_ID = 1

SITE_NAME = 'LemurCMS'

TIME_ZONE = 'Europe/Prague'

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'EN'),
    ('cs', 'CS'),
)

USE_I18N = True

DBTEMPLATES_MEDIA_PREFIX = '/static-/'

DBTEMPLATES_AUTO_POPULATE_CONTENT = True

DBTEMPLATES_ADD_DEFAULT_SITE = True

FILER_ENABLE_PERMISSIONS = True  # noqa

MIDDLEWARE = default.middlewares

ROOT_URLCONF = 'lemur_cms.urls'

LEMURCMS_BOOTSTRAP_URL = 'http://github.com/lemur-cms/lemur-cms/raw/master/contrib/bootstrap/demo.yaml'

MARKITUP_FILTER = ('markitup.renderers.render_rest', {'safe_mode': True})

INSTALLED_APPS = default.apps

# For easy_thumbnails to support retina displays (recent MacBooks, iOS)

THUMBNAIL_FORMAT = "PNG"

FEINCMS_USE_PAGE_ADMIN = True

LEMURCMS_USE_PAGE_ADMIN = False

FEINCMS_DEFAULT_PAGE_MODEL = 'page.Page'

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {}

CONSTANCE_ADDITIONAL_FIELDS = {}

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# enable auto loading packages
LEMURCMS_MODULE_AUTO_INCLUDE = True

# enable system module
LEMURCMS_SYSTEM_MODULE = True

##########################


STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

LOGIN_URL = '/auth/login/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = "/"

LOGOUT_ON_GET = True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'lemur_cms': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

BASE_TEMPLATES = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_TEMPLATES],
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

SECRET_KEY = None

APPS = []

PAGE_EXTENSIONS = []

FEINCMS_TIDY_HTML = False

APPLICATION_CHOICES = []

ADD_PAGE_ACTIONS = []

ADD_WIDGET_ACTIONS = []

MIGRATION_MODULES = []

CONSTANCE_ADDITIONAL_FIELDS = []

CONSTANCE_CONFIG_GROUPS = {}

MODULE_URLS = {}

WIDGETS = {}
