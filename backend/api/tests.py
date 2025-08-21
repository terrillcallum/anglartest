from django.test import TestCase
from rest_framework.test import APIClient

from .models import Item


class ItemModelTests(TestCase):
    def test_seed_items_exist(self):
        self.assertGreaterEqual(Item.objects.count(), 3)


class ItemAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_items_endpoint_returns_quantities(self):
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreaterEqual(len(data), 3)

        expected = {
            'Apples': 5,
            'Bananas': 3,
            'Cherries': 8,
        }

        for name, quantity in expected.items():
            item = next((i for i in data if i['name'] == name), None)
            self.assertIsNotNone(item, f"{name} not returned")
            self.assertEqual(item['quantity'], quantity)
