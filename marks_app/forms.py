from django import forms
from .models import Marks

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['subject', 'ct1', 'ct2', 'ct3', 'mid', 'final']