from django.urls import path

from . import views

app_name = "restaurant"
urlpatterns = [
    # Webpage URLs
    path("", views.index, name="index"),
    # API URLs
    path("restaurant/menu", views.MenuItemView.as_view(), name="menu_items"),
    path(
        "restaurant/menu/<int:pk>",
        views.MenuItemView.as_view(),
        name="single_menu_item",
    ),
]
