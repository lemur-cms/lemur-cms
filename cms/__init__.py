
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'cms.CMSConfig'


class Default(object):

    optgroup = ('CMS')
    
    apps = [
        'cms',
        'easy_thumbnails'
    ]

    public = True


class CMSConfig(AppConfig, Default):
    name = 'cms'
    verbose_name = ('CMS')

default = Default()
