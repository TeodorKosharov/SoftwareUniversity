from rest_framework import serializers
from django_rest_framework.api.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
