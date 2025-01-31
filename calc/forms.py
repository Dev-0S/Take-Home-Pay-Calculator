from datetime import date
from django import forms

class TaxForm(forms.Form):
    income = forms.FloatField(label='Enter your income', min_value=0)
