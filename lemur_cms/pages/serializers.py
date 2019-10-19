from rest_framework import serializers
from content_editor.models import Region
from .models import Page


class PageSerializer(serializers.ModelSerializer):
    regions = serializers.SerializerMethodField()
    
    def get_regions(self, obj):
        return obj.get_plugins()
    
    class Meta:
        model = Page
        fields = ("title", "regions")

