# apps/items/models.py - 2 
from django.db import models
from apps.categories.models import StockItemCategories  # Import the categories model
from apps.uom.models import StockItemUOM  # Import the UOM model

class StockItems(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(StockItemCategories, on_delete=models.SET_NULL, null=True, blank=True)
    uom = models.ForeignKey(StockItemUOM, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'stock_items'  # Ensure this matches the actual table in your DB
        managed = False  # Do NOT let Django alter the table

    def __str__(self):
        return self.code  # Display the 'code' field as the string representation
