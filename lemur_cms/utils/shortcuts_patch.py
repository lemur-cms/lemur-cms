
import warnings

import django
from django.http import HttpResponse
from django.template import RequestContext, loader


def render(request, template_name, context={}, content_type=None, status=None, using=None):
    """
    Returns a HttpResponse whose content is filled with the result of calling
    django.template.loader.render_to_string() with the passed arguments.
    """

    if hasattr(request, '_feincms_extra_context') and 'widget' in request._feincms_extra_context:
        context['widget'] = request._feincms_extra_context['widget']
    content = loader.render_to_string(
        template_name, context, request, using=using)
    return HttpResponse(content, content_type, status)


def patch_shortcuts():
    django.shortcuts.render = render
