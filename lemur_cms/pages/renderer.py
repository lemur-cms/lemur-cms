from django.utils.html import mark_safe

from feincms3.renderer import TemplatePluginRenderer

from lemur_cms.pages import models


renderer = TemplatePluginRenderer()
renderer.register_string_renderer(
    models.RichText,
    lambda plugin: mark_safe(plugin.text),
)
renderer.register_template_renderer(
    models.Image,
    'plugins/image.html',
)
