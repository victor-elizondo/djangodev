from django import forms
from .models import Treasure

# Create your forms here.

class TreasureForm(forms.ModelForm):
    class Meta:
        model = Treasure
        fields = ['name', 'value', 'material', 'location', 'image']

