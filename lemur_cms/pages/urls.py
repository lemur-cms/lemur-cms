from __future__ import unicode_literals

from django.conf.urls import url
from django.urls import path, include
from django.http import HttpResponseRedirect
from rest_framework import routers
from lemur_cms.pages import views

router = routers.DefaultRouter()
router.register(r'pages', views.PageViewSet, 'page')

app_name = 'pages'
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/get/pages/', views.PageAPIView.as_view(), name='page_list'),
    url(
        r'^$',
        lambda request: HttpResponseRedirect('/%s/' % request.LANGUAGE_CODE),
    ),
    url(
        r'^(?P<path>[-\w/]+)/$',
        views.page_detail,
        name='page',
    ),
    url(
        r'^$',
        views.page_detail,
        name='root',
    ),
]
