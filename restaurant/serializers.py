from rest_framework import serializers

from .models import MenuItem, Booking


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            "title",
            "price",
            "inventory",
        ]
        extra_kwargs = {
            "price": {"min_value": 0.1},
            "inventory": {"min_value": 0.1},
        }


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
