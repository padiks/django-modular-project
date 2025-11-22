# apps/uom/forms.py
from django import forms
from .models import StockItemUOM

class StockItemUOMForm(forms.ModelForm):
    STATUS_CHOICES = [
        (1, 'Active'),
        (2, 'Inactive'),
    ]

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = StockItemUOM
        fields = ['name', 'description', 'status']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
