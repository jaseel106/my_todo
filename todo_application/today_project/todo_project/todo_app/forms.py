from . models import task
from django import forms

class todoForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ['name', 'priority']