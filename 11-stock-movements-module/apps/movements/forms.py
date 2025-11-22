from django import forms
from django.utils import timezone
from .models import StockMovements

class StockMovementsForm(forms.ModelForm):

    movement_date = forms.DateTimeField(
        initial=timezone.now,
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',  # HTML5 datetime picker
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = StockMovements
        fields = [
            'item',
            'document_type',
            'document_number',
            'document_reference',
            'quantity',
            'status',
            'movement_date',
        ]

        widgets = {
            'item': forms.Select(attrs={'class': 'form-select'}),
            'document_type': forms.Select(attrs={'class': 'form-select'}),
            'document_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'document_reference': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            # 'movement_date' is now defined above with datetime-local picker
        }
