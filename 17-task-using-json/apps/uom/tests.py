# apps/uom/tests.py
# python manage.py test apps.uom.tests
from django.test import TestCase
from .models import StockItemUOM

class StockItemUOMTestCase(TestCase):

    def setUp(self):
        # Setup some initial data in the test database
        StockItemUOM.objects.create(
            name='Test UOM',
            description='A test UOM description',
            status=1,
            created_at='2023-01-01 00:00:00',
            updated_at='2023-01-01 00:00:00'
        )

    def test_uom_created(self):
        # Test if the StockItemUOM object is created properly
        uom = StockItemUOM.objects.get(name='Test UOM')
        self.assertEqual(uom.name, 'Test UOM')
        self.assertEqual(uom.status, 1)
        self.assertIsNotNone(uom.created_at)
        self.assertIsNotNone(uom.updated_at)

    def test_uom_count(self):
        # Test the count of records
        uom_count = StockItemUOM.objects.count()
        self.assertEqual(uom_count, 1)
