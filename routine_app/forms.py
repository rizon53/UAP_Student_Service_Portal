from django import forms
from .models import Routine

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['course_name', 'day', 'time', 'routine_file']  # ✅ added routine_file