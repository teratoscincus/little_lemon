from django.contrib import admin

from .models import Booking, MenuItem

admin.site.register(
    [
        Booking,
        MenuItem,
    ]
)
