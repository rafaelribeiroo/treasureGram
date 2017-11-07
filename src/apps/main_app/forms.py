from django import forms
from .models import Treasure


class TreasureForm(forms.Form):
    class Meta:
        model = Treasure
        fields = ['name', 'value', 'material', 'location', 'img_url']
