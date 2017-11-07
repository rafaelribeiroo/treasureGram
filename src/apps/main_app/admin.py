from django.contrib import admin
from .models import Treasure


@admin.register(Treasure)
class TreasureAdmin(admin.ModelAdmin):
    fields = ['name', 'value', 'material', 'location', 'image']
    list_display = ['id', 'name', 'value', 'material', 'location', 'image']
    list_filter = ['name', 'value', 'material', 'location', 'image']
    search_fields = ['name', 'value', 'material', 'location', 'image']

    class Meta:
        model = Treasure
