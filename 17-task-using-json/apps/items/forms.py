# apps/items/forms.py
from django import forms
from apps.categories.models import StockItemCategories  # Import StockItemCategories
from apps.uom.models import StockItemUOM  # Import StockItemUOM
from .models import StockItems

class StockItemsForm(forms.ModelForm):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]

    category = forms.ModelChoiceField(
        queryset=StockItemCategories.objects.filter(status=1),  # Only active categories
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label='Select a category'
    )

    uom = forms.ModelChoiceField(
        queryset=StockItemUOM.objects.all(),  # Get all UOMs
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label='Select a UOM'
    )

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = StockItems
        fields = ['code', 'description', 'category', 'uom', 'status']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
