from lemur_cms.pages import models

def get_available_renderers():
    renderers = {
        models.RichText: lambda plugin: {
            "text": plugin.text
        },
        models.Image: lambda plugin: {
            "image": plugin.image.url
        },
    }
    return renderers
