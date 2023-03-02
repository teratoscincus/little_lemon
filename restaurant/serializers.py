from rest_framework import serializers

from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            "title",
            "price",
            "inventory",
        ]
        extra_kwargs = {
            "price": {"min_value": 0.1},
            "inventory": {"min_value": 0.1},
        }
