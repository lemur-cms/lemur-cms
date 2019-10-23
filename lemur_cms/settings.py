from __future__ import absolute_import

import os
from django.apps import apps
from lemur_cms.base import lemur_cms, default
from lemur_cms.utils.settings import merge

import os
import six
import logging
import warnings

from django.apps import apps
from lemur_cms.conf.spec import DJANGO_CONF
from lemur_cms.base import lemur_cms, default
from lemur_cms.utils.settings import (get_conf_from_module, merge,
                                     get_loaded_modules)
from importlib import import_module  # noqa
from django.utils.module_loading import module_has_submodule  # noqa
from lemur_cms.conf.default import *

"""
Lemur CMS settings
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0vks5u62=+q71pwlgg4np(e8-(r21nck7(a_(c%yjr5gnr==r='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

APPS = merge(APPS, default.core)

if not apps.ready:
    # load directly specified apps
    lemur_cms.get_app_modules(APPS)

    # propagate settings to lemur_cms
    lemur_cms.MODULES_AUTOLOAD = LEMURCMS_MODULE_AUTO_INCLUDE

    # load all modules
    lemur_cms.load_modules()

    # just propagate all loaded modules to settings
    LEMURCMS_MODULES = lemur_cms.get_modules()

    # iterate over sorted modules
    for mod, mod_cfg in LEMURCMS_MODULES:

        try:
            # go through django keys and merge it to main settings
            for key in DJANGO_CONF.keys():
                updated_value = mod_cfg.get_value(key, globals()[key])
                globals()[key] = updated_value
                locals()[key] = updated_value
                # map value to lemur_cms but under our internal name
                setattr(lemur_cms, DJANGO_CONF[key], updated_value)

            if mod_cfg.urls_conf:
                MODULE_URLS[mod_cfg.urls_conf] = {'is_public': mod_cfg.public}

        except Exception as e:
            warnings.warn(
                'Exception "{}" raised during loading '
                'module {}'.format(str(e), mod))
else:
    warnings.warn("LemurCMS modules are already loaded. Skiped now.")

setattr(lemur_cms, 'widgets', WIDGETS)

# and again merge core with others
APPS = merge(APPS, default.core)

WSGI_APPLICATION = 'lemur_cms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'lemur_db'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', 'EN')
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# cors headers

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:5000',
    'http://localhost:8000',
    'http://localhost:8080',
]
