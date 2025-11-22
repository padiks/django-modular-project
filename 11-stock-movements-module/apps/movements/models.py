# apps/movements/models.py
from django.db import models
from django.utils import timezone
from apps.items.models import StockItems
from apps.doctype.models import StockDocType

class StockMovements(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]

    id = models.AutoField(primary_key=True)

    item = models.ForeignKey(
        StockItems,
        on_delete=models.DO_NOTHING,
        db_column='item_id'
    )

    document_type = models.ForeignKey(
        StockDocType,
        on_delete=models.DO_NOTHING,
        db_column='document_type_id'
    )

    document_number = models.IntegerField()
    document_reference = models.TextField(null=True, blank=True)
    quantity = models.IntegerField()

    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    movement_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'stock_movements'
        managed = False  # DO NOT let Django modify the table

    def __str__(self):
        return f"Movement #{self.id} - {self.item.code}"

    def save(self, *args, **kwargs):
        """
        Automatically set updated_at to now on save.
        Keep created_at unchanged for existing records.
        """
        if not self.id:
            # New record → set created_at
            self.created_at = timezone.now()
        # Always update updated_at
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
