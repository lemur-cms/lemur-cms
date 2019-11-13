import os
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from .base import lemur_cms

from rest_framework import routers

admin.autodiscover()

# init rest-framework router
router = routers.DefaultRouter()

urlpatterns = []

urlpatterns += lemur_cms.urlpatterns

urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'', include('feincms.contrib.preview.urls')),
    url(r'', include('feincms.urls'))
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,
)
