
from __future__ import absolute_import, unicode_literals

import logging
import re

from django import template
from django.conf import settings
from django.core.cache import caches
from django.template import TemplateSyntaxError
from django.template.defaulttags import kwarg_re
from django.utils.encoding import smart_str
from django.utils.translation import ugettext as _


register = template.Library()

def _render_content(content, **kwargs):
    # Track current render level and abort if we nest too deep. Avoids
    # crashing in recursive page contents (eg. a page list that contains
    # itself or similar).
    request = kwargs.get('request')
    if request is not None:
        level = getattr(request, 'feincms_render_level', 0)
        if level > 10:
            logging.getLogger('feincms').error(
                'Refusing to render %r, render level is already %s' % (
                    content, level))
            return
        setattr(request, 'feincms_render_level', level + 1)

    if request is not None:
        level = getattr(request, 'feincms_render_level', 1)
        setattr(request, 'feincms_render_level', max(level - 1, 0))

    cache = caches['default']

    if not request.frontend_editing and content.is_cached(request):
        value = cache.get(content.cache_key)
        if value is None:
            value = content.render(**kwargs)
            cache.set(content.cache_key, value, content.widget_cache_timeout)
        return value

    return content.render(**kwargs)
