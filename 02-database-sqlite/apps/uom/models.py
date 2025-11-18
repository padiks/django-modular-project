from django.db import models

class StockItemUOM(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'stock_items_uom'  # use your exact table
        managed = False               # <-- IMPORTANT: do NOT create or change table

    def __str__(self):
        return self.name
