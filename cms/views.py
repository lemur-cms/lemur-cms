from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, filters, generics
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from cms.models import Page
from cms.serializers import PageSerializer


def cms_home(request):
    return HttpResponse("<h>Works</h1>")


class PageViewSet(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # pagination_class = StandardResultsSetPagination
    filterset_fields = ('title', 'parent', 'in_navigation', 'language', 'active')
    ordering_fields = ('id', 'title', 'parent')
    ordering = 'title'

    def filter_queryset(self, queryset):
        queryset = super(PageViewSet, self).filter_queryset(queryset)
        return queryset.order_by('active')

