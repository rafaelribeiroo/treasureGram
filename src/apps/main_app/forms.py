from django import forms
from .models import Treasure


class TreasureForm(forms.Form):
    class Meta:
        model = Treasure
        fields = ['name', 'value', 'location', 'material', 'img_url']
     