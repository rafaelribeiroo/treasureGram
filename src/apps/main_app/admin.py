from django.contrib import admin
from .models import Treasure


@admin.register(Treasure)
class TreasureAdmin(admin.ModelAdmin):
    fields = ['user', 'name', 'value', 'material', 'location', 'image']
    list_display = ['user', 'id', 'name', 'value', 'material', 'location', 'image']
    list_filter = ['user', 'name', 'value', 'material', 'location', 'image']
    search_fields = ['user', 'name', 'value', 'material', 'location', 'image']

    class Meta:
        model = Treasure
