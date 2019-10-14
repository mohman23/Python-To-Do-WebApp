from django import forms
from .models import List #So we can use our list db here

class ListForm(forms.ModelForm):
    class Meta:
        model = List                # List from models.py
        fields = ["item", "completed"]  #From models.py
