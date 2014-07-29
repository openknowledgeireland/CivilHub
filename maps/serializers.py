# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.utils.translation import gettext as _
from .models import MapPointer


class MapPointerSerializer(serializers.ModelSerializer):
    """
    Serializer for map pointer.
    """
    class Meta:
        model = MapPointer


class MapObjecSerializer(serializers.ModelSerializer):
    """
    This serializer takes map pointer and related object and presents
    data in fixed format to display in map dialog.
    """
    lat = serializers.FloatField(source='latitude')
    lng = serializers.FloatField(source='longitude')
    content_object = serializers.SerializerMethodField('get_content_object')
    
    class Meta:
        model = MapPointer
        fields = ('lat', 'lng', 'content_object',)

    def get_content_object(self, obj):
        tmpobj = {
            'title': obj.content_object.__unicode__(),
            'url': obj.content_object.get_absolute_url(),
            'type': obj.content_object._meta.verbose_name,
            'desc': obj.content_object.get_description()
        }
        return tmpobj