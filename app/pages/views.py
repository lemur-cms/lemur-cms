from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from feincms3.regions import Regions
from rest_framework import viewsets, generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Page
from .renderer import renderer
from .serializers import PageSerializer


def page_detail(request, path=None):
    page = get_object_or_404(
        Page.objects.active(),
        path='/{}/'.format(path) if path else '/',
    )
    page.activate_language(request)
    return render(request, page.template.template_name, {
        'page': page,
        'regions': Regions.from_item(
            page, renderer=renderer, inherit_from=page.ancestors().reverse()),
    })


class PageViewSet(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all()


class PageAPIView(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'is_active', 'parent', 'language_code', 'position', 'menu']

