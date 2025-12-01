# apps/<app-name>/forms.py
from django import forms

class ComputeForm(forms.Form):
    input1 = forms.IntegerField(label="Value 1", required=True)
    input2 = forms.IntegerField(label="Value 2", required=True)

