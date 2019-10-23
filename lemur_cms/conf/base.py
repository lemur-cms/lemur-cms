import os
from app_loader.config import Config, MasterConfig
from app_loader.utils import merge
from lemur_cms.conf.spec import CONF_SPEC, DJANGO_CONF
from lemur_cms.utils.versions import get_versions


class ModuleConfig(Config):

    """Simple Module Config Object
    encapsulation of dot access dictionary

    use dictionary as constructor

    """

    def get_value(self, key, values):
        '''Accept key of propery and actual values'''
        return merge(values, self.get_property(key))

    def get_property(self, key):
        """Expect Django Conf property"""
        _key = DJANGO_CONF[key]
        return getattr(self, _key, CONF_SPEC[_key])

    @property
    def module_name(self):
        """Module name from module if is set"""
        if hasattr(self, "module"):
            return self.module.__name__
        return None

    @property
    def name(self):
        """Distribution name from module if is set"""
        if hasattr(self, "module"):
            return self.module.__name__.replace('_', '-')
        return None

    @property
    def version(self):
        """return module version"""
        return get_versions([self.module_name]).get(self.module_name, None)

    def set_module(self, module):
        """Just setter for module"""
        setattr(self, "module", module)


class LemurCMSConfig(MasterConfig):

    def get_attr(self, name, default=None, fail_silently=True):
        """try extra context
        """
        try:
            return getattr(self, name)
        except KeyError:
            extra_context = getattr(self, "extra_context")

            if name in extra_context:
                value = extra_context[name]

                if callable(value):
                    return value(request=None)

            return default
