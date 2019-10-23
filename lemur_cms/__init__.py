
default_app_config = 'lemur_cms.conf.base.LemurCMSConfig'

__import__('pkg_resources').declare_namespace(__name__)


try:
    from lemur_cms.base import lemur_cms  # noqa
except ImportError:
    import warnings

    def simple_warn(message, category, filename, lineno, file=None, line=None):
        return '%s: %s' % (category.__name__, message)

    msg = ("Could not import LemurCMS dependencies. "
           "This is normal during installation.\n")
    warnings.formatwarning = simple_warn
    warnings.warn(msg, Warning)
