from django.test import TestCase

from restaurant.models import MenuItem


class MenuItemTestCase(TestCase):
    def test_string_representation(self):
        title = "ice cream"
        price = 80
        menu_item = MenuItem.objects.create(title=title, price=price, inventory=50)
        self.assertEqual(str(menu_item), f"{title} : {price}")
