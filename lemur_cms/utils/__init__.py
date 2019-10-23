
from lemur_cms.utils.settings import dotdict, get_conf_from_module, merge
from lemur_cms.utils.widgets import (find_widget_class, get_all_widget_classes,
                                    get_grouped_widgets, load_widget_classes, render_region)

__all__ = ('dotdict', 'get_conf_from_module', 'get_lemur_cms_modules',
           'merge', 'find_widget_class', 'get_all_widget_classes',
           'get_grouped_widgets',)


def is_lemur_cms_module(mod):
    """returns True if is lemur_cms module
    """

    if hasattr(mod, 'default') \
            or hasattr(mod, 'lemur_cms_module_conf'):
        return True
    for key in dir(mod):
        if 'LEMURCMS' in key:
            return True
    return False
