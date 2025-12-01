# apps/doctype/forms.py - 5
from django import forms
from .models import StockDocType

class StockDocTypeForm(forms.ModelForm):
    STATUS_CHOICES = [
        (1, 'Active'),
        (2, 'Inactive'),
    ]

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = StockDocType
        fields = ['name', 'description', 'status']  # exclude created_at and updated_at

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
