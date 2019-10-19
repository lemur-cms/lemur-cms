from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from content_editor.models import Region, Template, create_plugin_base

from feincms3.apps import AppsMixin
from feincms3.mixins import TemplateMixin, MenuMixin, LanguageMixin
from feincms3.pages import AbstractPage
from feincms3.plugins import image, richtext
from django.shortcuts import get_object_or_404
from content_editor.contents import contents_for_item
from app.pages.utils import get_available_renderers
import json


class mydict(dict):
        def __str__(self):
            return json.dumps(self)


class Page(
    AbstractPage,
    AppsMixin,      # For adding the articles app to pages through the CMS.
    TemplateMixin,  # Two page templates, one with only a main
                    # region and another with a sidebar as well.
    MenuMixin,      # We have a main and a footer navigation (meta).
    LanguageMixin,  # We're building a multilingual CMS. (Also,
                    # feincms3.apps depends on LanguageMixin
                    # currently.)
):

    # TemplateMixin
    TEMPLATES = [
        Template(
            key='standard',
            title=_('standard'),
            template_name='pages/standard.html',
            regions=(
                Region(key='main', title=_('Main'), content='contents.main'),
                Region(key='footer', title=_('Footer'), inherited=True, content='contents.footer'),
            ),
        ),
        Template(
            key='with-sidebar',
            title=_('with sidebar'),
            template_name='pages/with-sidebar.html',
            regions=(
                Region(key='main', title=_('Main'), content='contents.main'),
                Region(key='sidebar', title=_('Sidebar'), content='contents.sidebar'),
                Region(key='footer', title=_('Footer'), inherited=True, content='contents.footer'),
            ),
        ),
    ]

    # MenuMixin
    MENUS = [
        ('main', _('main')),
        ('footer', _('footer')),
    ]

    def get_plugins(self):
        renderers = get_available_renderers()
        page = get_object_or_404(Page, pk=self.id)
        contents = contents_for_item(page, PagePlugins)
        data = []
        for region in self.regions:
            new_data = {
                region.key : [
                    dict(
                        renderers[plugin.__class__](plugin),
                        type=plugin.__class__.__name__,
                        lang=page.language_code,
                        parent=page.slug
                    )
                ]
                for plugin in eval(region.content)
            }
            data.append(new_data)
        return data

    # AppsMixin. We have two apps, one is for company PR, the other
    # for a more informal blog.
    #
    # NOTE! The app names (first element in the tuple) have to match the
    # article categories exactly for URL reversing and filtering articles by
    # app to work! (See app.articles.models.Article.CATEGORIES)
    APPLICATIONS = [
        ('publications', _('publications'), {
            'urlconf': 'app.articles.urls',
        }),
        ('blog', _('blog'), {
            'urlconf': 'app.articles.urls',
        }),
    ]


PagePlugin = create_plugin_base(Page)


class RichText(richtext.RichText, PagePlugin):
    pass


class Image(image.Image, PagePlugin):
    caption = models.CharField(
        _('caption'),
        max_length=200,
        blank=True,
    )

PagePlugins = [RichText, Image]
