from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _


class PagesConfig(AppConfig):
    name = 'lemur_cms.pages'
    verbose_name = capfirst(_('pages'))
