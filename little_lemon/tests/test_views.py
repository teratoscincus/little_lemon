from django.test import TestCase

from restaurant.views import MenuItemView, MenuItem, MenuSerializers


class MenuViewTestCase(TestCase):
    def setUp(self) -> None:
        title = "ice cream"
        price = 80
        self.menu_item = MenuItem.objects.create(title=title, price=price, inventory=50)
