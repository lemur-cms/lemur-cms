from django.db import models
from feincms.module.page.models import Page
from django.utils.translation import ugettext_lazy as _
from feincms.content.richtext.models import RichTextContent
from django.core.validators import MinValueValidator

Page.register_extensions(
    'feincms.extensions.datepublisher',
    'feincms.extensions.translations'
)

Page.register_templates({
    'title': _('LemurCMS default template'),
    'path': 'base.html',
    'regions': (
        ('header', _('Page header'), 'inherited'),
        ('main', _('Main content area')),
        ('sidebar', _('Sidebar'), 'inherited'),
        ('footer', _('Page footer'), 'inherited'),
    ),
})

Page.create_content_type(RichTextContent)

DEFAULT_X = 0
DEFAULT_WIDTH = 12

COLUMN_CHOICES = (
    (DEFAULT_X, str(DEFAULT_X)),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),
    (DEFAULT_WIDTH, '12'),
)


class Widget(models.Model):
    """
    Page Widget
    """

    widget_pos_x = models.IntegerField(verbose_name=_("X position"),
                                       choices=COLUMN_CHOICES, default=DEFAULT_X)
    widget_pos_y = models.IntegerField(verbose_name=_("Y position"), validators=[MinValueValidator(0)], default=0)
    widget_width = models.IntegerField(verbose_name=_("Width"),
                                       choices=COLUMN_CHOICES, default=DEFAULT_WIDTH)
    widget_height = models.IntegerField(verbose_name=_("Height"), validators=[MinValueValidator(1)], default=1)

    class Meta:
        abstract = True
        verbose_name = _("Widget")
        verbose_name_plural = _("Widgets")
