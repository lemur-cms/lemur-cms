from django.urls import include, path
from cms import views

from lemur_cms.urls import router

app_name = 'pages'

router.register(r'pages', views.PageViewSet, 'page')
