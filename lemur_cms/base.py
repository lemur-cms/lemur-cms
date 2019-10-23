
import warnings

from app_loader.base import AppLoader
from django.conf.urls import url
from django.urls import include, path
from django.utils import six
from django.utils.functional import cached_property
from django.utils.module_loading import module_has_submodule  # noqa
from importlib import import_module  # noqa
from lemur_cms.conf import Default
from lemur_cms.decorators import _decorate_urlconf, require_auth
from lemur_cms.utils import is_lemur_cms_module
from lemur_cms.utils.settings import (get_conf_from_module,
                                     get_loaded_modules,
                                     merge)


# use lemur_cms instead
default = Default()


class LemurCMS(AppLoader):

    '''Main CMS instance

    .. code-block:: python

        from lemur_cms import lemur_cms

        print(lemur_cms.config.apps)
        print(lemur_cms.config.widgets)
    '''

    default = default

    MODULES_AUTOLOAD = True

    CONFIG_MODULE_PREFIX = "LEMURCMS"
    CONFIG_MODULE_SPEC_CLASS = "lemur_cms.conf.spec.CONF_SPEC"
    CONFIG_MODULE_OBJECT_CLASS = "lemur_cms.conf.base.ModuleConfig"
    CONFIG_MASTER_OBJECT_CLASS = "lemur_cms.conf.base.LemurCMSConfig"

    def __init__(self):
        pass

    def get_app_modules(self, apps):
        """return array of imported lemur_cms modules for apps
        """
        modules = getattr(self, "_modules", [])
        if not modules:
            self._modules = modules
        return self._modules

    @cached_property
    def urlpatterns(self):
        '''load and decorate urls from all modules
        then store it as cached property for less loading
        '''
        if not hasattr(self, '_urlspatterns'):
            urlpatterns = []
            # load all urls
            # support .urls - automatic adds urls to core
            # decorate all url patterns if is not explicitly excluded
            for mod in lemur_cms.modules:
                if is_lemur_cms_module(mod):
                    conf = get_conf_from_module(mod)
                    if module_has_submodule(mod, 'urls'):
                        urls_mod = import_module('.urls', mod.__name__)
                        if hasattr(urls_mod, 'urlpatterns'):
                            # if not public decorate all
                            if conf['public']:
                                urlpatterns += urls_mod.urlpatterns
                            else:
                                _decorate_urlconf(urls_mod.urlpatterns,
                                                  require_auth)
                                urlpatterns += urls_mod.urlpatterns
            self._urlpatterns = urlpatterns
        return self._urlpatterns

    _instance = None

lemur_cms = LemurCMS()
