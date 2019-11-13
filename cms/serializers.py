from rest_framework import serializers

from .models import Page


class PageSerializer(serializers.ModelSerializer):
    regions = serializers.SerializerMethodField()
    template_name = serializers.SerializerMethodField()

    @staticmethod
    def get_regions(obj):
        data = {}
        for region in obj.template.regions:
            region_content = eval("obj.content." + region.key)
            widgets = []
            for widget in region_content:
                _widget = {
                    'id': widget.id,
                    'content': widget.render(),
                    'region': widget.region
                }
                widgets.append(_widget)
            data[region.key] = widgets
        return data

    @staticmethod
    def get_template_name(obj):
        return obj.template.title

    class Meta:
        model = Page
        fields = '__all__'
